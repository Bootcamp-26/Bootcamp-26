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
    # En üstte karşılama şeridi ve Kullanıcı Menüsü
    col_welcome, col_pop = st.columns([3.2, 1])
    with col_welcome:
        st.markdown(f"### 👋 Merhaba, {st.session_state.username}!")
    with col_pop:
        with st.popover("👤 Hesabım", use_container_width=True):
            st.markdown(f"**Aktif Kullanıcı:** `{st.session_state.username}`")
            st.divider()
            if st.button("🚪 Çıkış Yap", use_container_width=True):
                st.session_state.username = ""
                st.session_state.step = "login"
                st.session_state.pop("chat_sessions", None)
                st.session_state.pop("current_chat_session_id", None)
                st.session_state.pop("selected_idea", None)
                st.session_state.pop("idea_session_id", None)
                st.rerun()

    # Altında status_bar gösterelim
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
    if "custom_idea_input" not in st.session_state:
        st.session_state.custom_idea_input = ""

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
                # Kart seçildiğinde, metin alanını da bu kartın temizlenmiş içeriği ile güncelle
                text = idea.strip()
                if text[:2].rstrip(".").isdigit():
                    text = text.split(".", 1)[-1].strip()
                st.session_state.custom_idea_input = text
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # Başka öner butonu (Fikir kartlarının hemen altında)
    st.write("")
    _, col_suggest, _ = st.columns([1.2, 1, 1.2])
    with col_suggest:
        if st.button("🔄 Başka Fikir Öner", use_container_width=True):
            st.session_state.pop("generated_ideas", None)
            st.session_state.idea_selected_index = None
            st.session_state.custom_idea_input = ""
            st.rerun()

    st.write("")
    st.markdown("##### ✍️ Veya Kendi Fikrini Yaz / Düzenle")
    st.caption("Yukarıdaki önerilerden birini seçip üzerinde değişiklik yapabilir ya da tamamen yeni bir fikir yazabilirsin:")
    
    custom_idea = st.text_area(
        "Fikir İçeriği",
        value=st.session_state.custom_idea_input,
        placeholder="Örn: Yapay zeka destekli, öğrencilerin ödevlerini analiz eden mobil uygulama...",
        label_visibility="collapsed",
        key="custom_idea_input"
    )

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Geri Dön (Tema Değiştir)", use_container_width=True):
            st.session_state.pop("generated_ideas", None)
            st.session_state.idea_selected_index = None
            st.session_state.pop("custom_idea_input", None)
            st.session_state.step = "theme_selection"
            st.rerun()

    with col2:
        develop_disabled = not custom_idea.strip()
        if st.button("Bu Fikri Geliştir →", type="primary", use_container_width=True, disabled=develop_disabled):
            selected = custom_idea.strip()
            st.session_state.selected_idea = selected
            
            import uuid
            idea_session_id = str(uuid.uuid4())
            st.session_state.idea_session_id = idea_session_id

            with st.spinner("Kaynaklar araştırılıyor ve bilgi tabanı hazırlanıyor..."):
                try:
                    results = search_sources(selected)
                    documents = [item for item in results if item.get("content")]
                    if documents:
                        save_documents(documents, idea_session_id)
                    
                    # Yeni fikir için ilk sohbet oturumunu oluşturalım
                    chat_session_id = str(uuid.uuid4())
                    welcome_message = {
                        "role": "assistant",
                        "content": f"Merhaba! **{selected}** fikrinizi geliştirmek için gerekli araştırmaları tamamladım ve bilgi tabanını hazırladım. Projenin iş modeli, hedef kitlesi, teknik altyapısı veya pazarlama stratejisi gibi konuları birlikte tartışıp geliştirebiliriz. Merak ettiğiniz soruları sormaya başlayabilirsiniz!"
                    }
                    
                    # Kullanıcının mevcut diğer eski sohbetlerini koruyarak yeni sohbeti ekleyelim
                    from services.storage_service import load_user_chats, save_user_chats
                    current_sessions = load_user_chats(st.session_state.username)
                    current_sessions[chat_session_id] = {
                        "title": "Yeni Sohbet",
                        "messages": [welcome_message],
                        "idea_session_id": idea_session_id,
                        "selected_idea": selected
                    }
                    
                    st.session_state.chat_sessions = current_sessions
                    st.session_state.current_chat_session_id = chat_session_id
                    save_user_chats(st.session_state.username, st.session_state.chat_sessions)
                    
                    st.session_state.step = "chat"
                    st.session_state.idea_selected_index = None
                    st.rerun()
                except Exception as e:
                    st.error(f"Kaynaklar toplanırken bir hata oluştu: {e}")
