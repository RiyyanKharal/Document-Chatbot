# ================= ui/styling.py =================
import streamlit as st

def load_custom_styles(theme="light"):
    """
    Loads custom CSS styles for light or dark mode.
    Args:
        theme (str): "light" or "dark"
    """
    if theme == "dark":
        bg_color = "#1e1e2f"
        user_bubble = "#3e3e5e"
        bot_bubble = "#5e5e7e"
        text_color = "#f5f5fa"
        sidebar_bg = "#2b2b3d"
        title_color = "#dba6f4"
        subtitle_color = "#a988d2"
    else:
        bg_color = "#fff0f5"
        user_bubble = "#fddde6"
        bot_bubble = "#e6d6f3"
        text_color = "#2a003f"
        sidebar_bg = "#f8e6f8"
        title_color = "#d48ec7"
        subtitle_color = "#aa6faa"

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Quicksand', sans-serif;
            background-color: {bg_color};
            color: {text_color};
        }}

        .stApp {{
            background-color: {bg_color};
        }}

        .stFileUploader, .stTextInput, .stChatInputContainer {{
            background-color: #fde7f3;
            border-radius: 10px;
        }}

        .stButton>button {{
            background-color: #eecff5;
            color: #4a1942;
            border-radius: 10px;
        }}

        .stAlert-success {{
            background-color: #e6ffe6;
            border-left: 6px solid #b2fab4;
        }}

        .stAlert-error {{
            background-color: #ffe6ea;
            border-left: 6px solid #ffb3c6;
        }}

        .title-text {{
            font-family: 'Pacifico', cursive;
            font-size: 3em;
            color: {title_color};
            text-align: center;
            margin-bottom: 0.5em;
        }}

        .subtitle-text {{
            font-size: 1.2em;
            color: {subtitle_color};
            text-align: center;
            margin-bottom: 2em;
        }}

        .chat-bubble-user {{
            background-color: {user_bubble};
            color: #4a1942;
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            max-width: 80%;
            align-self: flex-end;
            animation: fadeIn 0.5s ease-in-out;
        }}

        .chat-bubble-bot {{
            background-color: {bot_bubble};
            color: {text_color};
            padding: 10px 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            max-width: 80%;
            align-self: flex-start;
            animation: fadeIn 0.5s ease-in-out;
        }}

        .chat-container {{
            display: flex;
            flex-direction: column;
        }}

        section[data-testid="stSidebar"] {{
            background-color: {sidebar_bg};
            padding: 1rem;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        </style>
    """, unsafe_allow_html=True)


def display_title():
    """Displays app title and subtitle."""
    st.markdown("""
        <div class="title-text"> Bloom </div>
        <div class="subtitle-text">Bringing your documents to life. </div>
    """, unsafe_allow_html=True)


def display_chat_bubble(sender, msg):
    """Renders chat bubble for user or bot."""
    bubble_class = "chat-bubble-user" if sender == "User" else "chat-bubble-bot"
    st.markdown(f'<div class="{bubble_class}">{msg}</div>', unsafe_allow_html=True)


def clear_conversation():
    """Clears all relevant conversation state keys."""
    for key in ["chat_history", "user_input", "stored_file", "vectorstore"]:
        if key in st.session_state:
            del st.session_state[key]
