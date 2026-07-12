import sys
import os
import uuid

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from components.chat_ui import chat_ui 
from components.theme_picker import theme_picker
from components.idea_picker import idea_picker 

st.set_page_config(page_title="IdeApp - Fikir Havuzu", layout="wide")

def main():
    st.title("💡 IdeApp: RAG Destekli Fikir Havuzu")
    
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
        
    if "step" not in st.session_state:
        st.session_state.step = "theme_selection"
        
    if st.session_state.step == "theme_selection":
        theme_picker()
    elif st.session_state.step == "idea_selection":
        idea_picker()
    elif st.session_state.step == "chat":
        chat_ui()

if __name__ == "__main__":
    main()
