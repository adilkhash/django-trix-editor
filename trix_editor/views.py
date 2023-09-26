from http import HTTPStatus

from django.views.decorators.http import require_POST
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings


def requires_permission(view_func):
    def wrapper(request, *args, **kwargs):
        if permission := getattr(settings, 'TRIX_UPLOAD_PERMISSION', None):
            if not request.user.has_perm(permission):
                return JsonResponse(
                    {'error': 'You do not have permission to upload attachments.'},
                    status=HTTPStatus.FORBIDDEN,
                )
        return view_func(request, *args, **kwargs)
    return wrapper


@requires_permission
@require_POST
def handle_upload(request):
    file = request.FILES.get('file')
    filename = default_storage.save(file.name, file)
    return JsonResponse({'attachment_url': default_storage.url(filename)})
