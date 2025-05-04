# Afet Yardım Koordinasyon Uygulaması

Bu uygulama, afet durumlarında yardım taleplerini ve yardım tekliflerini koordine etmek için geliştirilmiş bir web uygulamasıdır.

## Özellikler

- Kullanıcılar yardım talebi veya teklifi oluşturabilir
- Konum bazlı harita görüntüleme
- Otomatik eşleştirme sistemi
- Bildirim sistemi
- Modern ve kullanıcı dostu arayüz

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repo-url]
cd [repo-name]
```

2. Sanal ortam oluşturun ve aktif edin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
# veya
.\venv\Scripts\activate  # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Uygulamayı çalıştırın:
```bash
python app.py
```

## Kullanım

1. Tarayıcınızda `http://localhost:5000` adresine gidin
2. Yeni bir mesaj oluşturmak için "Yeni Mesaj" butonuna tıklayın
3. Mesajınızı girin ve konumunuzu seçin
4. Haritada diğer mesajları görüntüleyin ve eşleşmeleri takip edin

## Teknolojiler

- Flask (Backend)
- SQLite (Veritabanı)
- Leaflet.js (Harita)
- Bootstrap (UI)
- JavaScript (Frontend)

## Lisans

MIT