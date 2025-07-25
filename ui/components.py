# In ui/components.py

import streamlit as st
from io import BytesIO
from fpdf import FPDF

def sidebar_chat_controls():
    st.markdown("## 💾 Download Chat")

    # Convert chat history to plain text
    if "chat_history" in st.session_state and st.session_state.chat_history:
        chat_text = "\n\n".join([f"{msg['sender']}: {msg['message']}" for msg in st.session_state.chat_history])
        
        # Download as TXT
        st.download_button(
            label="📄 Download TXT",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )

        # Download as PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in chat_text.split('\n'):
            pdf.multi_cell(0, 10, line)
        pdf_buffer = BytesIO()
        pdf.output(pdf_buffer)
        pdf_buffer.seek(0)

        st.download_button(
            label="🧾 Download PDF",
            data=pdf_buffer,
            file_name="chat_history.pdf",
            mime="application/pdf"
        )

    else:
        st.info("Chat log will appear here once you chat.")

    # Clear conversation button
    if st.button("🗑️ Clear Chat"):
        for key in ["chat_history", "user_input", "stored_file", "vectorstore"]:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()
