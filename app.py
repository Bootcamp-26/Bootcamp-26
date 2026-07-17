import uuid

import streamlit as st

from components.chat_ui import chat_ui
from components.idea_picker import idea_picker
from components.theme import render_theme_switcher
from components.theme_picker import theme_picker


st.set_page_config(
    page_title="IdeApp — Fikrini görünür kıl",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def _init_state() -> None:
    defaults = {
        "step": "theme_selection",
        "session_id": str(uuid.uuid4()),
        "messages": [],
        "theme_mode": "clean",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _render_header() -> None:
    st.markdown(
        """
        <header class="ideapp-header">
            <a class="wordmark" href="#">IdeApp<span>•</span></a>
            <p>AI-powered idea studio</p>
        </header>
        """,
        unsafe_allow_html=True,
    )


def _render_intro() -> None:
    st.markdown(
        """
        <section class="hero-copy">
            <p class="eyebrow">ONE IDEA · TWO CREATIVE STATES</p>
            <h1>Choose your<br><em>creative state.</em></h1>
            <p class="hero-text">
                Aklındaki konuyu yaz. IdeApp olasılıkları araştırıp
                geliştirebileceğin fikirleri önüne getirsin.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    _init_state()
    _render_header()
    render_theme_switcher()

    step = st.session_state.step
    if step == "theme_selection":
        _render_intro()
        theme_picker()
    elif step == "idea_selection":
        idea_picker()
    elif step == "chat":
        chat_ui()
    else:
        st.session_state.step = "theme_selection"
        st.rerun()


if __name__ == "__main__":
    main()
