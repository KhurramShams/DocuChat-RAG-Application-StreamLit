<!-- ------------------------------------------------------------------- -->
<!--    DocuChat – README                                                -->
<!-- ------------------------------------------------------------------- -->

<h1 align="center">DocuChat 🔍💬</h1>
<h4 align="center">The AI‑powered way to read, search, and chat with your PDFs</h4>

<p align="center">
  <a href="https://docuchat-live.streamlit.app/" target="_blank"><img alt="Open in Streamlit" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"></a>
  <a href="https://github.com/your‑username/DocuChat/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <a href="https://github.com/your‑username/DocuChat/actions"><img alt="CI status" src="https://github.com/your‑username/DocuChat/actions/workflows/ci.yml/badge.svg"></a>
</p>

---

## ✨ What is DocuChat?

**DocuChat** is a Retrieval‑Augmented Generation (RAG) chatbot that turns any short PDF ( ≤ 5 pages ) into a live Q&A assistant.  
Upload a document, ask anything, and DocuChat responds with grounded, citation‑worthy answers—no manual skimming required.

|                      |                                                                               |
|----------------------|-------------------------------------------------------------------------------|
| **Typical uses**     | Résumé review, policy documents, research papers, lab protocols, meeting notes |
| **Tech stack**       | Streamlit · LangChain · OpenAI · Pinecone · PyMuPDF                            |
| **Live demo**        | [docuchat-live.streamlit.app](https://docuchat-live.streamlit.app/)                      |
| **Status**           | **Beta v0.5** – feedback welcome 🙌                                           |

---

## 🚀 Key Features

| Feature | Details |
|---------|---------|
| 📥 **Drag‑and‑Drop PDFs** | Accepts one PDF up to 5 pages / 10 k words for fast indexing |
| 🔎 **Semantic Chunking & Search** | Uses LangChain + Pinecone to embed 500‑token chunks with overlap, ensuring query‑time recall |
| 💬 **GPT‑4o‑mini Answers** | Combines retrieved context with OpenAI’s GPT‑4o‑mini for accurate, concise responses |
| 🔄 **Duplicate Detection** | SHA‑256 hash prevents re‑indexing of the same document |
| 🖥 **Zero‑Install Front‑End** | Pure Streamlit interface—runs locally or on Streamlit Cloud |
| 📝 **Extensible RAG Prompt** | Self‑contained prompt template in `pdf_utils.py` for easy tweaking |

---

## ⚙️ Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/your‑username/DocuChat.git
cd DocuChat
pip install -r requirements.txt

Here’s a complete **Quick Start** section formatted in one clean Markdown structure. You can directly paste this into your `README.md` **after the Key Features** section:

---

## ⚙️ Quick Start

### 🧑‍💻 1. Clone the Repository

```bash
git clone https://github.com/your-username/DocuChat.git
cd DocuChat
```

### 📦 2. Install Dependencies

Make sure you have **Python 3.10+** installed, then run:

```bash
pip install -r requirements.txt
```

### 🔐 3. Set Up API Keys

#### ➤ For Local Development:

Create a file at `.streamlit/secrets.toml` with the following content:

```toml
[openai]
openapi_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

[pinecone]
pineconeapi_key = "pcd-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
pinecone_environment = "us-east-1"  # Use your Pinecone project’s region

[index]
index_name = "docuchat-index"
```

#### ➤ For Streamlit Cloud Deployment:

1. Deploy the repo via [streamlit.io/cloud](https://streamlit.io/cloud).
2. Go to **App settings → Secrets**.
3. Add the same key-value pairs from the `.streamlit/secrets.toml` file above.

---

### 🚀 4. Run the Application

Start your RAG-powered chatbot locally:

```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

---

### ☁️ 5. Optional – Deploy on Streamlit Cloud

1. Push this repo to your GitHub account.
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud) and click **"New App"**.
3. Select your GitHub repo and branch, then click **Deploy**.
4. Add your API keys under **Settings → Secrets** as shown above.
5. Your live RAG chatbot is ready to use!

---

### 🧪 How to Use

* Upload a short PDF (maximum 5 pages).
* Ask natural language questions based on its content.
* Get accurate, context-aware answers powered by LangChain + OpenAI.
* Use the **debug checkbox** to inspect text chunks if needed.



