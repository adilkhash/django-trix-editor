from django.db import models
from trix_editor.widgets import TrixEditorWidget


class TrixEditorField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = TrixEditorWidget
        return super().formfield(**kwargs)
