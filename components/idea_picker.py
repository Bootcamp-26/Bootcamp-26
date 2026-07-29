import streamlit as st

from services.llm_service import generate_ideas
from services.search_service import search_sources
from services.rag_service import save_documents
from components.theme.photon_theme import inject_photon_theme, status_bar, holographic_divider

IDEA_COUNT = 4  # "4 fikirden istediğini seç" akışı için


def _loading_view() -> None:
    st.markdown(
        """
        <div class="photon-fade-up" style="text-align:center; padding: 30px 0 10px;">
            <div style="font-family:'Space Mono',monospace; color:#22d3ee; font-size:13px; letter-spacing:.08em;">
                🧠 YAPAY ZEKA FİKİRLER ÜRETİYOR...
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.spinner("RAG-CORE fikir üretim modülü çalışıyor, lütfen bekleyin..."):
        try:
            ideas = generate_ideas(st.session_state.theme, n=IDEA_COUNT)
            st.session_state.generated_ideas = ideas
        except Exception:
            st.session_state.generated_ideas = []
            st.error("Fikir üretilirken bir hata oluştu.")


def _idea_card_label(idea: str, index: int) -> str:
    # LLM çıktısı genelde "1. Başlık - açıklama" formatında geliyor.
    # Kart üstünde sade görünmesi için baştaki numarayı temizliyoruz.
    text = idea.strip()
    if text[:2].rstrip(".").isdigit():
        text = text.split(".", 1)[-1].strip()
    return f"💡  {text}"


def idea_picker() -> None:
    inject_photon_theme()
    status_bar(st.session_state.get("session_id", ""), module="RAG-CORE v2.3")

    st.markdown("#### 💡 Fikir Havuzu")
    st.markdown(
        f'<span class="photon-chip">🎯 TEMA: {st.session_state.theme}</span>',
        unsafe_allow_html=True,
    )
    holographic_divider()

    if "generated_ideas" not in st.session_state:
        _loading_view()

    ideas = st.session_state.get("generated_ideas", [])

    if not ideas:
        st.warning("Hiç fikir üretilemedi. Lütfen geri dönüp temayı değiştirin.")
        if st.button("← Geri Dön (Tema Değiştir)"):
            st.session_state.pop("generated_ideas", None)
            st.session_state.step = "theme_selection"
            st.rerun()
        return

    st.markdown("###### Senin için üretilen fikirlerden birini seç:")

    if "idea_selected_index" not in st.session_state:
        st.session_state.idea_selected_index = None

    # ---- 2x2 fikir kartı grid'i ----
    cols = st.columns(2)
    for i, idea in enumerate(ideas):
        is_selected = st.session_state.idea_selected_index == i
        with cols[i % 2]:
            st.markdown('<div class="photon-fade-up">', unsafe_allow_html=True)
            if st.button(
                _idea_card_label(idea, i),
                key=f"idea_card_{i}",
                type="primary" if is_selected else "secondary",
                use_container_width=True,
            ):
                st.session_state.idea_selected_index = i
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Geri Dön (Tema Değiştir)", use_container_width=True):
            st.session_state.pop("generated_ideas", None)
            st.session_state.idea_selected_index = None
            st.session_state.step = "theme_selection"
            st.rerun()

    with col2:
        develop_disabled = st.session_state.idea_selected_index is None
        if st.button("Bu Fikri Geliştir →", type="primary", use_container_width=True, disabled=develop_disabled):
            selected = ideas[st.session_state.idea_selected_index]
            st.session_state.selected_idea = selected

            with st.spinner("Kaynaklar araştırılıyor ve bilgi tabanı hazırlanıyor..."):
                try:
                    results = search_sources(selected)
                    documents = [item for item in results if item.get("content")]
                    if documents:
                        save_documents(documents, st.session_state.session_id)
                    st.session_state.step = "chat"
                    st.session_state.idea_selected_index = None
                    st.rerun()
                except Exception as e:
                    st.error(f"Kaynaklar toplanırken bir hata oluştu: {e}")
