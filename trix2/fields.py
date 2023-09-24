from django.db import models
from trix2.widgets import Trix2Widget


class Trix2Field(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = Trix2Widget
        return super().formfield(**kwargs)
