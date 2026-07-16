import streamlit as st
from services.rag_service import get_rag_response

def chat_ui():
    st.markdown("### 💬 IdeApp: RAG Destekli Fikir Havuzu")
    
    # Sohbet geçmişini koruyan o kutsal durum yönetimi
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mesajları şık bir döngüyle ekrana basıyoruz
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Kullanıcıdan girişi al
    if prompt := st.chat_input("Hangi konuda fikir geliştirelim?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # RAG'ın çalıştığı o büyülü an
        with st.chat_message("assistant"):
            with st.spinner("İnternet tarıyor, zihinler açılıyor..."):
                try:
                    # Backend'deki RAG servisini çağırıyoruz
                    response = get_rag_response(prompt)
                    st.markdown(response)
                except Exception as e:
                    st.error("Bir aksilik oldu, ama olsun! Sistem kendini güncelliyor.")
                    response = "Şu an bağlantı kuramadık ama fikirlerinizi not ettim."
        
        st.session_state.messages.append({"role": "assistant", "content": response})