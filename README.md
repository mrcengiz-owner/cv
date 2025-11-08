# Murat Cengiz - CV Web Sitesi

Bu proje, Django framework kullanılarak geliştirilmiş modern ve uzay temalı bir özgeçmiş web sitesidir.

## Özellikler

- 🚀 Modern ve responsive tasarım
- ⭐ Animasyonlu yıldız arka planı
- 📱 Mobil uyumlu (responsive)
- 📄 PDF CV indirme özelliği
- 🎨 Gradient renkler ve animasyonlar
- ⚡ Hızlı ve optimize edilmiş

## Teknolojiler

- **Backend**: Django 5.1.6
- **Frontend**: HTML5, CSS3, JavaScript
- **Fontlar**: Google Fonts (Orbitron, Inter)

## Kurulum

### Gereksinimler

- Python 3.8+
- pip (Python paket yöneticisi)

### Adımlar

1. Projeyi klonlayın veya indirin:
```bash
git clone <repository-url>
cd cv
```

2. Sanal ortam oluşturun (önerilir):
```bash
python -m venv venv
```

3. Sanal ortamı etkinleştirin:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

5. Veritabanı migrasyonlarını çalıştırın:
```bash
python manage.py migrate
```

6. Development sunucusunu başlatın:
```bash
python manage.py runserver
```

7. Tarayıcınızda şu adresi açın:
```
http://127.0.0.1:8000/
```

## Proje Yapısı

```
cv/
├── cv_app/              # Ana Django uygulaması
│   ├── migrations/      # Veritabanı migrasyonları
│   ├── views.py         # View fonksiyonları
│   ├── models.py        # Veritabanı modelleri
│   └── ...
├── cv_project/          # Django proje ayarları
│   ├── settings.py      # Proje ayarları
│   ├── urls.py          # URL yapılandırması
│   └── ...
├── templates/           # HTML şablonları
│   └── cv_app/
│       └── index.html
├── static/              # Statik dosyalar (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── media/               # Medya dosyaları (PDF, resimler)
│   └── cv.pdf
├── manage.py            # Django yönetim scripti
├── requirements.txt     # Python paket gereksinimleri
└── README.md            # Bu dosya
```

## Geliştirme

### Static Dosyaları Toplama

Production ortamı için static dosyaları toplamak için:
```bash
python manage.py collectstatic
```

### Admin Paneli

Django admin paneline erişmek için önce bir süper kullanıcı oluşturun:
```bash
python manage.py createsuperuser
```

Sonra admin paneline şu adresten erişebilirsiniz:
```
http://127.0.0.1:8000/admin/
```

## Production Dağıtımı

Production ortamı için:

1. `settings.py` dosyasında `DEBUG = False` yapın
2. `ALLOWED_HOSTS` listesine domain adresinizi ekleyin
3. Static dosyaları toplayın: `python manage.py collectstatic`
4. Veritabanı için uygun bir veritabanı sistemi kullanın (PostgreSQL, MySQL vb.)
5. Web sunucusu olarak Nginx + Gunicorn veya benzeri bir kombinasyon kullanın

## Lisans

Bu proje kişisel kullanım içindir.

## İletişim

- **E-posta**: mracengiz@gmail.com
- **Telefon**: +90 537 512 3099
- **Konum**: Mardin, Türkiye

---

© 2025 Murat Cengiz. Coded with 💙 and ☕

