import streamlit as st
from services.rag_service import get_rag_response
from services.llm_service import generate_chat_title

def chat_ui():
    # 1. Oturum yapısının başlatılması
    if "chat_sessions" not in st.session_state or not st.session_state.chat_sessions:
        import uuid
        idea_session_id = st.session_state.get("idea_session_id") or str(uuid.uuid4())
        selected = st.session_state.get("selected_idea", "RAG Destekli Fikir Havuzu")
        chat_session_id = str(uuid.uuid4())
        welcome_message = {
            "role": "assistant",
            "content": f"Merhaba! **{selected}** fikrinizi geliştirmek için gerekli araştırmaları tamamladım ve bilgi tabanını hazırladım. Projenin iş modeli, hedef kitlesi, teknik altyapısı veya pazarlama stratejisi gibi konuları birlikte tartışıp geliştirebiliriz. Merak ettiğiniz soruları sormaya başlayabilirsiniz!"
        }
        st.session_state.chat_sessions = {
            chat_session_id: {
                "title": "Yeni Sohbet",
                "messages": [welcome_message],
                "idea_session_id": idea_session_id,
                "selected_idea": selected
            }
        }
        st.session_state.current_chat_session_id = chat_session_id

    # 2. Sidebar navigasyonu ve yeni sohbet oluşturma
    with st.sidebar:
        st.markdown("### ⚙️ İşlemler")
        if st.button("➕ Yeni Sohbet Başlat", use_container_width=True):
            import uuid
            new_chat_id = str(uuid.uuid4())
            selected = st.session_state.get("selected_idea", "RAG Destekli Fikir Havuzu")
            idea_session_id = st.session_state.get("idea_session_id")
            welcome_message = {
                "role": "assistant",
                "content": f"Merhaba! **{selected}** fikrinizi geliştirmek için gerekli araştırmaları tamamladım ve bilgi tabanını hazırladım. Projenin iş modeli, hedef kitlesi, teknik altyapısı veya pazarlama stratejisi gibi konuları birlikte tartışıp geliştirebiliriz. Merak ettiğiniz soruları sormaya başlayabilirsiniz!"
            }
            st.session_state.chat_sessions[new_chat_id] = {
                "title": "Yeni Sohbet",
                "messages": [welcome_message],
                "idea_session_id": idea_session_id,
                "selected_idea": selected
            }
            st.session_state.current_chat_session_id = new_chat_id
            st.rerun()

        st.markdown("---")
        st.markdown("### 💬 Sohbet Geçmişi")
        
        for session_id, session_data in list(st.session_state.chat_sessions.items()):
            title = session_data.get("title", "Yeni Sohbet")
            is_active = (session_id == st.session_state.current_chat_session_id)
            btn_label = f"👉 {title}" if is_active else title
            
            if st.button(btn_label, key=f"session_btn_{session_id}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.current_chat_session_id = session_id
                st.rerun()
                
        st.markdown("---")
        if st.button("🔄 Başka Fikir Seç / Geri Dön", use_container_width=True):
            st.session_state.pop("chat_sessions", None)
            st.session_state.pop("current_chat_session_id", None)
            st.session_state.pop("selected_idea", None)
            st.session_state.pop("idea_session_id", None)
            st.session_state.step = "idea_selection"
            st.rerun()

    # 3. Aktif sohbet oturumunun yüklenmesi
    active_session_id = st.session_state.current_chat_session_id
    session_data = st.session_state.chat_sessions[active_session_id]
    messages = session_data["messages"]
    idea_session_id = session_data["idea_session_id"]
    selected_idea = session_data["selected_idea"]

    # Sayfa başlığı
    st.markdown(f"## 💡 IdeApp: {selected_idea}")
    st.markdown("---")

    # Mesaj geçmişini listele
    for msg in messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Kullanıcı girdisi ve LLM yanıtı
    if prompt := st.chat_input("Hangi konuda fikir geliştirelim?"):
        # Kullanıcı mesajını geçmişe ekle
        messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # İlk kullanıcı mesajı gönderildiğinde başlığı özetleyip güncelle
        # (Messages listesinde [0] hoş geldin asistan mesajıdır, [1] ise ilk kullanıcı mesajıdır)
        if len(messages) == 2:
            with st.spinner("Sohbet başlığı özetleniyor..."):
                try:
                    summary_title = generate_chat_title(prompt)
                    session_data["title"] = summary_title
                except Exception:
                    pass

        with st.chat_message("assistant"):
            # RAG pipeline canlı gösterge
            with st.status("Veri işleniyor...", expanded=True) as status:
                st.write("Vektör veritabanı taranıyor...")
                try:
                    history = messages[:-1]
                    response = get_rag_response(prompt, idea_session_id, history)
                    status.update(label="Analiz tamamlandı!", state="complete", expanded=False)
                except Exception as e:
                    status.update(label="Bir aksilik oldu", state="error")
                    st.error("Sistem şu an meşgul, ama fikir havuzumuz çalışmaya devam ediyor.")
                    response = "Şu an bağlantı kuramadım ama fikirlerinizi not ettim."
            
            st.markdown(response)
            
            # Kaynakları göster
            from services.rag_service import retrieve_documents
            sources = retrieve_documents(prompt, idea_session_id)
            with st.expander("📚 Kullanılan Kaynaklar"):
                if sources:
                    for idx, src in enumerate(sources):
                        title = src.get("title") or f"Kaynak #{idx+1}"
                        url = src.get("url")
                        if url:
                            st.markdown(f"📌 [{title}]({url})")
                        else:
                            st.markdown(f"📌 {title}")
                else:
                    st.write("Bu soru için veritabanında özel bir referans bulunamadı.")
            
            # Asistan mesajını geçmişe ekle ve sayfayı yenile
            messages.append({"role": "assistant", "content": response})
            st.rerun()