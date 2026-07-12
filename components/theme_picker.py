import streamlit as st

def theme_picker():
    st.markdown("### 🎯 Tema Seçimi")
    theme = st.text_input("Hangi alanda bir proje geliştirmek istiyorsunuz?", placeholder="Örn: Yapay Zeka destekli eğitim...")
    
    if st.button("Fikir Üret"):
        if theme.strip():
            st.session_state.theme = theme
            st.session_state.step = "idea_selection"
            st.rerun()
        else:
            st.warning("Lütfen bir tema giriniz.")
