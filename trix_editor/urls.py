from django.urls import path

from trix_editor.views import handle_upload


urlpatterns = [
    path('upload/', handle_upload, name='upload'),
]
