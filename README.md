# Django Trix Editor Integration

This package provides a Django app that integrates the [Trix editor](https://trix-editor.org/) with your Django project.

## Installation

Install the package with pip:

```bash
pip install django-trix-editor
```

To change the version of Trix that is used, you can specify the version in your `settings.py`:

```python
TRIX_VERSION = '2.0.0'
```

## Usage
To use this package, you need to add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'trix_editor',
    ...
]
```

Don't forget to add the `trix_editor` urls to your `urls.py` to handle attachments:
```python

from django.urls import include, path

urlpatterns = [
    ...
    path('trix-editor/', include('trix_editor.urls')),
    ...
]
```

You can use the `TrixEditorField` in your models:

```python
from django.db import models
from trix_editor.fields import TrixEditorField

class MyModel(models.Model):
    content = TrixEditorField()
```


## Templates and forms

Customize your forms to use the widget `TrixEditorWidget`:

```python
from django import forms
from trix_editor.widgets import TrixEditorWidget

class MyForm(forms.Form):
    content = forms.CharField(widget=TrixEditorWidget())
```

But don't forget to include the following statements to your template to load the Trix editor assets:

```html
...
<head>
    <meta charset="utf-8">
    <title></title>
    ...
    {{ form.media.css }}
</head>
...
<!-- footer -->
{{ form.media.js }}
```

## Django Admin Integration
To use the Trix editor in the Django admin, you need to add the following to your `admin.py`:

```python
from django.contrib import admin
from django import forms

from trix_editor.widgets import TrixEditorWidget

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ["title", "content", "status"]
        widgets = {
            "content": TrixEditorWidget(),
        }

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created", "updated")
    form = ContentForm
```
