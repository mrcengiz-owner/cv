import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv_project.settings')
django.setup()

from cv_app.models import Profile, SkillCategory, Skill, Experience, ContactInfo

def populate():
    # 1. Profile
    if not Profile.objects.exists():
        print("Creating Profile...")
        Profile.objects.create(
            full_name="MURAT CENGİZ",
            subtitle="Software Developer & Space Enthusiast",
            tagline="From Code to Cosmos 🚀",
            about_title="6 Yaşında Başlayan Bir Yolculuk",
            about_emoji="👨‍💻",
            about_text="Bilgisayarlara 6 yaşında tanıştım, 10 yaşımda yazılım geliştirmeye başladım. Mardin Artuklu Üniversitesi Bilgisayar Programcılığı bölümünden mezun oldum.\n\n"
                       "Günümüzde yapay zeka, web teknolojileri ve Linux sunucu yönetimi üzerine çalışmaktayım. Freelance olarak müşterilere özel yazılım çözümleri geliştiriyorum.\n\n"
                       "Geleceğe Dair Hedefim: Uzay sistemleri mühendisliği alanında çalışarak, yazılım bilgimi uzay teknolojilerine uygulamak istiyorum. 🌌",
            footer_text="© 2025 Murat Cengiz. Coded with 💙 and ☕"
        )

    # 2. Skills
    if not SkillCategory.objects.exists():
        print("Creating Skills...")
        
        # Backend
        backend = SkillCategory.objects.create(name="Backend Development", icon="💻", order=1)
        Skill.objects.create(category=backend, name="C# & VB.NET", order=1)
        Skill.objects.create(category=backend, name="Python (Django)", order=2)
        Skill.objects.create(category=backend, name="Java", order=3)
        Skill.objects.create(category=backend, name="MySQL & MSSQL", order=4)

        # Frontend
        frontend = SkillCategory.objects.create(name="Frontend Development", icon="🎨", order=2)
        Skill.objects.create(category=frontend, name="HTML5 & CSS3", order=1)
        Skill.objects.create(category=frontend, name="JavaScript", order=2)
        Skill.objects.create(category=frontend, name="React.js (Öğreniyor)", order=3)
        Skill.objects.create(category=frontend, name="Vue.js (Öğreniyor)", order=4)

        # DevOps
        devops = SkillCategory.objects.create(name="Server & DevOps", icon="🖥️", order=3)
        Skill.objects.create(category=devops, name="Linux Server Kurulumu", order=1)
        Skill.objects.create(category=devops, name="cPanel, Plesk, Webmin", order=2)
        Skill.objects.create(category=devops, name="Apache & Nginx", order=3)
        Skill.objects.create(category=devops, name="SSH & Terminal", order=4)

        # Others
        others = SkillCategory.objects.create(name="Diğer Yetenekler", icon="🌐", order=4)
        Skill.objects.create(category=others, name="Problem Çözme", order=1)
        Skill.objects.create(category=others, name="Liderlik", order=2)
        Skill.objects.create(category=others, name="İngilizce (A2)", order=3)
        Skill.objects.create(category=others, name="Almanca (A2)", order=4)

    # 3. Experience
    if not Experience.objects.exists():
        print("Creating Experience...")
        Experience.objects.create(
            job_title="Freelance Yazılım Geliştirici",
            company="",
            date_range="2014 - Günümüz",
            description="Müşteri taleplerine göre web ve masaüstü uygulamaları geliştirme. Mevcut yazılımlarda performans iyileştirmesi.",
            order=1
        )
        Experience.objects.create(
            job_title="Yazılım Desteği & Eğitim",
            company="Datakod & METADATA Yazılım",
            date_range="2016 - 2017",
            description="Satılan yazılımlar için teknik destek ve SQL ile özel raporlama sistemleri geliştirme.",
            order=2
        )
        Experience.objects.create(
            job_title="Donanım & Yazılım Teknikeri",
            company="Midyat Bilişim",
            date_range="2013 - 2014",
            description="Teknik servis ve yazılım kurulum hizmetleri.",
            order=3
        )
        Experience.objects.create(
            job_title="Stajyer",
            company="Çözüm Bilişim",
            date_range="Şubat 2014",
            description="WordPress, Drupal, Magento kurulum ve desteği.",
            order=4
        )
        Experience.objects.create(
            job_title="Satış & Yazılım Desteği",
            company="Baran Bilgisayar",
            date_range="2010 - 2011",
            description="İlk iş deneyimim: müşteri ilişkileri ve temel teknik destek.",
            order=5
        )

    # 4. Contact
    if not ContactInfo.objects.exists():
        print("Creating Contact Info...")
        ContactInfo.objects.create(
            title="Telefon",
            icon="📞",
            value="+90 537 512 3099",
            link="tel:+905375123099",
            order=1
        )
        ContactInfo.objects.create(
            title="E-posta",
            icon="✉️",
            value="mracengiz@gmail.com",
            link="mailto:mracengiz@gmail.com",
            order=2
        )
        ContactInfo.objects.create(
            title="Konum",
            icon="📍",
            value="Mardin, Türkiye",
            link="",
            order=3
        )

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()
