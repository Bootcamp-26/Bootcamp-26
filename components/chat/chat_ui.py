"""
components/chat/chat_ui.py
Streamlit tabanlı sohbet arayüzü.

- st.chat_message  -> mesaj balonları (user/assistant)
- st.status        -> RAG pipeline çalışırken canlı ilerleme göstergesi
- st.expander      -> her cevabın altında kaynak şeffaflığı (skor barlı)

NOT: adapter.run_query tek seferde retrieval+generation'ı bitirip döner
(gerçek streaming yok). st.status içindeki adımlar bu nedenle "gerçek zamanlı
event" değil, kullanıcıya süreci anlatan bir UX simülasyonudur. Gerçek
adım-adım streaming isterseniz adapter'ın generator/callback tabanlı bir
versiyonu gerekir — ayrı bir görev olarak ele alınmalı.
"""

from __future__ import annotations

import asyncio

import streamlit as st

from components.theme import render_theme_toggle
from schemas.response import QueryRequest
from services import adapter


def _run_async(coro):
    """Streamlit senkron çalışır; adapter.run_query async — köprü burada."""
    return asyncio.run(coro)


def _init_session_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []  # UI'da gösterilen mesaj geçmişi
    if "session_id" not in st.session_state:
        st.session_state.session_id = None


def _render_sources(sources: list[dict]) -> None:
    if not sources:
        return
    with st.expander(f"📎 Kaynaklar ({len(sources)})"):
        for i, src in enumerate(sources, start=1):
            st.markdown(f"**Kaynak {i}** — `{src['doc_id']}`")
            st.progress(src["score"], text=f"Güven skoru: {src['score']:.0%}")
            preview = src["chunk_text"][:300]
            if len(src["chunk_text"]) > 300:
                preview += "..."
            st.caption(preview)
            st.divider()


def render_chat_ui() -> None:
    """Ana giriş noktası — streamlit_app.py bunu çağırır."""
    _init_session_state()

    with st.sidebar:
        render_theme_toggle()
        st.divider()
        if st.button("🗑️ Sohbeti Temizle", use_container_width=True):
            st.session_state.messages = []
            st.session_state.session_id = None
            st.rerun()

    # Geçmiş mesajları render et
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant":
                _render_sources(msg.get("sources", []))

    prompt = st.chat_input("Bir fikir sorun veya sohbete devam edin...")
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        status_box = st.status("Kaynaklar taranıyor...", expanded=True)
        response = None
        try:
            with status_box:
                st.write("🔍 İlgili dokümanlar aranıyor...")
                request = QueryRequest(query=prompt, session_id=st.session_state.session_id)
                response = _run_async(adapter.run_query(request))
                st.write(
                    f"✅ {len(response.sources)} kaynak bulundu "
                    f"(ort. skor: {response.retrieval_score_avg:.0%})"
                )
                st.write("🧠 Cevap oluşturuluyor...")
            status_box.update(label="Tamamlandı", state="complete", expanded=False)
        except Exception as exc:  # noqa: BLE001
            status_box.update(label="Hata oluştu", state="error")
            st.error(f"Bir şeyler ters gitti: {exc}")
            return  # history'ye yazılmaz — bilinçli tercih (bkz. adapter notları)

        st.session_state.session_id = response.session_id
        sources_dump = [s.model_dump() for s in response.sources]

        st.markdown(response.answer)
        _render_sources(sources_dump)
        st.caption(
            f"⏱️ {response.latency_ms:.0f}ms · 🔢 {response.tokens_used} token · "
            f"🧵 {response.history_length}/20 mesaj hafızada"
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": response.answer, "sources": sources_dump}
        )