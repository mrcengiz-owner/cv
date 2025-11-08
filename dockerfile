FROM python:3.11-slim

WORKDIR /app

# Sistem bağımlılıklarını kur
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projeyi kopyala
COPY . .

# Static dosyaları topla
RUN python manage.py collectstatic --noinput || true

# Port aç
EXPOSE 8000

# Gunicorn ile başlat
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "mysite.wsgi:application"]
```

**requirements.txt:**
```
Django>=4.2,<5.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
python-decouple==3.8
whitenoise==6.6.0
```

---

### 2. Coolify'da Build Pack Ayarı

Eğer Dockerfile'ınız yoksa ve Django projeniz klasik yapıdaysa:

1. Coolify'da uygulamanızın **Configuration** sekmesine gidin
2. **Build Pack** bölümünü bulun
3. **"Nixpacks"** veya **"Python"** seçin (Dockerfile yerine)
4. **Start Command** ekleyin:
```
   gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application
```

---

### 3. Repository Yapısını Kontrol Edin

Repository'nizin root dizini şöyle görünmeli:
```
mrcengiz-owner/cv:main/
├── Dockerfile          ← OLMALI
├── requirements.txt    ← OLMALI
├── manage.py          ← Django projesi
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── ...
```

---

### 4. Alternatif: Manuel Dockerfile Ekleme

Eğer repository'yi değiştiremiyorsanız, Coolify'da manuel ekleyebilirsiniz:

1. **Configuration** → **Build**
2. **"Use Custom Dockerfile"** seçin
3. Dockerfile içeriğini yapıştırın (yukarıdaki örneği kullanın)

---

## 🚀 Hızlı Test İçin Basit Çözüm

Eğer hızlıca test etmek istiyorsanız:

### Coolify'da "Nixpacks" Kullanın:

1. Uygulamanızı silin ve yeniden oluşturun
2. Bu sefer **"Nixpacks"** build pack seçin
3. Repository URL'inizi girin
4. **Port**: `8000`
5. **Start Command**: 
```
   gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application
