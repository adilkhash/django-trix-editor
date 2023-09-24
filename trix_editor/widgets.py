from django import forms
from django.utils.html import html_safe
from django.conf import settings

TRIX_VERSION = getattr(settings, 'TRIX_VERSION', '2.0.6')


@html_safe
class JSPath:
    def __str__(self):
        return (
            f'<script src="https://unpkg.com/trix@{TRIX_VERSION}/dist/trix.umd.min.js" rel="stylesheet">'
        )


@html_safe
class CSSPath:
    def __str__(self):
        return (
            f'<link rel="stylesheet" href="https://unpkg.com/trix@{TRIX_VERSION}/dist/trix.css">'
        )


class Trix2Widget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['hidden'] = True
        html = super().render(name, value, attrs=attrs, renderer=renderer)
        return f'{html}<trix-editor input="{attrs["id"]}"></trix-editor>'

    class Media:
        js = [JSPath()]
        css = {
            'all': [CSSPath()],
        }
