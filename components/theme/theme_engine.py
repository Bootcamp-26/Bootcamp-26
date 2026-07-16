"""
components/theme/theme_engine.py
'Clean Girl' (aydınlık) vs 'Messy Girl' (karanlık) tema motoru.

Arkaplan: dış bir stok görsel servisine (ör. depositphotos) bağımlı DEĞİL —
saf CSS `repeating-conic-gradient` ile üretilen optik illüzyon deseni
(spiral/halka görünümü). Bu tercih bilinçli:
  - Telif/lisans riski yok (hiçbir dış görsel indirilmiyor).
  - Network bağımlılığı yok -> anında render, ek gecikme yok.
  - Renk paletini tema ile birebir eşleştirebiliyoruz (stok görselde mümkün değil).
"""

from __future__ import annotations

import streamlit as st

_CLEAN_BG = "repeating-conic-gradient(from 0deg, #fdfdfd 0deg 8deg, #ececec 8deg 16deg)"
_MESSY_BG = "repeating-conic-gradient(from 0deg, #0a0a0a 0deg 8deg, #1f1f1f 8deg 16deg)"


def render_theme_toggle() -> str:
    """
    Sidebar'da tema toggle'ı gösterir ve seçili temayı uygular.
    Dönüş: "clean" | "messy" (chat_ui.py veya başka bir component
    tema bilgisine ihtiyaç duyarsa kullanabilir).
    """
    is_messy = st.toggle(
        "🌙 Messy Girl",
        value=False,
        help="Kapalı: Clean Girl (aydınlık) · Açık: Messy Girl (karanlık)",
    )
    theme = "messy" if is_messy else "clean"
    _apply_theme(theme)
    return theme


def _apply_theme(theme: str) -> None:
    is_messy = theme == "messy"
    bg_pattern = _MESSY_BG if is_messy else _CLEAN_BG
    text_color = "#f5f5f5" if is_messy else "#111111"
    card_bg = "rgba(20,20,20,0.85)" if is_messy else "rgba(255,255,255,0.88)"
    accent = "#c9a3ff" if is_messy else "#7c5cff"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: {bg_pattern};
            background-size: 42px 42px;
            background-attachment: fixed;
            color: {text_color};
        }}
        [data-testid="stChatMessage"] {{
            background: {card_bg};
            border-radius: 14px;
            backdrop-filter: blur(6px);
        }}
        [data-testid="stSidebar"] {{
            background: {card_bg};
        }}
        .stProgress > div > div {{
            background-color: {accent};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )