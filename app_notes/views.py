import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from app_notes.forms import UploadFileForm
from app_notes.models import UploadFile

logger = logging.getLogger(__name__)


# Create your views here.

@require_POST
@csrf_exempt
def upload_file(request):
    form = UploadFileForm(data=request.POST, files=request.FILES)
    location = 'upload failed'
    if form.is_valid():
        file = request.FILES['file']
        cls = file.content_type
        cls_prefix_map_path = {
            'image/': 'image/',
            'video/': 'video/',
        }
        upload_path = None
        for prefix, path in cls_prefix_map_path.items():
            if cls.startswith(prefix):
                upload_path = path
                break
        if upload_path:
            instance = UploadFile(file=file, name=file.name, cls=cls, size=file.size)
            instance.file.field.upload_to = upload_path
            instance.save()
            location = instance.file.url

    return JsonResponse(dict(location=location))
