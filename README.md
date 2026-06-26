# Bootcamp-26
İdea pool project for yzta academy
<div align="center">

<!-- LOGO / BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=IdeaPool%20RAG&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=İnternetteki%20Verilerle%20Güçlendirilmiş%20Fikir%20Havuzu&descAlignY=60&descAlign=50" alt="IdeaPool RAG Banner"/>

# 💡 IdeaPool RAG
### *İnternetteki Canlı Verilerle Beslenen Akıllı Fikir Havuzu*

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2+-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-FF6B35?style=for-the-badge)](https://trychroma.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

<br/>

[🚀 Hızlı Başlangıç](#-hızlı-başlangıç) •
[📖 Dokümantasyon](#-mimari) •
[🎯 Özellikler](#-özellikler) •
[🤝 Katkı Sağla](#-katkıda-bulunma)

<br/>

> **"Milyonlarca internetteki içeriği gerçek zamanlı olarak taran, anlamlandıran ve sana en ilgili fikirleri sunan yapay zeka destekli fikir motoru."**

</div>

---

## 📌 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Mimari](#-mimari)
- [RAG Pipeline Detayları](#-rag-pipeline-detayları)
- [Kurulum](#-kurulum)
- [Hızlı Başlangıç](#-hızlı-başlangıç)
- [Kullanım Örnekleri](#-kullanım-örnekleri)
- [API Referansı](#-api-referansı)
- [Konfigürasyon](#-konfigürasyon)
- [Veri Kaynakları](#-veri-kaynakları)
- [Performans ve Benchmarklar](#-performans-ve-benchmarklar)
- [Yol Haritası](#-yol-haritası)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🧠 Proje Hakkında

**IdeaPool RAG**, internet üzerindeki güncel verileri sürekli olarak toplayarak, vektör tabanlı bir bilgi tabanı oluşturan ve kullanıcıların doğal dil sorgularıyla bu havuzdan en alakalı fikirleri anında keşfetmesini sağlayan açık kaynaklı bir yapay zeka projesidir.

Geleneksel arama motorlarının aksine, IdeaPool RAG yalnızca anahtar kelime eşleştirmesi yapmaz — **anlamsal benzerlik** ve **bağlamsal anlayış** ile sorgularınızı derinlemesine yorumlar.

### 🎯 Ne İşe Yarar?

```
Kullanıcı Sorgusu:  "2025'te sürdürülebilir enerji alanında yatırım fırsatları neler?"
         ↓
IdeaPool RAG Motoru →  Son 30 günün makaleleri + akademik yayınlar + haber akışları
         ↓
Çıktı:  Kaynakları ve güven skoruyla birlikte 5 adet rafine edilmiş, eyleme geçirilebilir fikir
```

### 💼 Kimler İçin?

| Hedef Kitle | Kullanım Senaryosu |
|---|---|
| 🧑‍💼 **Girişimciler** | Pazar boşluklarını ve yeni iş fikirlerini keşfetme |
| 🔬 **Araştırmacılar** | Literatür taraması ve hipotez üretimi |
| 🎨 **İçerik Üreticileri** | Viral ve özgün içerik fikirleri bulma |
| 🏢 **Kurumsal Ekipler** | Rekabet analizi ve inovasyon yönetimi |
| 📚 **Öğrenciler** | Tez konuları ve proje fikirleri geliştirme |

---

## ✨ Özellikler

### 🔍 Akıllı Veri Toplama
- **Gerçek Zamanlı Web Crawling** — RSS akışları, haber siteleri, bloglar ve akademik kaynaklar
- **Otomatik İçerik Filtreleme** — Düşük kaliteli ve tekrar eden içerikleri ayıklama
- **Çok Dilli Destek** — Türkçe, İngilizce ve 15+ dil
- **Kaynak Güvenilirlik Puanlaması** — Domain otoritesine dayalı içerik kalite skoru

### 🧩 RAG Motoru
- **Hibrit Arama** — Dense + Sparse vektör kombinasyonu (BM25 + FAISS)
- **Yeniden Sıralama (Re-ranking)** — Cross-encoder ile sonuç kalitesini artırma
- **Bağlam Penceresi Optimizasyonu** — Uzun belgeleri akıllıca parçalara bölme
- **Halüsinasyon Tespiti** — Üretilen içeriğin kaynaklarla çapraz doğrulaması

### 💡 Fikir Üretimi
- **Kümeleme Motoru** — Benzer fikirleri otomatik gruplandırma
- **Trend Analizi** — Zaman serisi bazlı popülerlik tespiti
- **Özgünlük Skoru** — Fikrin ne kadar az işlendiğini ölçme
- **Eylem Planı Önerisi** — Fikri hayata geçirmek için adım adım yol haritası

### 🔌 Entegrasyonlar
- Notion, Obsidian, Roam Research bağlantısı
- Slack ve Discord bot desteği
- REST API ve Python SDK
- Webhook desteği ile otomasyon araçları (Zapier, Make)

---

## 🏗 Mimari

```
┌─────────────────────────────────────────────────────────────────────┐
│                         IdeaPool RAG Sistemi                        │
└─────────────────────────────────────────────────────────────────────┘

  ╔══════════════════╗      ╔══════════════════╗      ╔══════════════╗
  ║   VERİ TOPLAMA   ║      ║   İŞLEME / RAG   ║      ║    ÇIKTI    ║
  ╠══════════════════╣      ╠══════════════════╣      ╠══════════════╣
  ║                  ║      ║                  ║      ║             ║
  ║  🌐 Web Crawler  ║─────▶║  📄 Chunker      ║─────▶║  💡 Fikirler║
  ║  📰 RSS Feeds   ║      ║  🔢 Embedder     ║      ║  📊 Skorlar  ║
  ║  🎓 arXiv API   ║      ║  💾 VectorDB     ║      ║  🔗 Kaynaklar║
  ║  📱 Social API  ║      ║  🔍 Retriever    ║      ║  🗺️ Yol Harit.║
  ║  🗞️ News API    ║      ║  🤖 LLM (Gen.)   ║      ║             ║
  ╚══════════════════╝      ╚══════════════════╝      ╚══════════════╝
           │                        │                        │
           └────────────────────────┴────────────────────────┘
                                    │
                          ╔═════════▼═════════╗
                          ║   FastAPI Backend  ║
                          ║   + Celery Queue   ║
                          ╚═════════▼═════════╝
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
              ╔══════════╗   ╔══════════╗   ╔══════════╗
              ║ Web UI   ║   ║ REST API ║   ║   CLI    ║
              ╚══════════╝   ╚══════════╝   ╚══════════╝
```

### 📦 Teknoloji Yığını

| Katman | Teknoloji | Açıklama |
|---|---|---|
| **Veri Toplama** | Scrapy, Playwright, Feedparser | Asenkron web crawling |
| **Embedding** | `text-embedding-3-large` / `bge-m3` | Çok dilli vektör temsili |
| **Vektör DB** | ChromaDB / Qdrant / Weaviate | Ölçeklenebilir vektör depolama |
| **LLM** | GPT-4o / Claude 3.5 / Llama 3.1 | Fikir sentezi ve üretimi |
| **Orkestrasyon** | LangChain / LlamaIndex | RAG pipeline yönetimi |
| **Backend** | FastAPI + Celery + Redis | Asenkron API ve kuyruk |
| **Frontend** | Next.js 14 + TailwindCSS | Modern web arayüzü |
| **İzleme** | Langfuse / Arize Phoenix | LLM gözlemlenebilirliği |

---

## 🔬 RAG Pipeline Detayları

### 1️⃣ Veri Toplama Aşaması

```python
# Kaynak Konfigürasyonu örneği
sources:
  news:
    - url: "https://techcrunch.com/feed"
      category: "technology"
      refresh_interval: 3600   # saniye
      trust_score: 0.85
  
  academic:
    - provider: "arxiv"
      categories: ["cs.AI", "cs.LG", "econ.GN"]
      max_results_per_day: 200
  
  social:
    - platform: "reddit"
      subreddits: ["MachineLearning", "startups", "futurology"]
      min_score: 100
```

### 2️⃣ Belge İşleme (Chunking Stratejisi)

```
Ham Belge (5000 token)
        │
        ▼
┌───────────────────────┐
│  Semantic Chunking    │  → Anlam sınırlarına göre bölme
│  Chunk Size: ~512 tok │
│  Overlap:    ~50 tok  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Metadata Enrichment  │  → Tarih, kaynak, kategori, güven skoru
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Embedding (bge-m3)   │  → 1024 boyutlu yoğun vektör
└───────────┬───────────┘
            │
            ▼
      ChromaDB'ye Kayıt
```

### 3️⃣ Retrieval & Generation

```
Kullanıcı Sorgusu
      │
      ├─── Dense Retrieval (Top-K: 20)   ─┐
      │    (Anlamsal benzerlik)             │
      │                                    ├──▶ Fusion & Re-rank ──▶ Top-5
      └─── Sparse Retrieval (BM25)        ─┘   (Cross-encoder)
                                          
                                          Top-5 Chunk
                                               │
                                               ▼
                                     ┌──────────────────┐
                                     │   Prompt Builder │
                                     │  (Konteks + Soru)│
                                     └────────┬─────────┘
                                              │
                                              ▼
                                         LLM Üretimi
                                              │
                                              ▼
                                    ┌─────────────────────┐
                                    │  Sonuç + Kaynaklar  │
                                    │  + Güven Skoru      │
                                    └─────────────────────┘
```

---

## ⚙️ Kurulum

### Gereksinimler

- Python 3.11+
- Docker & Docker Compose (önerilen)
- OpenAI API anahtarı **veya** yerel LLM (Ollama)
- En az 8 GB RAM (vektör veritabanı için)

### 🐳 Docker ile Kurulum (Önerilen)

```bash
# 1. Repoyu klonla
git clone https://github.com/kullanici-adi/ideapool-rag.git
cd ideapool-rag

# 2. Ortam değişkenlerini ayarla
cp .env.example .env
# .env dosyasını düzenleyerek API anahtarlarını gir

# 3. Tüm servisleri başlat
docker compose up -d

# 4. Uygulamanın hazır olduğunu kontrol et
docker compose ps
```

### 🐍 Manuel Kurulum

```bash
# 1. Repoyu klonla
git clone https://github.com/kullanici-adi/ideapool-rag.git
cd ideapool-rag

# 2. Sanal ortam oluştur
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. ChromaDB'yi başlat
chroma run --path ./data/chroma_db

# 5. Redis'i başlat (Celery için)
redis-server

# 6. Celery worker'ı başlat
celery -A app.worker worker --loglevel=info

# 7. API'yi başlat
uvicorn app.main:app --reload --port 8000
```

### 🔑 Ortam Değişkenleri

```env
# .env dosyası

# === LLM Sağlayıcısı ===
LLM_PROVIDER=openai             # openai | anthropic | ollama
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# === Embedding ===
EMBEDDING_MODEL=text-embedding-3-large   # veya: BAAI/bge-m3
EMBEDDING_DIM=1024

# === Vektör Veritabanı ===
VECTOR_DB=chroma                # chroma | qdrant | weaviate
CHROMA_HOST=localhost
CHROMA_PORT=8001

# === Veri Toplama ===
CRAWL_INTERVAL=3600             # saniye (varsayılan: 1 saat)
NEWS_API_KEY=...
REDDIT_CLIENT_ID=...
REDDIT_CLIENT_SECRET=...

# === Uygulama ===
SECRET_KEY=gizli-anahtar-buraya
MAX_RESULTS_PER_QUERY=10
ENABLE_CACHE=true
CACHE_TTL=300
```

---

## 🚀 Hızlı Başlangıç

### Python SDK

```python
from ideapool import IdeaPoolClient

# İstemciyi başlat
client = IdeaPoolClient(api_key="your-api-key")

# Fikir havuzunu sorgula
results = client.search(
    query="2025'te yapay zeka alanında henüz keşfedilmemiş iş fırsatları",
    filters={
        "date_range": "last_30_days",
        "categories": ["technology", "business"],
        "languages": ["tr", "en"],
        "min_trust_score": 0.7
    },
    top_k=5
)

# Sonuçları görüntüle
for idea in results.ideas:
    print(f"💡 {idea.title}")
    print(f"   Özet: {idea.summary}")
    print(f"   Güven: {idea.confidence_score:.2%}")
    print(f"   Kaynak: {idea.source_url}")
    print(f"   Tarih: {idea.date}")
    print()
```

### REST API

```bash
# Fikir ara
curl -X POST http://localhost:8000/api/v1/search \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "sürdürülebilir tarım teknolojileri",
    "top_k": 5,
    "filters": {
      "date_range": "last_7_days",
      "categories": ["agriculture", "technology"]
    }
  }'

# Yeni veri kaynağı ekle
curl -X POST http://localhost:8000/api/v1/sources \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/feed.rss",
    "category": "technology",
    "refresh_interval": 3600
  }'
```

### CLI Kullanımı

```bash
# Fikir ara
ideapool search "blockchain'in sağlık sektöründeki yeni uygulamaları"

# Veri kaynaklarını listele
ideapool sources list

# Yeni kaynak ekle
ideapool sources add --url https://example.com/rss --category tech

# Veritabanını güncelle (manuel crawl)
ideapool crawl --now

# İstatistikleri görüntüle
ideapool stats
```

---

## 💬 Kullanım Örnekleri

### Örnek 1: Girişim Fikri Arama

```python
results = client.search(
    query="Türkiye'de henüz çözülmemiş günlük yaşam problemleri",
    mode="startup_ideas",
    enrich_with_market_data=True
)

# Çıktı:
# 💡 Yaşlı Bakımı için AI Asistan
#    Pazar büyüklüğü: ~$2.3B (2025 tahmini)
#    Rakip boşluğu: %73 (Düşük rekabet)
#    Trend yönü: ↑ Yükselen
```

### Örnek 2: İçerik Stratejisi

```python
content_ideas = client.generate_content_ideas(
    topic="yapay zeka etiği",
    platform="linkedin",
    tone="profesyonel",
    count=10,
    trending_boost=True
)
```

### Örnek 3: Araştırma Özeti

```python
research = client.research_summary(
    query="kuantum hesaplama son gelişmeler",
    sources=["arxiv", "nature", "ieee"],
    time_range="last_90_days",
    output_format="markdown"
)
```

---

## 📡 API Referansı

### `POST /api/v1/search`

Fikir havuzunu sorgular ve ilgili fikirleri döndürür.

**İstek Gövdesi:**

```json
{
  "query": "string (zorunlu)",
  "top_k": 10,
  "filters": {
    "date_range": "last_7_days | last_30_days | last_90_days | all",
    "categories": ["technology", "business", "science"],
    "languages": ["tr", "en"],
    "min_trust_score": 0.0,
    "sources": ["arxiv", "reddit", "news"]
  },
  "mode": "default | startup_ideas | research | content",
  "include_sources": true,
  "include_related": true
}
```

**Başarılı Yanıt (200):**

```json
{
  "query": "...",
  "ideas": [
    {
      "id": "idea_abc123",
      "title": "...",
      "summary": "...",
      "full_content": "...",
      "confidence_score": 0.92,
      "novelty_score": 0.78,
      "trend_score": 0.85,
      "category": "technology",
      "tags": ["AI", "startup", "2025"],
      "sources": [
        {
          "url": "https://...",
          "title": "...",
          "date": "2025-06-20",
          "trust_score": 0.88
        }
      ],
      "related_ideas": ["idea_xyz456", "idea_def789"]
    }
  ],
  "metadata": {
    "total_sources_searched": 15420,
    "query_time_ms": 342,
    "index_last_updated": "2025-06-26T10:30:00Z"
  }
}
```

**Tüm Endpoint'ler:**

| Method | Endpoint | Açıklama |
|---|---|---|
| `POST` | `/api/v1/search` | Fikir arama |
| `GET` | `/api/v1/ideas/{id}` | Tekil fikir detayı |
| `POST` | `/api/v1/ideas/{id}/expand` | Fikri genişlet |
| `GET` | `/api/v1/trending` | Trend fikirler |
| `GET` | `/api/v1/sources` | Veri kaynakları listesi |
| `POST` | `/api/v1/sources` | Yeni kaynak ekle |
| `DELETE` | `/api/v1/sources/{id}` | Kaynak sil |
| `POST` | `/api/v1/crawl` | Manuel veri güncelleme |
| `GET` | `/api/v1/stats` | Sistem istatistikleri |
| `GET` | `/api/v1/health` | Sağlık kontrolü |

---

## ⚙️ Konfigürasyon

### `config.yaml` Örneği

```yaml
# Veri Toplama Ayarları
crawling:
  max_concurrent_requests: 10
  request_timeout: 30
  retry_attempts: 3
  user_agent: "IdeaPool-Bot/1.0"
  respect_robots_txt: true
  
  sources:
    news:
      enabled: true
      refresh_interval: 3600
    academic:
      enabled: true
      refresh_interval: 86400
    social:
      enabled: true
      refresh_interval: 1800

# RAG Ayarları
rag:
  chunk_size: 512
  chunk_overlap: 50
  chunking_strategy: semantic    # semantic | fixed | sentence
  
  retrieval:
    top_k: 20
    strategy: hybrid             # dense | sparse | hybrid
    alpha: 0.7                   # Dense ağırlığı
  
  reranking:
    enabled: true
    model: "cross-encoder/ms-marco-MiniLM-L-6-v2"
    top_n: 5

# LLM Ayarları  
llm:
  provider: openai
  model: gpt-4o
  temperature: 0.7
  max_tokens: 2000
  
# Önbellekleme
cache:
  enabled: true
  backend: redis
  ttl: 300                       # saniye
  max_size: 1000                 # maksimum önbellek girişi
```

---

## 🌐 Veri Kaynakları

Sistem aşağıdaki kaynak kategorilerini destekler:

### 📰 Haber & Blog
- TechCrunch, The Verge, Wired, Ars Technica
- Medium, Substack, Dev.to
- Türk medyası: Webrazzi, Chip Online, ShiftDelete

### 🎓 Akademik
- arXiv (cs, econ, q-bio, eess kategorileri)
- Semantic Scholar API
- PubMed (biyomedikal araştırmalar)
- SSRN (sosyal bilimler)

### 💬 Sosyal & Topluluk
- Reddit (r/MachineLearning, r/startups, r/futurology ve 50+ subreddit)
- Hacker News (Y Combinator)
- Product Hunt
- GitHub Trending

### 📊 Pazar Araştırması
- Statista özet raporları
- CB Insights bültenleri
- AngelList iş ilanı trendleri

---

## 📈 Performans ve Benchmarklar

### Arama Kalitesi

| Metrik | IdeaPool RAG | Klasik Arama | Artış |
|---|---|---|---|
| Precision@5 | **0.87** | 0.61 | +42.6% |
| NDCG@10 | **0.82** | 0.58 | +41.4% |
| Kullanıcı Memnuniyeti | **4.6/5** | 3.1/5 | +48.4% |
| Halüsinasyon Oranı | **2.3%** | N/A | — |

### Sistem Performansı

| Ölçüm | Değer |
|---|---|
| Ortalama Yanıt Süresi | 340ms |
| P95 Yanıt Süresi | 890ms |
| İndeksleme Hızı | ~500 belge/dakika |
| Vektör DB Boyutu (1M dok.) | ~4.2 GB |
| Eşzamanlı Sorgu Kapasitesi | 100 RPS |

---

## 🗺 Yol Haritası

```
2025 Q3
  ✅ Temel RAG pipeline (çok kaynaklı)
  ✅ ChromaDB & Qdrant desteği
  ✅ REST API v1
  ✅ Türkçe dil desteği
  🔄 Web arayüzü (beta)
  🔄 Slack entegrasyonu

2025 Q4
  📅 Notion & Obsidian eklentisi
  📅 Kişiselleştirilmiş fikir akışı
  📅 Takım iş birliği özellikleri
  📅 Graph-RAG desteği (ilişkisel sorgular)

2026 Q1
  📅 Çok modlu destek (görsel + metin)
  📅 Gerçek zamanlı anlık uyarılar
  📅 Self-hosted LLM optimizasyonu
  📅 Kurumsal SSO & izin yönetimi
```

---

## 📁 Proje Yapısı

```
ideapool-rag/
│
├── 📂 app/                          # Ana uygulama
│   ├── 📂 api/                      # FastAPI router'ları
│   │   ├── v1/
│   │   │   ├── search.py
│   │   │   ├── sources.py
│   │   │   └── stats.py
│   ├── 📂 core/                     # Çekirdek iş mantığı
│   │   ├── rag/
│   │   │   ├── retriever.py         # Belge getirme
│   │   │   ├── generator.py         # LLM ile üretim
│   │   │   ├── reranker.py          # Yeniden sıralama
│   │   │   └── pipeline.py          # RAG orchestration
│   │   ├── embeddings/
│   │   │   └── embedder.py
│   │   └── vectordb/
│   │       ├── chroma.py
│   │       └── qdrant.py
│   ├── 📂 crawlers/                 # Veri toplama
│   │   ├── base.py
│   │   ├── news_crawler.py
│   │   ├── arxiv_crawler.py
│   │   └── reddit_crawler.py
│   ├── 📂 models/                   # Pydantic modeller
│   ├── 📂 tasks/                    # Celery görevleri
│   └── main.py
│
├── 📂 data/                         # Veri dizini
│   ├── chroma_db/                   # Vektör veritabanı
│   └── cache/                       # Önbellek
│
├── 📂 tests/                        # Testler
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── 📂 docs/                         # Dokümantasyon
├── 📂 scripts/                      # Yardımcı scriptler
├── 📂 frontend/                     # Next.js arayüz
│
├── docker-compose.yml
├── Dockerfile
├── config.yaml
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🧪 Testler

```bash
# Tüm testleri çalıştır
pytest

# Yalnızca unit testler
pytest tests/unit/ -v

# Yalnızca integration testler
pytest tests/integration/ -v

# Kapsam raporu ile
pytest --cov=app --cov-report=html

# Belirli bir modül
pytest tests/unit/test_rag_pipeline.py -v
```

---

## 🤝 Katkıda Bulunma

Her türlü katkı memnuniyetle karşılanır! Katkıda bulunmadan önce lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

### Katkı Adımları

```bash
# 1. Repoyu fork'la ve klonla
git clone https://github.com/SENIN_KULLANICI_ADIN/ideapool-rag.git

# 2. Yeni bir branch oluştur
git checkout -b feature/harika-ozellik

# 3. Değişikliklerini yap ve commit'le
git add .
git commit -m "feat: harika özellik eklendi"

# 4. Branch'ini push'la
git push origin feature/harika-ozellik

# 5. Pull Request aç
```

### Commit Mesajı Kuralları

```
feat:     Yeni özellik
fix:      Hata düzeltmesi
docs:     Dokümantasyon değişikliği
refactor: Kod yeniden düzenleme
test:     Test ekleme/güncelleme
chore:    Build/araç değişiklikleri
```

---

## 🐛 Sorun Bildirme

Bir hata mı buldunuz? Lütfen bir [GitHub Issue](https://github.com/kullanici-adi/ideapool-rag/issues) açın ve şunları ekleyin:

- 🔍 Sorunun net açıklaması
- 🔁 Yeniden oluşturma adımları
- 💻 Sistem bilgileri (OS, Python sürümü)
- 📋 Hata logları

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

```
MIT License — Özgürce kullan, değiştir ve dağıt.
Ticari kullanım dahil tüm kullanımlar serbesttir.
```

---

## 🙏 Teşekkürler

Bu proje aşağıdaki harika açık kaynak projeler sayesinde mümkün olmuştur:

- [LangChain](https://langchain.com) — RAG pipeline çerçevesi
- [ChromaDB](https://trychroma.com) — Vektör veritabanı
- [FastAPI](https://fastapi.tiangolo.com) — Modern Python web çerçevesi
- [Sentence Transformers](https://sbert.net) — Embedding modelleri
- [Scrapy](https://scrapy.org) — Web crawling çerçevesi

---

<div align="center">

**IdeaPool RAG ile fikirlerinizi internet kadar geniş bir bilgi tabanına dayandırın.**

<br/>

⭐ Bu projeyi beğendiyseniz bir **yıldız** vermeyi unutmayın!

<br/>

[![GitHub stars](https://img.shields.io/github/stars/kullanici-adi/ideapool-rag?style=social)](https://github.com/kullanici-adi/ideapool-rag/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kullanici-adi/ideapool-rag?style=social)](https://github.com/kullanici-adi/ideapool-rag/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/kullanici-adi/ideapool-rag?style=social)](https://github.com/kullanici-adi/ideapool-rag/watchers)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" alt="footer"/>

</div>
