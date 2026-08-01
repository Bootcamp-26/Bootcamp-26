import streamlit as st
import sys
import os
import uuid

# Sistemin modülleri bulması için root dizinini ekliyoruz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from components.chat_ui import chat_ui
from components.theme_picker import theme_picker
from components.idea_picker import idea_picker

st.set_page_config(page_title="IdeApp - Fikir Havuzu", layout="wide", initial_sidebar_state="collapsed")

def login_screen():
    from components.theme.photon_theme import inject_photon_theme
    inject_photon_theme()
    
    _, col_center, _ = st.columns([1, 1.2, 1])
    with col_center:
        st.markdown(
            """
            <div style="text-align: center; margin-top: 80px;" class="photon-fade-up">
                <h1 style="font-size: 2.8rem; margin-bottom: 5px;">IdeApp</h1>
                <p style="color: #8fa3b8; font-size: 1.1rem; margin-bottom: 30px;">
                    RAG Destekli Yaratıcı Fikir Havuzuna Hoş Geldiniz
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Şık kullanıcı adı girişi
        st.markdown("<p style='font-size: 0.95rem; margin-bottom: 8px;'>Kullanıcı Adı</p>", unsafe_allow_html=True)
        username = st.text_input(
            "Kullanıcı Adı",
            placeholder="Lütfen kullanıcı adınızı girin...",
            label_visibility="collapsed"
        ).strip()
        
        st.write("")
        if st.button("✨ Giriş Yap", type="primary", use_container_width=True):
            if username:
                st.session_state.username = username
                st.session_state.step = "theme_selection"
                st.rerun()
            else:
                st.warning("Lütfen geçerli bir kullanıcı adı girin.")

def main():
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    if "step" not in st.session_state:
        st.session_state.step = "login"
    if "username" not in st.session_state:
        st.session_state.username = ""

    if st.session_state.step == "login":
        login_screen()
    elif st.session_state.step == "theme_selection":
        theme_picker()
    elif st.session_state.step == "idea_selection":
        idea_picker()
    elif st.session_state.step == "chat":
        chat_ui()

if __name__ == "__main__":
    main()