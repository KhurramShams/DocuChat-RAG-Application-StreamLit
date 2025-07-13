from pinecone import Pinecone, ServerlessSpec
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from pdf_utils import validate_pdf
from pdf_utils import process_pdf_and_split
from langchain.chains import RetrievalQA
from pdf_utils import load_environment, initialize_pinecone, initialize_embeddings, initialize_llm, store_chunks_in_pinecone, query_llm_with_rag, get_pdf_hash, is_document_already_indexed
import logging


load_dotenv()

# Define API keys
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
try:
    PINECONE_API_KEY, OPENAI_API_KEY = load_environment()
except Exception as e:
    st.error(f"Error loading environment: {str(e)}")
    logger.error(f"Error loading environment: {str(e)}")
    st.stop()

# Initialize Pinecone
try:
    pc = initialize_pinecone(PINECONE_API_KEY)
    # st.success("Pinecone client initialized successfully")
except Exception as e:
    st.error(f"Error initializing Pinecone: {str(e)}")
    st.stop()

# Initialize embeddings
try:
    embedding_function = initialize_embeddings(OPENAI_API_KEY)
except Exception as e:
    st.error(f"Error initializing embeddings: {str(e)}")
    st.stop()

# Initialize LLM
try:
    llm = initialize_llm(OPENAI_API_KEY)
except Exception as e:
    st.error(f"Error initializing LLM: {str(e)}")
    st.stop()

# Initialize PineconeVectorStore
try:
    vector_store = PineconeVectorStore(
    index_name="rag-index",
    embedding=embedding_function,
    pinecone_api_key=PINECONE_API_KEY
    )
except Exception as e:
    st.error(f"Error initializing DataBase: {str(e)}")
    st.stop()

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set. Please set it in the environment or .env file.")

#------------------------------------- Streamlit Ui Design
Display=True
st.set_page_config(page_title="Your RAG Assistant", page_icon=":material/smart_toy:",layout="centered")

if Display:
    # Desging App
    st.image("DcouChat_logo.jpg", width=150)
    st.title("AI-Powered Document Assistant")
    st.write("""
                **DocuChat** is a smart PDF-based assistant that allows you to upload a document and ask questions in natural language. It uses Retrieval-Augmented Generation (RAG) powered by LangChain, OpenAI, and Pinecone to provide accurate answers grounded in the document content. Whether it's resumes, reports, or study material, DocuChat helps you interact with complex PDFs in a conversational way.  
            ⚠️ *Note: Currently, DocuChat supports only one PDF at a time, with a limit of 5 pages or 10,000 words. Multi-document and long-format support are planned for future versions.*
            """)
    st.divider()
    
    file = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=False
    )
           
    # Show validation result
    if file:

        # Reset file pointer after validation
        file.seek(0)
        file_content = file.read()

        pdf_hash=get_pdf_hash(file_content)

        if not is_document_already_indexed(pc.Index("rag-index"), pdf_hash):

        # Store PDF validation result
            if file and "pdf_validated" not in st.session_state:
                is_valid, msg, extracted_text = validate_pdf(file_content)
                st.session_state.pdf_validated = is_valid
                st.session_state.pdf_msg = msg
                st.session_state.pdf_text = extracted_text if is_valid else ""

            if st.session_state.pdf_validated:
                st.success("✅ " + st.session_state.pdf_msg)
                
                chunks = process_pdf_and_split(file_content)
                
                if st.checkbox("🔍 View Chunks for Debugging"):
                    for i, c in enumerate(chunks):
                        st.markdown(f"**Chunk {i+1}:**")
                        st.code(c[:500], language="markdown")
                try:
                    
                    vector_store=store_chunks_in_pinecone(chunks=chunks,embedding_function=embedding_function, pdf_hash=pdf_hash)
                    
                    # metadatas = [{"doc_hash": pdf_hash, "chunk_id": i} for i in range(len(chunks))]
                    # vector_store = PineconeVectorStore.from_texts(
                    #     texts=chunks,
                    #     embedding=embedding_function,
                    #     index_name="rag-index",
                    #     metadatas=metadatas,
                    #     pinecone_api_key=PINECONE_API_KEY
                    # )
                    
                    logger.info(f"Stored {len(chunks)} chunks in Pinecone")
                    st.success("✅ Successfully stored embeddings in Pinecone.")
                    store=False
                except Exception as e:
                    st.error(f"❌ Error storing embeddings in Pinecone: {str(e)}")
            else:
                st.error("❌ Error in pdf validation." + st.session_state.pdf_msg)
        else:
            st.success("✅ Document already indexed.")
            

    if file and st.session_state.pdf_validated:
        question = st.text_area("Ask me! (Max 200 characters)", max_chars=200)

        if st.button("Submit", help="Click to get an answer"):
            if not question.strip():
                st.warning("Please enter a question.")
            else:
                with st.spinner("Thinking... Please wait ⏳"):
                    try:
                        answer=query_llm_with_rag(question,vector_store,llm)
                        st.subheader("Answer:")
                        st.write(answer)
                        st.divider()
                    except Exception as e:
                        st.error(f"❌ Error retrieving data from Pinecone: {str(e)}")
                    
    else:
        st.info("Upload a valid PDF to ask questions.")
