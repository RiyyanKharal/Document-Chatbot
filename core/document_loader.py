# ================= core/document_loader.py =================
import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

def load_document(file, debug=False):
    """
    Saves uploaded file temporarily and loads it using appropriate LangChain loader.
    Supported: PDF, TXT, DOCX.
    """
    ext = os.path.splitext(file.name)[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    if debug:
        print(f"[DEBUG] Loading file: {file.name} (ext: {ext}) -> {tmp_path}")

    if ext == ".pdf":
        loader = PyPDFLoader(tmp_path)
    elif ext == ".txt":
        loader = TextLoader(tmp_path)
    elif ext == ".docx":
        loader = Docx2txtLoader(tmp_path)
    else:
        return None

    return loader.load()
