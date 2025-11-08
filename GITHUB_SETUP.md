# GitHub'a Yükleme Adımları

## ✅ Git Hazırlıkları Tamamlandı

- ✅ Git repository başlatıldı
- ✅ Dosyalar commit edildi
- ✅ Branch `main` olarak ayarlandı
- ✅ Remote repository eklendi: `https://github.com/mrcengiz-owner/cv.git`

## 1. GitHub'da Yeni Repository Oluştur

1. GitHub'a giriş yap: https://github.com
2. Sağ üst köşedeki "+" butonuna tıkla ve "New repository" seç
3. Repository bilgilerini gir:
   - **Repository name**: `cv` (remote zaten bu isimle ayarlandı)
   - **Description**: "Django ile geliştirilmiş özgeçmiş web sitesi"
   - **Visibility**: Public veya Private (istediğin seçeneği seç)
   - **⚠️ ÖNEMLİ**: "Initialize this repository with" kısmında **HİÇBİR ŞEY İŞARETLEME** (README, .gitignore, license) - Çünkü zaten dosyalarımız hazır
4. "Create repository" butonuna tıkla

## 2. Dosyaları GitHub'a Yükle

Repository oluşturduktan sonra aşağıdaki komutu çalıştır:

```bash
git push -u origin main
```

Eğer authentication sorunu yaşarsan:
- GitHub kullanıcı adı ve şifre yerine Personal Access Token kullanman gerekebilir
- Token oluşturmak için: GitHub Settings > Developer settings > Personal access tokens > Tokens (classic) > Generate new token
- Token'a `repo` yetkisi ver

## Alternatif: GitHub Desktop Kullan

Eğer GitHub Desktop kullanıyorsan:

1. GitHub Desktop'ı aç
2. File > Add Local Repository
3. Bu klasörü seç (C:\Users\Murat\Desktop\cv)
4. Publish repository butonuna tıkla
5. Repository adını ve açıklamasını gir
6. Publish butonuna tıkla

## Notlar

- İlk push'ta GitHub kullanıcı adı ve şifre/access token isteyebilir
- Eğer 2FA (iki faktörlü kimlik doğrulama) aktifse, Personal Access Token kullanman gerekebilir
- Token oluşturmak için: GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)

