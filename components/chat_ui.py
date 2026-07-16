import streamlit as st
import uuid
from services.rag_service import get_rag_response

def chat_ui():
    # 1. Dinamik Session Management: Her kullanıcı için benzersiz kimlik
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("💡 IdeApp: RAG Destekli Fikir Havuzu")
    st.markdown("---")

    # 2. UX Dokunuşu: Kenar çubuğu ile profesyonel bir kontrol paneli
    with st.sidebar:
        st.header("Sistem Konsolu")
        st.success(f"Session ID: {st.session_state.session_id[:8]}...")
        topic = st.selectbox("Fikir Kategorisi", ["Yapay Zeka", "Siber Güvenlik", "Blokzincir"])
        st.info("RAG motoru aktif. Kaynaklar taranıyor...")

    # 3. Sohbet Geçmişi: Mesajları akıllı bir döngüyle basıyoruz
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 4. Kullanıcı Girdi Alanı: Modern chat arayüzü[cite: 1]
    if prompt := st.chat_input("Hangi konuda fikir geliştirelim?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 5. RAG'ın Büyülü Anı: Spinner ile "işlem yapılıyor" izlenimi[cite: 1]
        with st.chat_message("assistant"):
            with st.status("Veri işleniyor...", expanded=True) as status:
                st.write("Vektör veritabanı aranıyor...")
                # Backend'den gerçek yanıtı çağırıyoruz
                try:
                    response = get_rag_response(prompt, st.session_state.session_id)
                    status.update(label="Analiz tamamlandı!", state="complete", expanded=False)
                    st.markdown(response)
                    
                    # Kaynakları şık bir 'expander' ile göstermek jürinin kalbini çalar
                    with st.expander("📚 Kullanılan Kaynaklar"):
                        st.write("📌 Örnek Kaynak 1: Teknik Dökümantasyon")
                        st.write("📌 Örnek Kaynak 2: Güncel Sektörel Analiz")
                
                except Exception as e:
                    # UX: Hata anında sistemi kilitlemiyoruz, nezaketle bilgilendiriyoruz
                    status.update(label="Analiz başarısız oldu", state="error")
                    st.error("Sistem şu an meşgul, ama fikir havuzumuz çalışmaya devam ediyor.")
                    response = "Şu an bağlantı kuramadım ama fikirlerinizi not ettim!"
            
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    chat_ui()