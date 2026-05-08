import json
from pathlib import Path

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils.text import get_valid_filename
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from TableVisualiser.logic.pixelizer import update_image, import_image, clear

import os
import uuid

from TableVisualiser.logic.strip import get_strip

UPLOADS_DIR = os.path.join(settings.MEDIA_ROOT, 'uploads')
DEFAULT_BRIGHTNESS = 0.25  # 0.0 (off) to 1.0 (full)

def _get_latest_images(limit=10):
    if not os.path.isdir(UPLOADS_DIR):
        return []

    entries = []
    for name in os.listdir(UPLOADS_DIR):
        path = os.path.join(UPLOADS_DIR, name)
        if os.path.isfile(path):
            entries.append((name, os.path.getmtime(path)))

    entries.sort(key=lambda item: item[1], reverse=True)
    return [f'{settings.MEDIA_URL}uploads/{name}' for name, _ in entries[:limit]]


def homepage(request):
    return render(request, 'index.html', {'gallery_images': _get_latest_images()})


def upload_image(request):
    if request.method != 'POST' or 'image' not in request.FILES:
        return render(request, 'index.html', {
            'error': 'No file uploaded.',
            'gallery_images': _get_latest_images(),
        })

    upload = request.FILES['image']
    safe_name = get_valid_filename(upload.name)
    name_root, ext = os.path.splitext(safe_name)
    filename = f'{name_root}-{uuid.uuid4().hex}{ext}'

    storage = FileSystemStorage(location=UPLOADS_DIR)
    saved_name = storage.save(filename, upload)
    image_url = f'{settings.MEDIA_URL}uploads/{saved_name}'

    return render(request, 'index.html', {
        'image_url': image_url,
        'gallery_images': _get_latest_images(),
    })


@csrf_exempt
def update_image_backend(request):
    data = json.loads(request.body)
    image_src = data.get('image')
    print(image_src)
    if not image_src:
        return JsonResponse({'error': 'Missing image'}, status=400)

    print(settings.BASE_DIR)
    image_path = Path(settings.BASE_DIR) / Path(image_src.lstrip("/"))
    print(image_path)
    strip = get_strip()
    update_image(image_path, strip)

    return JsonResponse({'status': 'ok'})

def clear_image_backend(request):
    data = json.loads(request.body)
    instruction = data.get('instruction')
    if instruction == 'clear':
        strip = get_strip()
        clear(strip)
    else:
        return JsonResponse({'error': 'Invalid instruction'}, status=400)

    return JsonResponse({'status': 'ok'})
