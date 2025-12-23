from django.db import models
from django.core.exceptions import ValidationError

class Profile(models.Model):
    full_name = models.CharField(max_length=100, default="Murat Cengiz")
    subtitle = models.CharField(max_length=200, default="Software Developer & Space Enthusiast")
    tagline = models.CharField(max_length=200, default="From Code to Cosmos 🚀")
    
    # Hakkımda Kısmı
    about_title = models.CharField(max_length=200, default="6 Yaşında Başlayan Bir Yolculuk")
    about_emoji = models.CharField(max_length=10, default="👨‍💻", help_text="Profil resmi yerine geçen emoji")
    about_text = models.TextField(help_text="Paragraflar arası boşluk bırakarak yazınız.")
    
    # Footer
    footer_text = models.CharField(max_length=200, default="© 2025 Murat Cengiz. Coded with 💙 and ☕")

    def save(self, *args, **kwargs):
        if not self.pk and Profile.objects.exists():
            raise ValidationError('Sadece bir tane Profile kaydı olabilir.')
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Profil Ayarları"
        verbose_name_plural = "Profil Ayarları"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, help_text="Emoji ikonu (örn: 💻)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Yetenek Kategorisi"
        verbose_name_plural = "Yetenek Kategorileri"

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Yetenek"
        verbose_name_plural = "Yetenekler"

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100, help_text="Örn: 2014 - Günümüz")
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Deneyim"
        verbose_name_plural = "Deneyimler"

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class ContactInfo(models.Model):
    title = models.CharField(max_length=50) # Telefon, E-posta
    icon = models.CharField(max_length=10) # 📞
    value = models.CharField(max_length=100) # +90 537...
    link = models.CharField(max_length=200, blank=True) # tel:..., mailto:...
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "İletişim Bilgisi"
        verbose_name_plural = "İletişim Bilgileri"

    def __str__(self):
        return self.title
