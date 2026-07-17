from __future__ import annotations

import re
from html import escape

import streamlit as st

from services.llm_service import generate_ideas
from services.rag_service import save_documents
from services.search_service import search_sources


def _idea_parts(raw: str) -> tuple[str, str]:
    """Turn the LLM's numbered line into an editorial title and summary."""
    cleaned = re.sub(r"^\s*\d+[.)-]?\s*", "", raw).strip()
    for separator in (" — ", " – ", " - ", ": "):
        if separator in cleaned:
            title, description = cleaned.split(separator, 1)
            return title.strip(), description.strip()
    return cleaned, "Bu fikri seçerek kaynaklarını araştırabilir ve ayrıntılandırabilirsin."


def _reset_to_theme() -> None:
    st.session_state.pop("generated_ideas", None)
    st.session_state.pop("active_idea", None)
    st.session_state.step = "theme_selection"
    st.rerun()


def _open_idea(idea: str) -> None:
    st.session_state.active_idea = idea


def _start_research(selected: str) -> None:
    st.session_state.selected_idea = selected
    with st.spinner("Kaynaklar taranıyor, çalışma alanın hazırlanıyor..."):
        try:
            results = search_sources(selected)
            documents = [item for item in results if item.get("content")]
            st.session_state.research_sources = results
            if documents:
                save_documents(documents, st.session_state.session_id)
            st.session_state.step = "chat"
            st.rerun()
        except Exception as exc:  # noqa: BLE001
            st.error(f"Kaynaklar hazırlanırken bir hata oluştu: {exc}")


def idea_picker() -> None:
    st.markdown(
        f"""
        <section class="ideas-heading">
            <p class="eyebrow">CURATED FOR · {st.session_state.theme.upper()}</p>
            <h1>Üç farklı<br><em>başlangıç.</em></h1>
            <p>Bir fikri aç, yaklaşımını incele ve sana en yakın olanı geliştir.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    if "generated_ideas" not in st.session_state:
        with st.spinner("Yapay zekâ fikirleri kürate ediyor..."):
            try:
                st.session_state.generated_ideas = generate_ideas(st.session_state.theme, n=3)
            except Exception:  # noqa: BLE001
                st.error("Fikirler şu anda üretilemedi. Lütfen tekrar deneyin.")
                if st.button("Tema ekranına dön"):
                    _reset_to_theme()
                return

    ideas = st.session_state.generated_ideas
    if not ideas:
        st.warning("Fikir üretilemedi. Temayı değiştirerek tekrar deneyebilirsin.")
        if st.button("Tema ekranına dön"):
            _reset_to_theme()
        return

    active = st.session_state.get("active_idea")
    st.markdown('<div class="idea-list-marker"></div>', unsafe_allow_html=True)

    for index, idea in enumerate(ideas, start=1):
        title, description = _idea_parts(idea)
        is_active = active == idea
        label = f"0{index}   {title}\n\n{description}" if is_active else f"0{index}   {title}"

        if st.button(
            label,
            key=f"idea_card_{index}",
            type="primary" if is_active else "secondary",
            use_container_width=True,
            on_click=_open_idea,
            args=(idea,),
        ):
            pass

        if is_active:
            st.markdown(
                f"""
                <div class="idea-detail">
                    <span>EDITOR'S NOTE</span>
                    <p>{escape(description)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(
                "Bu fikri araştır  →",
                key=f"research_{index}",
                type="primary",
                use_container_width=True,
            ):
                _start_research(idea)

    st.markdown('<div class="ideas-footer"></div>', unsafe_allow_html=True)
    if st.button("← Temayı değiştir", key="back_to_theme"):
        _reset_to_theme()
