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
