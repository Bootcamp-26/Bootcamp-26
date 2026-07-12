import sys
import os
import uuid

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from components.chat.chat_ui import chat_ui 

st.set_page_config(page_title="IdeApp - Fikir Havuzu", layout="wide")

def main():
    st.title("💡 IdeApp: RAG Destekli Fikir Havuzu")
    
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    
    chat_ui()

if __name__ == "__main__":
    main()
