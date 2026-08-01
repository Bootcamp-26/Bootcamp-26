import streamlit as st
from services.rag_service import get_rag_response
from services.llm_service import generate_chat_title

def chat_ui():
    # 1. Oturum yapısının başlatılması ve diskten yüklenmesi
    if "chat_sessions" not in st.session_state or not st.session_state.chat_sessions:
        from services.storage_service import load_user_chats, save_user_chats
        loaded_sessions = load_user_chats(st.session_state.username)
        if loaded_sessions:
            st.session_state.chat_sessions = loaded_sessions
            st.session_state.current_chat_session_id = list(loaded_sessions.keys())[0]
        else:
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
            save_user_chats(st.session_state.username, st.session_state.chat_sessions)

    # 2. Sidebar navigasyonu ve yeni sohbet oluşturma
    with st.sidebar:
        st.markdown("### ⚙️ İşlemler")
        if st.button("➕ Yeni Sohbet Başlat", use_container_width=True):
            # Eğer şu an aktif olan sohbet boşsa (yalnızca hoşgeldin mesajı içeriyorsa), yeni oluşturmaya gerek yok
            active_id = st.session_state.current_chat_session_id
            active_msg_count = len(st.session_state.chat_sessions.get(active_id, {}).get("messages", []))
            
            if active_msg_count <= 1:
                st.rerun()
                
            # Değilse yeni oluştur:
            import uuid
            new_chat_id = str(uuid.uuid4())
            selected = st.session_state.get("selected_idea", "RAG Destekli Fikir Havuzu")
            idea_session_id = st.session_state.get("idea_session_id")
            welcome_message = {
                "role": "assistant",
                "content": f"Merhaba! **{selected}** fikrinizi geliştirmek için gerekli araştırmaları tamamladım ve bilgi tabanını hazırladım. Projenin iş modeli, hedef kitlesi, teknik altyapısı veya pazarlama stratejisi gibi konuları birlikte tartışıp geliştirebiliriz. Merak ettiğiniz soruları sormaya başlayabilirsiniz!"
            }
            
            # Diğer tüm boş sohbetleri (aktif olan hariç) temizleyelim
            to_remove = [sid for sid, sdata in st.session_state.chat_sessions.items() if len(sdata.get("messages", [])) <= 1]
            for sid in to_remove:
                st.session_state.chat_sessions.pop(sid, None)
                
            st.session_state.chat_sessions[new_chat_id] = {
                "title": "Yeni Sohbet",
                "messages": [welcome_message],
                "idea_session_id": idea_session_id,
                "selected_idea": selected
            }
            st.session_state.current_chat_session_id = new_chat_id
            
            from services.storage_service import save_user_chats
            save_user_chats(st.session_state.username, st.session_state.chat_sessions)
            st.rerun()

        st.markdown("---")
        st.markdown("### 💬 Sohbet Geçmişi")
        
        for session_id, session_data in list(st.session_state.chat_sessions.items()):
            title = session_data.get("title", "Yeni Sohbet")
            is_active = (session_id == st.session_state.current_chat_session_id)
            btn_label = f"👉 {title}" if is_active else title
            
            col_sel, col_del = st.columns([5, 1])
            with col_sel:
                if st.button(btn_label, key=f"session_btn_{session_id}", use_container_width=True, type="primary" if is_active else "secondary"):
                    # Eğer tıklandığında eski aktif sohbet boşsa, onu kaldıralım
                    current_id = st.session_state.current_chat_session_id
                    if current_id != session_id and len(st.session_state.chat_sessions[current_id]["messages"]) <= 1:
                        st.session_state.chat_sessions.pop(current_id, None)
                        
                    st.session_state.current_chat_session_id = session_id
                    st.rerun()
            with col_del:
                if st.button("🗑️", key=f"del_btn_{session_id}", use_container_width=True, help="Bu sohbeti sil"):
                    st.session_state.chat_sessions.pop(session_id, None)
                    from services.storage_service import save_user_chats
                    save_user_chats(st.session_state.username, st.session_state.chat_sessions)
                    
                    if session_id == st.session_state.current_chat_session_id:
                        remaining_keys = list(st.session_state.chat_sessions.keys())
                        if remaining_keys:
                            st.session_state.current_chat_session_id = remaining_keys[0]
                        else:
                            st.session_state.pop("chat_sessions", None)
                            st.session_state.pop("current_chat_session_id", None)
                    st.rerun()
                
        st.markdown("---")
        if st.button("🔄 Başka Fikir Seç / Geri Dön", use_container_width=True):
            st.session_state.pop("chat_sessions", None)
            st.session_state.pop("current_chat_session_id", None)
            st.session_state.pop("selected_idea", None)
            st.session_state.pop("idea_session_id", None)
            st.session_state.step = "theme_selection"
            st.rerun()

        st.markdown("---")
        st.markdown(f"👤 Kullanıcı: `{st.session_state.username}`")
        if st.button("🚪 Çıkış Yap", use_container_width=True):
            st.session_state.username = ""
            st.session_state.step = "login"
            st.session_state.pop("chat_sessions", None)
            st.session_state.pop("current_chat_session_id", None)
            st.session_state.pop("selected_idea", None)
            st.session_state.pop("idea_session_id", None)
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
        from services.storage_service import save_user_chats
        save_user_chats(st.session_state.username, st.session_state.chat_sessions)
        
        with st.chat_message("user"):
            st.markdown(prompt)

        # İlk kullanıcı mesajı gönderildiğinde başlığı özetleyip güncelle
        if len(messages) == 2:
            with st.spinner("Sohbet başlığı özetleniyor..."):
                try:
                    summary_title = generate_chat_title(prompt)
                    session_data["title"] = summary_title
                    save_user_chats(st.session_state.username, st.session_state.chat_sessions)
                except Exception:
                    pass

        with st.chat_message("assistant"):
            # RAG pipeline canlı gösterge
            with st.status("Veri işleniyor...", expanded=True) as status:
                st.write("Vektör veritabanı taranıyor...")
                try:
                    history = messages[:-1]
                    response = get_rag_response(prompt, idea_session_id, history, selected_idea)
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
            save_user_chats(st.session_state.username, st.session_state.chat_sessions)
            st.rerun()