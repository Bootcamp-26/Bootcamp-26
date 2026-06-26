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
