from django.shortcuts import render
from django.http import FileResponse, Http404
import os
from django.conf import settings
from pathlib import Path
from .models import Profile, SkillCategory, Experience, ContactInfo


def index(request):
    """Ana sayfa görünümü"""
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    experiences = Experience.objects.all()
    contact_infos = ContactInfo.objects.all()
    
    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'contact_infos': contact_infos,
    }
    return render(request, 'cv_app/index.html', context)


def download_cv(request):
    """CV PDF dosyasını indirmek için görünüm"""
    cv_path = Path(settings.MEDIA_ROOT) / 'cv.pdf'
    if cv_path.exists():
        return FileResponse(
            open(cv_path, 'rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename='Murat_Cengiz_CV.pdf'
        )
    else:
        raise Http404("CV dosyası bulunamadı")
