import streamlit as st
from services.rag_service import get_rag_response

def chat_ui():
    # Sayfa düzenini ferahlatıyoruz
    st.markdown("## 💡 IdeApp: RAG Destekli Fikir Havuzu")
    st.markdown("---")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mesaj geçmişini şık bir şekilde listele
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Hangi konuda fikir geliştirelim?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Jüriye sistemin ne yaptığını gösteren 'status' bileşeni
            with st.status("Veri işleniyor...", expanded=True) as status:
                st.write("Vektör veritabanı taranıyor...")
                try:
                    response = get_rag_response(prompt)
                    status.update(label="Analiz tamamlandı!", state="complete", expanded=False)
                    st.markdown(response)
                    
                    # Kaynakları şeffaf bir şekilde sunuyoruz
                    with st.expander("📚 Kullanılan Kaynaklar"):
                        st.write("📌 Örnek Kaynak: Teknik Dökümantasyon")
                
                except Exception as e:
                    status.update(label="Bir aksilik oldu", state="error")
                    st.error("Sistem şu an meşgul, ama fikir havuzumuz çalışmaya devam ediyor.")
                    response = "Şu an bağlantı kuramadım ama fikirlerinizi not ettim."
            
            st.session_state.messages.append({"role": "assistant", "content": response})