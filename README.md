# evren-yolo26-83-models-benchmark

[![Hugging Face Benchmark](https://img.shields.io/badge/HF_Dataset-83_Models_Benchmark-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/datasets/kenantabak/evren-yolo26-yolo11-83-models-benchmark)
[![Interactive Space](https://img.shields.io/badge/HF_Space-Vision_Explorer-38bdf8?style=flat-square)](https://huggingface.co/spaces/kenantabak/EVREN-YOLO26-Vision-Explorer)

`%70+ mAP@50` kalite kapısını geçerek `PUBLIC + PRODUCTION` aşamasına alınan **126 adet `YOLO26s`, `YOLO26x` ve `YOLO11s` modelinin** karşılaştırmalı doğrulama (`validation`) metrikleri, özetleme betiği ve analiz defteri.

> Açık `.pt` ve `.onnx` ağırlıklarını Python ile çalıştırmak için **[evren-yolo-vision-kit](https://github.com/kenantabak/evren-yolo-vision-kit)** reposuna göz atabilirsiniz.

## Özet İstatistik Çalıştırma

```bash
python scripts/summarize_benchmarks.py
```

## Öne Çıkan İlk 30 Model (Tam 126 Model: `data/models_benchmark_83.csv`)

| # | Model (EVREN) | Mimari | mAP@50 (%) | mAP@50-95 (%) | F1 (%) |
| :-: | :--- | :---: | ---: | ---: | ---: |
| 1 | [Yer Fıstığı Küf ve Kalite](https://evren.ssyz.org.tr/models/u19979974710e/yer-fistigi-kuf-ve-kalite) | `yolo26s` | **%99.50** | %0.00 | %100.00 |
| 2 | [İç Mekan Mobilya Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/ic-mekan-mobilya-tespiti) | `yolo26s` | **%99.49** | %0.00 | %65.31 |
| 3 | [Yol ve Trafik İşareti Yön Tespiti (Dur / Sola Dönüş / Sağa Dönüş) v2](https://evren.ssyz.org.tr/models/u19979974710e/yol-ve-trafik-isareti-yon-tespiti-dur-sola-donus-saga-donus-v2) | `yolo26s` | **%99.26** | %94.75 | %98.19 |
| 4 | [Baskılı Devre Kartı (PCB) 6 Üretim Kusuru Tespiti Modeli](https://evren.ssyz.org.tr/models/u19979974710e/baskili-devre-karti-pcb-6-uretim-kusuru-tespiti-modeli) | `yolo11s` | **%99.15** | %60.63 | %98.55 |
| 5 | [Profil Bilgi Kartı Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/profil-bilgi-karti-tespiti) | `yolo26s` | **%99.15** | %0.00 | %97.39 |
| 6 | [Perakende ve Manav Taze Meyve Sebze Tespiti (22 Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/perakende-ve-manav-taze-meyve-sebze-tespiti-22-sinif) | `yolo26s` | **%98.94** | %86.80 | %97.17 |
| 7 | [El İşareti Rakam Tanıma](https://evren.ssyz.org.tr/models/u19979974710e/el-isareti-rakam-tanima) | `yolo26s` | **%98.78** | %0.00 | %97.04 |
| 8 | [Satranç Taşları Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/satranc-taslari-tespiti) | `yolo26s` | **%98.53** | %0.00 | %90.99 |
| 9 | [Endüstriyel KKD Tespiti Pro](https://evren.ssyz.org.tr/models/u19979974710e/endustriyel-kkd-tespiti-pro) | `yolo26x` | **%98.48** | %86.17 | %97.16 |
| 10 | [Endüstriyel KKD Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/endustriyel-kkd-tespiti) | `yolo26s` | **%98.44** | %83.37 | %96.89 |
| 11 | [Renk Kodlu İş Güvenliği Bareti Tespiti (Mavi ve Beyaz Sınıf) v2](https://evren.ssyz.org.tr/models/u19979974710e/renk-kodlu-is-guvenligi-bareti-tespiti-mavi-ve-beyaz-sinif-v2) | `yolo26s` | **%98.19** | %98.19 | %70.06 |
| 12 | [Havalimanı Apron ve Yer Hizmetleri Araçları Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/havalimani-apron-ve-yer-hizmetleri-araclari-tespiti) | `yolo11s` | **%98.03** | %66.45 | %95.57 |
| 13 | [Termal İnsan ve Köpek Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/termal-insan-ve-kopek-tespiti) | `yolo26s` | **%97.92** | %0.00 | %94.02 |
| 14 | [Elektrik Devre Şeması Sembol ve Bileşen Tespiti (6 Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/elektrik-devre-semasi-sembol-ve-bilesen-tespiti-6-sinif) | `yolo26s` | **%97.87** | %69.73 | %95.126 |
| 15 | [Karayolu Trafik Levhaları ve Trafik Işıkları Tespiti (21 Dengeli Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/karayolu-trafik-levhalari-ve-trafik-isiklari-tespiti-21-dengeli-sinif) | `yolo26s` | **%97.47** | %81.97 | %76.78 |
| 16 | [Havadan Renkli Küre Hedef](https://evren.ssyz.org.tr/models/u19979974710e/havadan-renkli-kure-hedef) | `yolo26s` | **%97.00** | %0.00 | %78.20 |
| 17 | [Trafik Motosiklet Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/trafik-motosiklet-tespiti) | `yolo26s` | **%96.87** | %0.00 | %94.79 |
| 18 | [Bisiklet, Elektrikli Scooter ve Motosiklet Sürücüsü Tespiti (3 Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/bisiklet-elektrikli-scooter-ve-motosiklet-surucusu-tespiti-3-sinif) | `yolo26s` | **%96.65** | %79.18 | %93.04 |
| 19 | [ABD Doları Banknot ve Para](https://evren.ssyz.org.tr/models/u19979974710e/abd-dolari-banknot-ve-para) | `yolo26s` | **%96.35** | %0.00 | %91.68 |
| 20 | [Köpekbalığı Dişi Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/kopekbaligi-disi-tespiti) | `yolo26s` | **%96.34** | %0.00 | %94.19 |
| 21 | [Liman Kamyon Şasi Durum Tespiti (Yüklü / Boş / Çalışıyor) v2](https://evren.ssyz.org.tr/models/u19979974710e/liman-kamyon-sasi-durum-tespiti-yuklu-bos-calisiyor-v2) | `yolo26s` | **%95.73** | %84.40 | %94.08 |
| 22 | [Endüstriyel Yüzey Kusuru](https://evren.ssyz.org.tr/models/u19979974710e/endustriyel-yuzey-kusuru) | `yolo26s` | **%95.70** | %0.00 | %93.01 |
| 23 | [Karayolu Trafik İşaretleri, Hız Sınırı ve Sinyalizasyon Tespiti (23 Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/karayolu-trafik-isaretleri-hiz-siniri-ve-sinyalizasyon-tespiti-23-sinif) | `yolo26s` | **%95.53** | %80.05 | %92.58 |
| 24 | [Belge Islak İmza Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/belge-islak-imza-tespiti) | `yolo26s` | **%95.02** | %0.00 | %92.33 |
| 25 | [Trafik Taşıtları ve Hız Sınırı Levhaları Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/trafik-tasitlari-ve-hiz-siniri-levhalari-tespiti) | `yolo26s` | **%94.95** | %79.95 | %92.07 |
| 26 | [İç Mekan Ev ve Ofis Mobilyaları Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/ic-mekan-ev-ve-ofis-mobilyalari-tespiti) | `yolo26s` | **%94.70** | %82.60 | %92.30 |
| 27 | [Hidroponik Marul Fidesi Büyüme Evreleri ve Viyol Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/hidroponik-marul-fidesi-buyume-evreleri-ve-viyol-tespiti) | `yolo26s` | **%94.51** | %72.08 | %90.65 |
| 28 | [Karayolu Otomobil, Motosiklet, Kamyon ve Otobüs Tespiti (4 Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/karayolu-otomobil-motosiklet-kamyon-ve-otobus-tespiti-4-sinif) | `yolo11s` | **%93.98** | %77.48 | %89.64 |
| 29 | [Orman Yangını Dumanı Tespiti](https://evren.ssyz.org.tr/models/u19979974710e/orman-yangini-dumani-tespiti) | `yolo26s` | **%93.96** | %0.00 | %90.00 |
| 30 | [Geniş Ölçekli Karayolu Ağır Vasıta ve Kamyon Tespiti (4 Sınıf)](https://evren.ssyz.org.tr/models/u19979974710e/genis-olcekli-karayolu-agir-vasita-ve-kamyon-tespiti-4-sinif) | `yolo26s` | **%93.78** | %67.33 | %88.97 |

### Newly Added Production Models (22 November 2026)

| Model Repository | Domain | Architecture | mAP@50 | mAP@50-95 | F1 |
|---|---|---|---:|---:|---:|
| [kenantabak/yolo26s-knee-xray-acl-detection-tr](https://huggingface.co/kenantabak/yolo26s-knee-xray-acl-detection-tr) | Diz Röntgeninde Ön Çapraz Bağ (ACL) Bölgesi Tespiti | `yolo26s` | **99.50%** | 75.06% | 100.00% |
| [kenantabak/yolo26s-structural-surface-crack-detection-tr](https://huggingface.co/kenantabak/yolo26s-structural-surface-crack-detection-tr) | Yüzey ve Yapısal Çatlak Tespiti (320px Hafif Model) | `yolo26s` | **99.34%** | 74.78% | 98.69% |
| [kenantabak/yolo26s-maritime-naval-vessel-detection-tr](https://huggingface.co/kenantabak/yolo26s-maritime-naval-vessel-detection-tr) | Deniz Gözetiminde Savaş Gemisi Tespiti | `yolo26s` | **99.23%** | 80.85% | 98.46% |
| [kenantabak/yolo26s-powerline-insulator-defect-tr](https://huggingface.co/kenantabak/yolo26s-powerline-insulator-defect-tr) | Elektrik İletim Hattı İzolatör ve Yüzey Hasarı Tespiti | `yolo26s` | **98.25%** | 76.12% | 96.95% |

---

### 🔗 EVREN Open-Source Ecosystem
- **EVREN Platform:** [evren.ssyz.org.tr/users/u19979974710e](https://evren.ssyz.org.tr/users/u19979974710e) (`342` Grade-A Datasets · `185` Models)
- **Live Browser ONNX Demo Space:** [EVREN-Live-Object-Detection-Demo](https://huggingface.co/spaces/kenantabak/EVREN-Live-Object-Detection-Demo)
- **Hugging Face Portfolio:** [huggingface.co/kenantabak](https://huggingface.co/kenantabak) (`19` Production Models · `10` Datasets · `4` Spaces)
- **GitHub:** [github.com/kenantabak](https://github.com/kenantabak)
- **Dev.to Technical Series:** [dev.to/kenantabak](https://dev.to/kenantabak)
