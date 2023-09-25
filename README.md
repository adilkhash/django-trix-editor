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

Don't forget to add the `trix_editor` urls to your `urls.py`:
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

Or customize your forms using the widget `TrixEditorWidget`:

```python
from django import forms
from trix_editor.widgets import TrixEditorWidget

class MyForm(forms.Form):
    content = forms.CharField(widget=TrixEditorWidget())
```
