# Bloom – AI-Powered Document Chatbot

**Bloom** is a lightweight, local-first AI chatbot that allows users to upload documents (PDF, Word, or text) and query them in natural language. It uses a Retrieval-Augmented Generation (RAG) pipeline to provide real-time, context-aware answers using open-source LLMs (e.g., Mistral via Ollama).

---

##  Features

-  Supports **PDF**, **DOCX**, and **TXT** file uploads  
-  Real-time document analysis with RAG pipeline  
-  Interactive chat interface with chat bubbles  
-  Downloadable chat history  
-  Uses local models (Mistral via Ollama) for privacy  
-  Light/Dark theme toggle  
-  Clean, modular UI with custom styling  

---

##  Tech Stack

| Layer           | Tools/Libraries Used                                                                 |
|----------------|----------------------------------------------------------------------------------------|
| **Frontend**    | [Streamlit](https://streamlit.io/), HTML/CSS for UI components                        |
| **Backend**     | Python, [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/)        |
| **Document Parsing** | PyPDF2, python-docx, standard text I/O                                      |
| **Embeddings**  | [HuggingFace Sentence Transformers (MiniLM)](https://huggingface.co/sentence-transformers) |
| **Vector Store**| [FAISS](https://github.com/facebookresearch/faiss)                                   |

---

## How to Run Locally

###  Prerequisites

- Python 3.9+  
- [Ollama](https://ollama.com/) installed with the `mistral` model:
  ```bash
  ollama run mistral
  ```

* pip packages from `requirements.txt`

---

### Installation & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/RiyyanKharal/Document-Chatbot.git
   cd Document-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## Folder Structure

```
querybloom-chatbot/
├── app.py
├── core/
│   ├── document_loader.py
│   ├── vector_store.py
│   └── llm_chain.py
├── ui/
│   ├── styling.py
│   └── components.py
└── README.md
```

---

## To-Do / Enhancements

* [ ] Persistent session memory  
* [ ] Multi-document support    
* [ ] Support additional LLM backends (e.g., DeepSeek, LLaMA)  

---

> 🌸 Built with love and open-source tools to bloom your documents into answers!
