"""Editorial Clean Girl / Messy Girl visual theme for IdeApp."""

from __future__ import annotations

import streamlit as st


PALETTES = {
    "clean": {
        "bg": "#f3efe7",
        "ink": "#1d211c",
        "muted": "#686a62",
        "panel": "rgba(255, 253, 247, .78)",
        "line": "rgba(29, 33, 28, .16)",
        "accent": "#b44f36",
        "soft": "#d8dfca",
        "pattern_a": "rgba(81, 94, 72, .10)",
        "pattern_b": "rgba(180, 79, 54, .05)",
    },
    "messy": {
        "bg": "#151318",
        "ink": "#f3eee4",
        "muted": "#aaa2ad",
        "panel": "rgba(28, 24, 31, .80)",
        "line": "rgba(243, 238, 228, .16)",
        "accent": "#d47455",
        "soft": "#5d4a69",
        "pattern_a": "rgba(205, 168, 221, .10)",
        "pattern_b": "rgba(212, 116, 85, .07)",
    },
}


def render_theme_switcher() -> str:
    current = st.session_state.get("theme_mode", "clean")
    st.markdown('<div class="mood-switch-anchor"></div>', unsafe_allow_html=True)
    left, disk, right = st.columns([1, 0.42, 1], vertical_alignment="center")

    with left:
        if st.button(
            "CLEAN",
            type="primary" if current == "clean" else "secondary",
            use_container_width=True,
            key="clean_mode",
        ):
            st.session_state.theme_mode = "clean"
            st.rerun()
    with disk:
        if st.button("◉", key="optical_disk", use_container_width=True, help="Temayı çevir"):
            st.session_state.theme_mode = "messy" if current == "clean" else "clean"
            st.rerun()
    with right:
        if st.button(
            "MESSY",
            type="primary" if current == "messy" else "secondary",
            use_container_width=True,
            key="messy_mode",
        ):
            st.session_state.theme_mode = "messy"
            st.rerun()

    _apply_theme(st.session_state.theme_mode)
    st.markdown(
        f'<p class="mode-caption">{st.session_state.theme_mode.upper()} STATE</p>',
        unsafe_allow_html=True,
    )
    return st.session_state.theme_mode


def _apply_theme(theme: str) -> None:
    p = PALETTES[theme]
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
        :root {{ color-scheme: {'dark' if theme == 'messy' else 'light'}; }}
        .stApp {{
            color: {p['ink']};
            background:
                radial-gradient(circle at 92% 18%, {p['pattern_a']} 0 2px, transparent 3px 100%),
                repeating-radial-gradient(circle at 92% 18%, transparent 0 27px, {p['pattern_a']} 28px 29px),
                linear-gradient(120deg, {p['pattern_b']}, transparent 38%),
                {p['bg']};
            font-family: 'DM Sans', sans-serif;
            transition: background .45s ease, color .35s ease;
        }}
        .block-container {{ max-width: 1080px; padding-top: 1.4rem; padding-bottom: 4rem; }}
        #MainMenu, footer, [data-testid="stHeader"] {{ visibility: hidden; }}
        .ideapp-header {{ display:flex; align-items:center; justify-content:space-between; border-bottom:1px solid {p['line']}; padding:0 0 1rem; margin-bottom:1rem; }}
        .wordmark {{ color:{p['ink']} !important; font-family:'Playfair Display',serif; font-size:1.55rem; font-weight:600; text-decoration:none; }}
        .wordmark span {{ color:{p['accent']}; }}
        .ideapp-header p, .mode-caption {{ color:{p['muted']}; font-size:.69rem; letter-spacing:.18em; text-transform:uppercase; margin:0; }}
        .mood-switch-anchor + div[data-testid="stHorizontalBlock"] {{ max-width:390px; margin:-4.55rem 0 4.5rem auto; position:relative; z-index:5; }}
        .mode-caption {{ display:none; }}
        .hero-copy {{ max-width:790px; margin:0 auto 2.2rem; text-align:center; }}
        .eyebrow {{ color:{p['accent']}; font-size:.72rem; font-weight:600; letter-spacing:.22em; }}
        .hero-copy h1 {{ color:{p['ink']}; font-family:'Playfair Display',serif; font-size:clamp(3rem,7vw,6.4rem); line-height:.91; letter-spacing:-.055em; margin:1.2rem 0; }}
        .hero-copy h1 em {{ color:{p['accent']}; font-weight:600; }}
        .hero-text {{ color:{p['muted']}; max-width:610px; margin:auto; font-size:1.05rem; line-height:1.7; }}
        .ideas-heading {{ max-width:760px; margin:1.5rem 0 3rem; }}
        .ideas-heading h1 {{ color:{p['ink']}; font-family:'Playfair Display',serif; font-size:clamp(3rem,6vw,5.4rem); line-height:.94; letter-spacing:-.05em; margin:.8rem 0 1rem; }}
        .ideas-heading h1 em {{ color:{p['accent']}; font-weight:600; }}
        .ideas-heading > p:last-child {{ color:{p['muted']}; max-width:560px; line-height:1.65; }}
        div[data-testid="stButton"] button {{ border-radius:999px; border:1px solid {p['line']}; letter-spacing:.12em; font-size:.68rem; min-height:2.35rem; }}
        div[data-testid="stButton"] button[kind="primary"] {{ background:{p['ink']}; color:{p['bg']}; }}
        div[data-testid="stButton"]:has(button[title="Temayı çevir"]) button {{
            aspect-ratio:1; min-height:42px; border-radius:50%; font-size:1.3rem; color:{p['ink']};
            background:repeating-conic-gradient({p['ink']} 0 10deg, {p['soft']} 10deg 20deg);
            animation:ideapp-spin 14s linear infinite; box-shadow:0 0 0 5px {p['bg']}, 0 0 0 6px {p['line']};
        }}
        [data-testid="stForm"] {{ max-width:700px; margin:0 auto; padding:0; }}
        [data-testid="stTextInput"] {{ margin:0; }}
        [data-testid="stTextInput"] input {{ background:{p['panel']}; color:{p['ink']}; border:1px solid {p['line']}; border-radius:999px; min-height:58px; padding-inline:1.4rem; backdrop-filter:blur(14px); }}
        [data-testid="stFormSubmitButton"] {{ width:190px; margin:-3.2rem .38rem 0 auto; position:relative; z-index:2; }}
        [data-testid="stFormSubmitButton"] button {{ min-height:2.45rem; letter-spacing:.04em; }}
        [data-testid="stVerticalBlock"]:has(.idea-list-marker) div[data-testid="stButton"] button {{
            position:relative; justify-content:flex-start; text-align:left; white-space:pre-wrap;
            min-height:104px; padding:1.25rem 7.5rem 1.25rem 1.7rem; margin:.18rem 0;
            border-radius:2px; background:{p['panel']}; color:{p['ink']};
            font-family:'Playfair Display',serif; font-size:clamp(1.15rem,2.4vw,1.8rem);
            letter-spacing:-.015em; line-height:1.25; overflow:hidden;
        }}
        [data-testid="stVerticalBlock"]:has(.idea-list-marker) div[data-testid="stButton"] button::after {{
            content:''; position:absolute; inset:0 0 0 auto; width:105px; opacity:.82;
            background:repeating-radial-gradient(circle at center, transparent 0 7px, {p['accent']} 8px 9px), {p['soft']};
            transition:width .35s ease, filter .35s ease;
        }}
        [data-testid="stVerticalBlock"]:has(.idea-list-marker) div[data-testid="stButton"] button:hover::after {{ width:130px; filter:contrast(1.18); }}
        [data-testid="stVerticalBlock"]:has(.idea-list-marker) div[data-testid="stButton"] button[kind="primary"] {{ min-height:148px; background:{p['ink']}; color:{p['bg']}; }}
        .idea-detail {{ margin:-.4rem 0 .75rem; padding:1.2rem 1.7rem; border:1px solid {p['line']}; border-top:0; background:{p['panel']}; }}
        .idea-detail span {{ color:{p['accent']}; font-size:.62rem; font-weight:600; letter-spacing:.18em; }}
        .idea-detail p {{ color:{p['muted']}; max-width:700px; line-height:1.65; margin:.55rem 0 0; }}
        .ideas-footer {{ border-top:1px solid {p['line']}; margin-top:2rem; }}
        .chat-heading {{ max-width:820px; margin:1.6rem 0 2.5rem; }}
        .chat-heading h1 {{ color:{p['ink']}; font-family:'Playfair Display',serif; font-size:clamp(2.4rem,5vw,4.7rem); line-height:1; letter-spacing:-.045em; margin:.75rem 0 1rem; }}
        .chat-heading > p:last-child {{ color:{p['muted']}; line-height:1.65; }}
        [data-testid="stExpander"] details summary {{ color:{p['ink']}; font-size:.78rem; letter-spacing:.08em; text-transform:uppercase; }}
        .source-row {{ padding:1rem .25rem 1.2rem; border-bottom:1px solid {p['line']}; }}
        .source-row:last-child {{ border-bottom:0; }}
        .source-row span {{ color:{p['accent']}; font-size:.62rem; font-weight:600; letter-spacing:.14em; text-transform:uppercase; }}
        .source-row h4 {{ color:{p['ink']}; font-family:'Playfair Display',serif; font-size:1.25rem; margin:.35rem 0; }}
        .source-row p {{ color:{p['muted']}; font-size:.88rem; line-height:1.55; margin:.2rem 0 .5rem; }}
        .source-row a {{ color:{p['ink']} !important; font-size:.72rem; font-weight:600; text-decoration:none; }}
        .conversation-marker {{ border-top:1px solid {p['line']}; margin:2rem 0 1.2rem; }}
        .conversation-empty {{ max-width:580px; margin:3.2rem auto; text-align:center; }}
        .conversation-empty span {{ color:{p['accent']}; font-size:.62rem; font-weight:600; letter-spacing:.18em; }}
        .conversation-empty p {{ color:{p['muted']}; line-height:1.7; }}
        [data-testid="stChatMessage"] {{ max-width:820px; padding:1rem 1.15rem; margin:.7rem auto; box-shadow:none; }}
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {{ margin-left:auto; margin-right:0; max-width:72%; background:{p['ink']}; color:{p['bg']}; border-radius:22px 22px 5px 22px; }}
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {{ margin-left:0; max-width:84%; border-radius:22px 22px 22px 5px; }}
        [data-testid="stChatInput"] {{ background:{p['panel']}; border:1px solid {p['line']}; border-radius:999px; backdrop-filter:blur(14px); }}
        [data-testid="stAlert"], [data-testid="stChatMessage"], [data-testid="stExpander"] {{ background:{p['panel']}; color:{p['ink']}; border:1px solid {p['line']}; border-radius:18px; backdrop-filter:blur(14px); }}
        @keyframes ideapp-spin {{ to {{ transform:rotate(360deg); }} }}
        @media (prefers-reduced-motion: reduce) {{ * {{ animation:none !important; transition:none !important; }} }}
        @media (max-width:640px) {{
            .block-container {{ padding-inline:1rem; }}
            .ideapp-header p {{ display:none; }}
            .mood-switch-anchor + div[data-testid="stHorizontalBlock"] {{ max-width:100%; margin:.5rem 0 2.8rem; }}
            [data-testid="stFormSubmitButton"] {{ width:100%; margin:.5rem 0 0; }}
            .hero-copy h1 {{ font-size:3.25rem; }}
            [data-testid="stVerticalBlock"]:has(.idea-list-marker) div[data-testid="stButton"] button {{ padding-right:5.2rem; min-height:92px; }}
            [data-testid="stVerticalBlock"]:has(.idea-list-marker) div[data-testid="stButton"] button::after {{ width:70px; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
