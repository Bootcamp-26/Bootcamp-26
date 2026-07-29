"""
components/theme/photon_theme.py
PHOTON AI — sci-fi / cyber-lab görsel kimliği.

Bu modül Streamlit'in native bileşenlerini (st.button, st.text_input,
st.chat_message, st.spinner, st.radio, st.expander, vb.) değiştirmeden,
sadece CSS enjeksiyonu (unsafe_allow_html) ile yeniden derilendirir.
Böylece backend mantığı (services/*) hiç dokunulmadan kalır; sadece
görsel katman PHOTON AI diline çevrilir.

Kullanım: her sayfa fonksiyonunun en başında inject_photon_theme() çağrılır.
Streamlit her adımda scripti baştan çalıştırdığı için (rerun modeli) bu
çağrı ucuzdur ve idempotenttir.
"""

from __future__ import annotations

import streamlit as st

# ---------------------------------------------------------------------------
# Renk tokenleri
# ---------------------------------------------------------------------------
BG_DEEP = "#030712"
BG_PANEL = "#0b0f19"
CYAN = "#06b6d4"
CYAN_BRIGHT = "#22d3ee"
BLUE_HOLO = "#3b82f6"
TEXT_PRIMARY = "#e2f4f7"
TEXT_DIM = "#7d8ba1"


def inject_photon_theme() -> None:
    """Sayfanın tamamına PHOTON AI CSS kimliğini uygular."""
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', system-ui, sans-serif;
        }}

        /* ---------- Arka plan: derin uzay + izgara doku ---------- */
        .stApp {{
            background-color: {BG_DEEP};
            background-image:
                radial-gradient(circle at 12% 8%, rgba(6,182,212,0.10), transparent 42%),
                radial-gradient(circle at 88% 22%, rgba(59,130,246,0.09), transparent 46%),
                linear-gradient(rgba(6,182,212,0.045) 1px, transparent 1px),
                linear-gradient(90deg, rgba(6,182,212,0.045) 1px, transparent 1px);
            background-size: auto, auto, 44px 44px, 44px 44px;
            color: {TEXT_PRIMARY};
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, rgba(11,15,25,0.97), rgba(3,7,18,0.99));
            border-right: 1px solid rgba(6,182,212,0.18);
        }}

        /* ---------- Başlıklar ---------- */
        h1, h2, h3 {{
            font-family: 'Outfit', sans-serif !important;
            color: #ffffff !important;
            letter-spacing: 0.01em;
        }}
        h1 {{
            text-shadow: 0 0 8px rgba(34,211,238,0.55), 0 0 30px rgba(6,182,212,0.30);
        }}

        p, span, label, .stMarkdown {{
            color: {TEXT_PRIMARY};
        }}

        /* ---------- Metin girişleri ---------- */
        .stTextInput input, .stTextArea textarea {{
            background: rgba(11,15,25,0.85) !important;
            border: 1px solid rgba(6,182,212,0.35) !important;
            border-radius: 12px !important;
            color: {TEXT_PRIMARY} !important;
            font-size: 15px !important;
            padding: 12px 14px !important;
            transition: border-color .2s ease, box-shadow .2s ease;
        }}
        .stTextInput input:focus, .stTextArea textarea:focus {{
            border-color: {CYAN_BRIGHT} !important;
            box-shadow: 0 0 0 1px {CYAN_BRIGHT}55, 0 0 18px rgba(6,182,212,0.35) !important;
        }}
        .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
            color: {TEXT_DIM} !important;
        }}

        /* ---------- Butonlar ---------- */
        .stButton > button {{
            background: rgba(6,182,212,0.10) !important;
            border: 1px solid rgba(34,211,238,0.55) !important;
            color: {CYAN_BRIGHT} !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em;
            padding: 0.55rem 1.1rem !important;
            transition: transform .18s ease, box-shadow .18s ease, background .18s ease !important;
            box-shadow: 0 0 10px rgba(6,182,212,0.12);
        }}
        .stButton > button:hover {{
            background: rgba(6,182,212,0.22) !important;
            transform: translateY(-2px) scale(1.01);
            box-shadow: 0 0 14px rgba(34,211,238,0.55), 0 0 34px rgba(6,182,212,0.30) !important;
        }}
        .stButton > button:active {{
            transform: translateY(0) scale(0.98);
        }}
        .stButton > button:disabled {{
            opacity: 0.35 !important;
            box-shadow: none !important;
        }}
        /* primary tip -> "seçili" kart efekti (idea_picker seçiminde kullanılır) */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, rgba(6,182,212,0.30), rgba(59,130,246,0.22)) !important;
            border: 1px solid {CYAN_BRIGHT} !important;
            color: #ffffff !important;
            box-shadow: 0 0 0 1px {CYAN_BRIGHT}66, 0 0 22px rgba(34,211,238,0.45) !important;
        }}

        /* ---------- Radio / seçenekler ---------- */
        .stRadio [role="radiogroup"] label {{
            background: rgba(11,15,25,0.7);
            border: 1px solid rgba(6,182,212,0.25);
            border-radius: 12px;
            padding: 10px 14px;
            margin-bottom: 8px;
            transition: border-color .18s ease, box-shadow .18s ease;
        }}
        .stRadio [role="radiogroup"] label:hover {{
            border-color: {CYAN_BRIGHT};
            box-shadow: 0 0 12px rgba(6,182,212,0.25);
        }}

        /* ---------- Kart / konteyner (glassmorphism) ---------- */
        .photon-panel {{
            background: linear-gradient(160deg, rgba(11,15,25,0.85), rgba(3,7,18,0.85));
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(6,182,212,0.28);
            border-radius: 18px;
            padding: 20px 22px;
        }}
        .photon-chip {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(6,182,212,0.08);
            border: 1px solid rgba(6,182,212,0.30);
            border-radius: 999px;
            padding: 5px 13px;
            font-family: 'Space Mono', monospace;
            font-size: 11px;
            letter-spacing: 0.06em;
            color: {CYAN_BRIGHT};
        }}
        .photon-glow-text {{
            color: {CYAN_BRIGHT};
            text-shadow: 0 0 6px rgba(34,211,238,0.55), 0 0 22px rgba(6,182,212,0.30);
        }}

        /* ---------- Sohbet balonları ---------- */
        [data-testid="stChatMessage"] {{
            background: rgba(11,15,25,0.75) !important;
            border: 1px solid rgba(6,182,212,0.22) !important;
            border-radius: 16px !important;
            backdrop-filter: blur(10px);
            padding: 4px 6px;
        }}
        [data-testid="stChatMessageAvatarUser"] {{
            background: rgba(6,182,212,0.25) !important;
        }}
        [data-testid="stChatMessageAvatarAssistant"] {{
            background: rgba(59,130,246,0.25) !important;
        }}
        [data-testid="stChatInput"] textarea {{
            background: rgba(11,15,25,0.9) !important;
            border: 1px solid rgba(6,182,212,0.40) !important;
            color: {TEXT_PRIMARY} !important;
            border-radius: 14px !important;
        }}
        [data-testid="stChatInput"] {{
            border-top: 1px solid rgba(6,182,212,0.18);
        }}
        [data-testid="stChatInput"] button {{
            background: {CYAN} !important;
            border-radius: 10px !important;
        }}

        /* ---------- Spinner / status ---------- */
        .stSpinner > div {{
            border-top-color: {CYAN_BRIGHT} !important;
            filter: drop-shadow(0 0 6px rgba(34,211,238,0.6));
        }}
        [data-testid="stStatusWidget"] {{
            background: rgba(11,15,25,0.85) !important;
            border: 1px solid rgba(6,182,212,0.30) !important;
            border-radius: 14px !important;
        }}
        .stProgress > div > div {{
            background-color: {CYAN_BRIGHT} !important;
            box-shadow: 0 0 10px rgba(34,211,238,0.6);
        }}

        /* ---------- Expander (kaynaklar) ---------- */
        .streamlit-expanderHeader, [data-testid="stExpander"] {{
            background: rgba(11,15,25,0.7) !important;
            border: 1px solid rgba(6,182,212,0.22) !important;
            border-radius: 12px !important;
            color: {TEXT_PRIMARY} !important;
        }}

        /* ---------- Info / warning / error kutuları ---------- */
        [data-testid="stAlert"] {{
            background: rgba(11,15,25,0.8) !important;
            border: 1px solid rgba(6,182,212,0.30) !important;
            border-radius: 12px !important;
        }}

        /* ---------- Taramalı üst çizgi (ambient scan) ---------- */
        .photon-scanline {{
            position: fixed;
            top: 0; left: 0; right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, {CYAN_BRIGHT}bb, transparent);
            animation: photon-scan 3.6s linear infinite;
            z-index: 999999;
            pointer-events: none;
        }}
        @keyframes photon-scan {{
            0%   {{ transform: translateY(0);    opacity: 0; }}
            8%   {{ opacity: .8; }}
            92%  {{ opacity: .8; }}
            100% {{ transform: translateY(100vh); opacity: 0; }}
        }}

        @keyframes photon-pulse {{
            0%, 100% {{ opacity: .4; transform: scale(1); }}
            50%      {{ opacity: 1;  transform: scale(1.3); }}
        }}
        .photon-node {{
            animation: photon-pulse 2.2s ease-in-out infinite;
        }}

        @keyframes photon-fade-up {{
            from {{ opacity: 0; transform: translateY(14px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}
        .photon-fade-up {{ animation: photon-fade-up .5s cubic-bezier(.16,.84,.44,1) both; }}

        ::selection {{ background: rgba(6,182,212,0.35); color: #fff; }}
        </style>
        <div class="photon-scanline"></div>
        """,
        unsafe_allow_html=True,
    )


def status_bar(session_id: str, module: str = "RAG-CORE v2.3") -> None:
    """Üst bilgi şeridi: sistem durumu / modül / oturum kimliği (sci-fi detay)."""
    short_id = (session_id or "—")[:8]
    st.markdown(
        f"""
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:26px;">
            <span class="photon-chip">🟢 SİSTEM: ÇEVRİMİÇİ</span>
            <span class="photon-chip">🧠 MODÜL: {module}</span>
            <span class="photon-chip">🆔 OTURUM: {short_id}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def holographic_divider() -> None:
    st.markdown(
        """
        <div style="height:1px; margin:22px 0;
             background:linear-gradient(90deg, transparent, rgba(6,182,212,0.55), transparent);">
        </div>
        """,
        unsafe_allow_html=True,
    )
