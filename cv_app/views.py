from django.shortcuts import render
from django.http import FileResponse, Http404
import os
from django.conf import settings
from pathlib import Path


def index(request):
    """Ana sayfa görünümü"""
    return render(request, 'cv_app/index.html')


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
