from django.views.decorators.http import require_POST
from django.http.response import JsonResponse
from django.core.files.storage import default_storage


@require_POST
def handle_upload(request):
    file = request.FILES.get("file")
    filename = default_storage.save(file.name, file)
    return JsonResponse({"attachment_url": default_storage.url(filename)})
