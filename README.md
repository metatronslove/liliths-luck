# 🔮 Lilith's Lucky Set Simulator

<div align="center">
  <img src="https://github.com/metatronslove/liliths-luck/raw/main/screenshot.png" width="800" alt="Sistem Ekran Görüntüsü">
</div>
*480 deneyin istatistiksel analiziyle oluşturulan şanslı sayı seti*

## ✨ Özellikler
- **480 bağımsız deney** yapar (her deneyde 7 şanslı sayı)
- **Sayı frekans analizi** ile en çok çıkan 7'li seti bulur
- Python ve JavaScript versiyonları
- Terminal ve web arayüz seçenekleri

## 🛠 Kurulum

### Python Versiyonu
```bash
git clone https://github.com/metatronslove/liliths-luck.git
cd liliths-luck
pip install -r requirements.txt
python lilith_lucky.py
```

### Web Versiyonu
```bash
git clone https://github.com/metatronslove/liliths-luck.git
cd liliths-luck/docs
# index.html dosyasını tarayıcıda açın
```

## 📊 Bilimsel Arka Plan
- **Olasılık Teorisi**: Her sayı için 6-6 gelme olasılığı 1/36 (~%2.78)
- **İstatistik**: 480 deney × 7 sayı = 3,360 veri noktası
- **Dağılım**: En çok çıkan sayıların 35-45 frekans aralığında olması beklenir

## 📝 Örnek Çıktı
```text
╔════════════════════════════╗
║   LILITH'S LUCKY SET       ║
╚════════════════════════════╝
1. 17 (Frekans: 42)
2. 23 (Frekans: 39)
...
7. 89 (Frekans: 34)
```

## 🌟 Proje Yapısı
```
liliths-luck/
├── python/
│   ├── lilith_lucky.py
│   └── requirements.txt
├── docs/
│   └── index.html
└── README.md
```

## 📜 Lisans
MIT Lisansı - [metatronslove](https://github.com/metatronslove) tarafından geliştirilmiştir.

> ⚠️ Uyarı: Bu proje istatistiksel simülasyon amaçlıdır. Şans oyunlarıyla ilişkisi yoktur.