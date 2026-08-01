import streamlit as st
import random

from components.theme.photon_theme import inject_photon_theme, status_bar, holographic_divider

ALL_TOPICS = [
    ("🧠", "Yapay Zeka destekli eğitim"),
    ("🌱", "Sürdürülebilirlik ve iklim"),
    ("💊", "Dijital sağlık"),
    ("🎮", "Oyunlaştırılmış öğrenme"),
    ("💸", "Finansal teknolojiler"),
    ("🏙️", "Akıllı şehir çözümleri"),
    ("🎨", "Yaratıcı içerik araçları"),
    ("🔐", "Siber güvenlik"),
    ("🚀", "Uzay teknolojileri"),
    ("🌾", "Akıllı tarım ve gıda"),
    ("📦", "Otonom lojistik"),
    ("⚡", "Temiz enerji sistemleri"),
    ("🕶️", "Sanal ve artırılmış gerçeklik"),
    ("🐾", "Evcil hayvan teknolojileri"),
    ("👵", "Yaşlı bakım ve destek"),
    ("🏠", "Akıllı ev ve IoT"),
    ("🌊", "Deniz ve su teknolojileri"),
    ("♿", "Engelsiz yaşam çözümleri"),
    ("🛠️", "Mikro-üretim ve 3D"),
    ("🧬", "Biyoteknoloji ve genetik"),
    ("🚲", "Mikro-mobilite çözümleri"),
    ("🎬", "Yeni nesil eğlence"),
    ("📚", "Açık kaynak eğitim"),
    ("👔", "Uzaktan çalışma araçları"),
]


def _hero() -> None:
    col_text, col_visual = st.columns([1.15, 1], gap="large")

    with col_text:
        st.markdown(
            """
            <div class="photon-fade-up">
                <h1 style="font-size:3rem; line-height:1.05; margin-bottom:0;">
                    BUILD YOUR<br>
                    <span class="photon-glow-text">CREATIVE IDEAS</span>
                </h1>
                <p style="color:#8fa3b8; font-size:1.02rem; max-width:520px; margin-top:18px;">
                    RAG destekli yapay zeka çekirdeği ile bir tema seç, saniyeler içinde
                    özgün proje fikirleri üret ve seçtiğin fikri sohbet ederek derinleştir.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_visual:
        st.markdown(
            """
            <div class="photon-fade-up" style="display:flex; justify-content:center; padding-top:8px;">
                <svg viewBox="0 0 300 300" width="240" height="240">
                    <defs>
                        <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
                            <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.85"/>
                            <stop offset="60%" stop-color="#0891b2" stop-opacity="0.22"/>
                            <stop offset="100%" stop-color="#0891b2" stop-opacity="0"/>
                        </radialGradient>
                    </defs>
                    <circle cx="150" cy="150" r="95" fill="url(#coreGlow)"/>
                    <circle cx="150" cy="150" r="112" fill="none" stroke="#06b6d4" stroke-opacity="0.45" stroke-width="1" stroke-dasharray="3 9"/>
                    <circle cx="150" cy="150" r="90" fill="none" stroke="#67e8f9" stroke-opacity="0.5" stroke-width="1"/>
                    <circle cx="150" cy="150" r="34" fill="#030712" stroke="#22d3ee" stroke-width="1.5"/>
                    <circle cx="150" cy="150" r="5" fill="#22d3ee" class="photon-node"/>
                    <circle cx="150" cy="38" r="3" fill="#22d3ee" class="photon-node"/>
                    <circle cx="262" cy="150" r="3" fill="#22d3ee" class="photon-node"/>
                    <circle cx="150" cy="262" r="3" fill="#22d3ee" class="photon-node"/>
                    <circle cx="38" cy="150" r="3" fill="#22d3ee" class="photon-node"/>
                </svg>
            </div>
            """,
            unsafe_allow_html=True,
        )


def theme_picker() -> None:
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
    status_bar(st.session_state.get("session_id", ""), module="IDEA-ENGINE")

    _hero()
    holographic_divider()

    st.markdown("#### 🎯 Tema Seçimi")
    st.caption("HANGİ ALANDA BİR PROJE GELİŞTİRMEK İSTİYORSUN?")

    if "theme_text_input" not in st.session_state:
        st.session_state.theme_text_input = ""
    if "current_topics" not in st.session_state:
        st.session_state.current_topics = ALL_TOPICS[:8]

    # ---- Hızlı seçim çipleri (grid) ----
    cols = st.columns(4)
    for i, (emoji, label) in enumerate(st.session_state.current_topics):
        with cols[i % 4]:
            if st.button(f"{emoji} {label}", key=f"quick_{i}", use_container_width=True):
                st.session_state.theme_text_input = label

    # Başka öner butonu
    st.write("")
    _, col_suggest, _ = st.columns([1.2, 1, 1.2])
    with col_suggest:
        if st.button("🔄 Başka Öner", use_container_width=True):
            remaining = [t for t in ALL_TOPICS if t not in st.session_state.current_topics]
            st.session_state.current_topics = random.sample(remaining, 8)
            st.rerun()

    st.write("")
    theme = st.text_input(
        "Tema",
        value=st.session_state.theme_text_input,
        placeholder="Örn: Yapay Zeka destekli eğitim...",
        label_visibility="collapsed",
        key="theme_text_input",
    )

    st.write("")
    _, col_btn, _ = st.columns([1, 1.1, 1])
    with col_btn:
        if st.button("✨  FİKİR BUL", type="primary", use_container_width=True):
            if theme.strip():
                st.session_state.theme = theme
                st.session_state.step = "idea_selection"
                st.session_state.pop("generated_ideas", None)
                st.rerun()
            else:
                st.warning("Lütfen bir tema giriniz veya yukarıdan hızlı seçim yap.")

        # Eski sohbetleri yükle ve buton göster
        from services.storage_service import load_user_chats
        user_chats = load_user_chats(st.session_state.username)
        if user_chats:
            st.write("")
            if st.button("📚 Eski Sohbetlerim", use_container_width=True):
                st.session_state.chat_sessions = user_chats
                st.session_state.current_chat_session_id = list(user_chats.keys())[0]
                st.session_state.step = "chat"
                st.rerun()
