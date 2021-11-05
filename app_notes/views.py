import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from app_notes.forms import UploadFileForm
from app_notes.models import UploadFile

logger = logging.getLogger(__name__)


# Create your views here.


def check_upload_file(file):
    """
    检查上传文件是否合法
    :return:
    """
    result = None
    # 文件大小不能超过10M
    if file.size / 1024 / 1024 > 10:
        result = '文件大小不能超过10M'

    return result


@require_POST
@csrf_exempt
def upload_file(request):
    form = UploadFileForm(data=request.POST, files=request.FILES)
    location = None
    if form.is_valid():
        file = request.FILES['file']

        result = check_upload_file(file)
        if result:
            return JsonResponse(dict(error=result))

        cls = file.content_type
        cls_prefix_map_path = {
            'image/': 'image/%Y%m%d/',
            'video/': 'video/%Y%m%d/',
        }
        upload_to = None
        for prefix, path in cls_prefix_map_path.items():
            if cls.startswith(prefix):
                upload_to = path
                break
        if upload_to:
            instance = UploadFile(file=file, name=file.name, cls=cls, size=file.size)
            instance.file.field.upload_to = upload_to
            instance.save()
            location = instance.file.url

    return JsonResponse(dict(location=location))
