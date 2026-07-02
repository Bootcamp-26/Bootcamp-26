# IdeApp — Yapay Zeka Destekli Fikir Geliştirme Asistanı

> Fikir üretmekte zorlanıyor musun? IdeApp, seni temadan fikre, fikirden derin araştırmaya taşır.

---

## Takım Bilgileri

**Takım İsmi:** Grup-318

| Üye | Rol |
|-----|-----|
| Zeynep Temiz | Product Owner |
| Burak Ilgın | Scrum Master |
| İlkay Cangüder | Developer |
| Asel Yılmaz | Developer |
| Bengisu Küpeli| Developer |

---

## Ürün Bilgileri

**Ürün İsmi:** IdeApp

**Ürün Açıklaması:**
IdeApp, fikir üretmekte zorlanan kullanıcılara yapay zeka ve internet tabanlı veri toplama ile kişiselleştirilmiş bir fikir geliştirme ortamı sunar. Kullanıcı bir tema seçer, AI bu temaya uygun fikir önerileri sunar, sistem seçilen fikre ilişkin internet kaynaklarını otomatik olarak toplayarak bir RAG (Retrieval-Augmented Generation) bilgi ortamı oluşturur. Kullanıcı bu ortam içinde fikriyle ilgili sorularını serbestçe sorarak fikrini derinleştirebilir ve geliştirebilir — hiçbir kaynak yüklemesi gerekmez.

**Ürün Özellikleri:**
- 🎯 AI destekli tema ve fikir önerisi (Ollama / Gemma 3:4b)
- 🔍 Web arama ajanı ile otomatik kaynak toplama (Tavily API)
- 🧠 Oturum bazlı RAG pipeline (ChromaDB + nomic-embed-text)
- 💬 Bağlamdan çıkmadan sürekli sohbet modu (Llama 3.1:8b)
- ⚡ Kullanıcıdan kaynak yüklemesi gerektirmeyen sıfır-sürtünme deneyimi

**Hedef Kitle:**
- Girişim veya proje fikri arayan bireyler
- Araştırmaya başlamak isteyen öğrenciler ve akademisyenler
- İçerik üreticiler ve yaratıcı profesyoneller
- Yeni alanlara girmek isteyen meraklı kullanıcılar

**Teknoloji Yığını:**

| Katman | Teknoloji |
|--------|-----------|
| Arayüz (UI) | Streamlit |
| Dil | Python 3.11+ |
| LLM — geliştirme | Ollama (Gemma 3:4b, Llama 3.1:8b) |
| LLM — deploy | Groq API (llama-3.1-8b-instant) |
| Embedding | nomic-embed-text (Ollama) |
| Vektör Veritabanı | ChromaDB (in-memory, oturum bazlı) |
| Web Arama | Tavily API |
| Deploy | Streamlit Community Cloud |

> **Not:** Proje tamamen Python ile geliştirilmektedir. Streamlit, hem arayüzü hem de uygulama mantığını tek bir dilde yazmamızı sağladığı için tercih edilmiştir — ayrı bir frontend framework'üne (React/Next.js vb.) ihtiyaç duyulmamaktadır.

**Product Backlog:** Proje linki eklenecek.....

---

## Sprint 1 — 19 Haziran / 5 Temmuz 2026

### Sprint Hedefi
Temel uygulama iskeletinin kurulması; tema seçimi → fikir önerisi → Ollama entegrasyonu akışının Streamlit arayüzünde uçtan uca çalışır hale getirilmesi.

---

### Backlog Dağıtım Mantığı

Sprint 1'de toplam **21 story point** planlandı. Story'ler aşağıdaki öncelik mantığıyla seçildi:

1. **Altyapı önce:** Ollama entegrasyonu ve Streamlit kurulumu olmadan hiçbir özellik geliştirilemez.
2. **Dikey dilim yaklaşımı:** Sprint sonunda en az tema → fikir akışı uçtan uca çalışmalı, tek bir `app.py` üzerinden test edilebilir olmalı.
3. **RAG pipeline Sprint 2'ye ertelendi:** ChromaDB ve Tavily entegrasyonu bağımlılık zinciri oluşturduğundan kapsam dışı bırakıldı.

| ID | User Story | Atanan | Puan | Durum |
|----|-----------|--------|------|-------|
| US-01 | Projeye ait detayların hazırlanması ve repo hazırlıklarının yapılması | Burak | 2 | ✅ Done |

---

### Daily Scrum Notları

📎 Notların tamamı için: [docs/sprint1/daily_scrums.md](docs/sprint1/daily_scrums.md)

---

### Sprint Board

_Ekran görüntüsü sprint ilerledikçe güncellenecektir._

---

### Ürün Durumu

_Sprint 1 tamamlandığında çalışan Streamlit ekranlarının görüntüleri buraya eklenecek._

---

### Sprint Review

_5 Temmuz 2026 sonrasında doldurulacak._

**Tamamlanan story'ler:**

**Tamamlanamayan story'ler ve nedenler:**

**Demo notları:**

---

### Sprint Retrospective

_5 Temmuz 2026 sonrasında doldurulacak._

**İyi gidenler:**

**Geliştirmemiz gerekenler:**

**Sprint 2 için aksiyon maddeleri:**

---

## Sprint 2 — 6 Temmuz / 19 Temmuz 2026

_Sprint 2 başlangıcında güncellenecek._

---

## Sprint 3 — 20 Temmuz / 2 Ağustos 2026

_Sprint 3 başlangıcında güncellenecek._

---

## Proje Yapısı

```
IdeApp/
├── README.md
├── app.py                  # Streamlit giriş noktası, tüm UI burada
├── requirements.txt
├── .env.example
├── services/
│   ├── llm_service.py      # Ollama / Groq soyutlama katmanı
│   ├── search_service.py   # Tavily entegrasyonu
│   └── rag_service.py      # ChromaDB + embedding + retrieval
├── components/
│   ├── theme_picker.py     # tema seçim ekranı fonksiyonu
│   ├── idea_picker.py      # fikir seçim ekranı fonksiyonu
│   └── chat_ui.py          # RAG sohbet ekranı fonksiyonu
└── docs/
    ├── sprint1/
    │   ├── planning.md
    │   ├── daily_scrums.md
    │   ├── review.md
    │   └── retrospective.md
    ├── sprint2/
    └── sprint3/
```

---

## Kurulum

Proje adımları tamamlandıkça eklenecektir...

