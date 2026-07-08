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

---

## Sprint 1 — 19 Haziran / 5 Temmuz 2026

### Sprint Hedefi
Temel uygulama iskeletinin kurulması; tema seçimi → fikir önerisi → Ollama entegrasyonu akışının Streamlit arayüzünde uçtan uca çalışır hale getirilmesi.

### Backlog Dağıtım Mantığı

Sprint 1'de fikre ait olan adımlar geliştiriciler tarafından kendi çalışma planına göre parçalanarak planlanmıştır.

1. **Altyapı önce:** Ollama entegrasyonu ve Streamlit kurulumu olmadan hiçbir özellik geliştirilemez.
2. **Dikey dilim yaklaşımı:** Sprint sonunda proje detayları ve tasarımları belirlenmiş ve tamamlanmış olması planlamıştır. Sprint 2'de geliştirmeye başlanılacaktır.
3. **RAG pipeline Sprint 2'ye ertelendi:** ChromaDB ve Tavily entegrasyonu bağımlılık zinciri oluşturduğundan kapsam dışı bırakıldı.

### Daily Scrum Notları

📎 Notların tamamı için: [docs/Sprint-1/daily_scrums.md](docs/Sprint-1/daily_scrums.md)

### Sprint Board

📎 Board görünümleri ve detayları için: [https://github.com/orgs/Bootcamp-26/projects/1/views/1](https://github.com/orgs/Bootcamp-26/projects/1/views/1)

### Ürün Durumu

Bu sprintte herhangi bir geliştirme ve tasarlama yapılmamıştır. Mimari ve genel yapısı üzerine planlama ve tartışmalar yapılmıştır.

### Sprint Review

Kararlar: Projeye dair araştırma ve framework çalışmaları yapılmıştır. Backlog üzerinde issue'lar açılarak ürüne dair çalışma planları developerlar tarafından hazırlanmıştır.

**Tamamlanan story'ler:**

Kullanılacak Frameworklerin belirlenmesi ve ürünün genel şeması üzerinde tasarlanılması beklenen şema ve yapı mimarisi üzerinde toplantılar yapılmıştır.

**Tamamlanamayan story'ler ve nedenler:**

Sprint 1 içerisinde ürüne dair planlama ve araştırma adımları yapılmıştır. Ürün geliştirme adımı Sprint 2 içerisinde yapılacaktır.

### Sprint Retrospective

**İyi gidenler:**

Ürün planlaması ve ürünün arşatırmalar sonucu istenilen kriterlere uygun olup olmadığına karar verilmiştir.

**Sprint 2 için aksiyon maddeleri:**

- Ürünün gelişme adımlarının planlarak hayata geçirilmesi

---

## Sprint 2 — 6 Temmuz / 19 Temmuz 2026

---

### Sprint Hedefi
Sprint 1'de bahsedilen ürünün production aşamalarının planlarak Code Base oluşturulmaya başlanması

### Backlog Dağıtım Mantığı

Sprint 2'de üretime ait parçalar Developer'lar tarafından kendi çalışma planlarına göre ayarlanmıştır. Ürünün oluşturulma adımları ve mimari tasarımında kullanılması planlanan adımlar aşağıdaki gibidir. Planlanan durumda Sprint sonunda çalışır ürün planlaması yapılmıştır. 

1. **Altyapı önce:** Ollama entegrasyonu ve Streamlit kurulumu olmadan hiçbir özellik geliştirilemez.
2. **Dikey dilim yaklaşımı:** Sprint sonunda projeye ait çalışır bir demo ürün ortaya çıkması planlanmıştır. Sprint 3'te geliştirme ve iyileştirme basamakları üzerine çalışılması planlanmıştır.

### Daily Scrum Notları

📎 Notların tamamı için: [docs/Sprint-1/daily_scrums.md](docs/Sprint-1/daily_scrums.md)

### Sprint Board

📎 Board görünümleri ve detayları için: [https://github.com/orgs/Bootcamp-26/projects/1/views/1](https://github.com/orgs/Bootcamp-26/projects/1/views/1)

### Ürün Durumu

Ürünün gelişme adımları tamamlandıkça durum bilgisi güncellenecektir.

### Sprint Review

| İsim | Çalışılacak Alan |
|---|---------|
|Burak| Her adımda ve alanda Developer backup |
|Asel| RAG Data Transition LLM to User |
|Zeynep| Rag Service |
|Bengisu| UI Design |
|İlkay| LLM Service |

**Tamamlanan story'ler:**

Sprint 2 adımları tamamlandıkça güncellenecektir...

**Tamamlanamayan story'ler ve nedenler:**

Sprint 2 içerisinde güncellenecek...

### Sprint Retrospective

**İyi gidenler:**

Sprint 2 süresince güncellenecektir.

**Sprint 3 için aksiyon maddeleri:**

Sprint 2 sonunda güncellenecek....


---

## Sprint 3 — 20 Temmuz / 2 Ağustos 2026

_Sprint 3 başlangıcında güncellenecek._

---

## Proje Yapısı

```
IdeApp/
├── README.md
├── app.py                  # Streamlit giriş noktası, tüm UI burada olacak şekilde planlandı, geliştirme durumuna göre değiştirilebilir.
├── requirements.txt
├── .env.example
├── services/
│   ├── llm_service.py      # Ollama / Groq soyutlama katmanı
│   ├── search_service.py   # Tavily entegrasyonu öncelikli düşünüldü, performans ve verimliliğe göre update edilebilir
│   └── rag_service.py      # ChromaDB + embedding + retrieval -> RAG gerekliliklerine uygun mimari tasarımı oluşturulacaktır.
├── components/
│   ├── theme_picker.py     # tema seçim ekranı fonksiyonu
│   ├── idea_picker.py      # fikir seçim ekranı fonksiyonu
│   └── chat_ui.py          # RAG sohbet ekranı fonksiyonu
└── docs/
    ├── Sprint-1/
    │   ├── planning.md
    │   ├── daily_scrums.md
    │   ├── review.md
    │   └── retrospective.md
    ├── Sprint-2/
    └── Sprint-3/
```

---

## Kurulum

Proje adımları tamamlandıkça eklenecektir...

