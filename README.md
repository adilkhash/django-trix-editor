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
If you want to handle attachments, you need to add the following code to your `urls.py`:

```python
urlpatterns = [
    ...
    path('trix-editor/', include('trix_editor.urls')),
    ...
]
```
