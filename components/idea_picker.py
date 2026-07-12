import streamlit as st
from services.llm_service import generate_ideas

def idea_picker():
    st.markdown("### 💡 Fikir Seçimi")
    st.info(f"Seçilen Tema: **{st.session_state.theme}**")
    
    if "generated_ideas" not in st.session_state:
        with st.spinner("Yapay zeka fikirler üretiyor, lütfen bekleyin..."):
            try:
                ideas = generate_ideas(st.session_state.theme, n=3)
                st.session_state.generated_ideas = ideas
            except Exception as e:
                st.error("Fikir üretilirken bir hata oluştu.")
                return
                
    ideas = st.session_state.generated_ideas
    
    if not ideas:
        st.warning("Hiç fikir üretilemedi. Lütfen geri dönüp temayı değiştirin.")
        if st.button("Geri Dön (Tema Değiştir)"):
            del st.session_state.generated_ideas
            st.session_state.step = "theme_selection"
            st.rerun()
        return

    selected = st.radio("Aşağıdaki fikirlerden birini seçin:", ideas)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Geri Dön (Tema Değiştir)"):
            del st.session_state.generated_ideas
            st.session_state.step = "theme_selection"
            st.rerun()
            
    with col2:
        if st.button("Bu Fikri Geliştir"):
            st.session_state.selected_idea = selected
            st.session_state.step = "chat"
            st.rerun()
