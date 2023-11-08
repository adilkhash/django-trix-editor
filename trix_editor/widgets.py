from django import forms
from django.utils.safestring import mark_safe


class TrixEditorWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['hidden'] = True
        html = super().render(name, value, attrs=attrs, renderer=renderer)
        return mark_safe(f'{html}<trix-editor input="{attrs["id"]}"></trix-editor>')

    class Media:
        js = ['admin/js/jquery.init.js', 'trix_editor/trix.min.js', 'trix_editor/trix.upload.js']
        css = {
            'all': ['trix_editor/trix.css'],
        }
