FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "mysite.wsgi:application"]
```

## 📝 Düzeltme Adımları:

### 1. GitHub/GitLab'da Dockerfile'ı Düzeltin

1. Repository'nize gidin
2. `Dockerfile` dosyasını açın
3. **Tüm içeriği silin**
4. Yukarıdaki kodu (markdown olmadan) yapıştırın
5. Commit edin: `"Fix Dockerfile syntax"`

### 2. requirements.txt'yi de Kontrol Edin

`requirements.txt` dosyanızda da markdown olmasın:
```
Django>=4.2,<5.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
python-decouple==3.8
whitenoise==6.6.0
