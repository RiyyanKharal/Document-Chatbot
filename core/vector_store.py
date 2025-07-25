# ================= core/vector_store.py =================
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def process_and_index_documents(
    docs,
    chunk_size=500,
    chunk_overlap=100,
    model_name="all-MiniLM-L6-v2",
    debug=False
):
    """
    Splits documents into chunks, embeds them, and returns a FAISS vector store.
    
    Args:
        docs: List of LangChain Documents
        chunk_size: Size of each chunk in characters
        chunk_overlap: Overlap between chunks in characters
        model_name: HuggingFace embedding model to use
        debug: If True, prints debug info
    
    Returns:
        FAISS vector store
    """
    # 1. Split documents into overlapping chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(docs)
    
    if debug:
        print(f"[DEBUG] Split into {len(chunks)} chunks using chunk_size={chunk_size}, overlap={chunk_overlap}")

    # 2. Create embeddings for chunks
    embed_model = HuggingFaceEmbeddings(model_name=model_name)

    if debug:
        print(f"[DEBUG] Using embedding model: {model_name}")

    # 3. Build and return FAISS vector store
    return FAISS.from_documents(chunks, embed_model)
