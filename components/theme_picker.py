import streamlit as st

def theme_picker():
    with st.form("idea_prompt", clear_on_submit=False, border=False):
        theme = st.text_input(
            "Fikir alanı",
            placeholder="Bugün neyin üzerine düşünmek istiyorsun?",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button(
            "Fikirleri keşfet  →",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        if theme.strip():
            st.session_state.theme = theme
            st.session_state.step = "idea_selection"
            st.rerun()
        else:
            st.warning("Lütfen bir tema giriniz.")
