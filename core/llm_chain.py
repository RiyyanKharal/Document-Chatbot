# ================= core/llm_chain.py =================
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

_llm_instance = None

def get_llm(model_name="mistral"):
    """
    Returns a singleton instance of the Ollama LLM with the given model.
    Default is 'mistral'.
    """
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = Ollama(model=model_name)
    return _llm_instance

def get_qa_chain(vector_store):
    """
    Builds a RetrievalQA chain with the current vector store and LLM.
    """
    retriever = vector_store.as_retriever()
    llm = get_llm()

    # Basic Retrieval QA Chain (no memory)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # --- Conversational Chain ---
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
