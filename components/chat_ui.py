from __future__ import annotations

from html import escape
from urllib.parse import urlparse

import streamlit as st

from services.rag_service import get_rag_response


def _source_domain(url: str) -> str:
    try:
        return urlparse(url).netloc.removeprefix("www.") or "Web kaynağı"
    except ValueError:
        return "Web kaynağı"


def _render_source_drawer() -> None:
    sources = st.session_state.get("research_sources", [])
    label = f"Araştırma kaynakları · {len(sources)}"
    with st.expander(label, expanded=False):
        if not sources:
            st.caption("Bu oturum için görüntülenebilir kaynak bulunamadı.")
            return

        for index, source in enumerate(sources, start=1):
            title = escape(source.get("title") or f"Kaynak {index}")
            url = source.get("url", "")
            domain = escape(_source_domain(url))
            summary = escape((source.get("content") or "")[:180])
            href = escape(url, quote=True)
            link = f'<a href="{href}" target="_blank" rel="noopener noreferrer">Kaynağı aç ↗</a>' if url else ""
            st.markdown(
                f"""
                <article class="source-row">
                    <span>0{index} · {domain}</span>
                    <h4>{title}</h4>
                    <p>{summary}{'…' if len(source.get('content') or '') > 180 else ''}</p>
                    {link}
                </article>
                """,
                unsafe_allow_html=True,
            )


def _restart() -> None:
    for key in (
        "messages",
        "generated_ideas",
        "active_idea",
        "selected_idea",
        "research_sources",
        "theme",
    ):
        st.session_state.pop(key, None)
    st.session_state.messages = []
    st.session_state.step = "theme_selection"
    st.rerun()


def chat_ui() -> None:
    selected = st.session_state.get("selected_idea", "Seçilen fikir")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown(
        f"""
        <section class="chat-heading">
            <p class="eyebrow">IDEA WORKSPACE</p>
            <h1>{escape(selected)}</h1>
            <p>Kaynaklarla konuş, varsayımlarını test et ve fikrini netleştir.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    top_left, top_right = st.columns([4, 1], vertical_alignment="center")
    with top_left:
        _render_source_drawer()
    with top_right:
        if st.button("Yeni fikir", use_container_width=True, key="restart_idea"):
            _restart()

    st.markdown('<div class="conversation-marker"></div>', unsafe_allow_html=True)
    if not st.session_state.messages:
        st.markdown(
            """
            <div class="conversation-empty">
                <span>START HERE</span>
                <p>Bu fikrin hedef kitlesini, uygulanabilirliğini veya benzer çözümlerden nasıl ayrışacağını sorabilirsin.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Fikrinle ilgili bir şey sor…")
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("Kaynaklarda aranıyor…", expanded=False) as status:
            try:
                response = get_rag_response(
                    prompt,
                    st.session_state.session_id,
                    st.session_state.messages[:-1],
                )
                status.update(label="Yanıt hazır", state="complete", expanded=False)
            except Exception:  # noqa: BLE001
                status.update(label="Bağlantı kurulamadı", state="error", expanded=False)
                st.error("Şu anda araştırma servisine erişemiyorum. Biraz sonra tekrar deneyebilirsin.")
                return

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
