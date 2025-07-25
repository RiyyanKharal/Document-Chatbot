import streamlit as st
import time
from core.document_loader import load_document
from core.vector_store import process_and_index_documents
from core.llm_chain import get_qa_chain
from ui.styling import load_custom_styles, display_title, display_chat_bubble

# --- Setup ---
st.set_page_config(page_title="Bloom – AI Document Chatbot", page_icon="🌸", layout="wide")

# --- Sidebar: Theme + Download/Clear ---
with st.sidebar:
    theme = st.radio("🌗 Choose Theme", ["light", "dark"], index=0)
    load_custom_styles(theme=theme)

    # Download button for chat log (always visible, disabled if no history)
    chat_log_str = ""
    download_disabled = True

    if "chat_history" in st.session_state and st.session_state.chat_history:
        chat_log_str = "\n".join([f"{sender}: {msg}" for sender, msg in st.session_state.chat_history])
        download_disabled = False

    st.download_button(
        "💾 Download Chat",
        data=chat_log_str,
        file_name="chat_log.txt",
        mime="text/plain",
        disabled=download_disabled
    )

    # Optional message if no chat yet
    if download_disabled:
        st.caption("Start chatting to enable download.")

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# --- Title ---
display_title()

# --- Session State Initialization ---
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- File Upload ---
uploaded_file = st.file_uploader("📄 Upload a document", type=["pdf", "txt", "docx"])

# --- Document Processing ---
if uploaded_file and st.session_state.vector_store is None:
    docs = load_document(uploaded_file)
    if docs:
        st.session_state.vector_store = process_and_index_documents(docs)
        st.success("✅ Document processed and indexed!")
    else:
        st.error("❌ Unsupported file type.")

# --- Chat Interface ---
st.subheader("💬 Chat with your Document")
query = st.chat_input("Ask a question about the document...")

if query and st.session_state.vector_store is not None:
    qa_chain = get_qa_chain(st.session_state.vector_store)
    with st.spinner("BloomBot is thinking..."):
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            '<div class="chat-bubble-bot">💬 BloomBot is typing...</div>',
            unsafe_allow_html=True
        )
        time.sleep(1.2)
        response = qa_chain.run(query)
        typing_placeholder.empty()

    # Save to chat history
    st.session_state.chat_history.append(("User", query))
    st.session_state.chat_history.append(("Bot", response))

# --- Display Chat History ---
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, msg in st.session_state.chat_history:
    display_chat_bubble(sender, msg)
st.markdown('</div>', unsafe_allow_html=True)
