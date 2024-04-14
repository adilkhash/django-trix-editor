from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

TRIX_VERSION = getattr(settings, 'TRIX_VERSION', '2.1.0')
TRIX_FIELD_NAME = getattr(settings, 'TRIX_FIELD_NAME', 'description')


class JSPath:
    def __html__(self):
        return (
            f'<script type="text/javascript" src="//unpkg.com/trix@{TRIX_VERSION}/dist/trix.umd.min.js"></script>'
        )


class JSCode:
    def __html__(self):
        return (
            """
            <script type="text/javascript">
                function getCookie(name) {
                    let cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        const cookies = document.cookie.split(';');
                        for (let i = 0; i < cookies.length; i++) {
                            let cookie = cookies[i].trim();
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }

                addEventListener("trix-attachment-add", function (event) {
                    if (event.attachment.file) {
                        handleUpload(event.attachment)
                    }
                })

                function handleUpload(attachment) {
                    uploadFile(attachment.file, setProgress, setAttributes)
                
                    function setProgress(progress) {
                        attachment.setUploadProgress(progress)
                    }
                
                    function setAttributes(attributes) {
                        attachment.setAttributes(attributes)
                    }
                }

                function uploadFile(file, progressCallback, successCallback) {
                    var formData = new FormData()
                    var xhr = new XMLHttpRequest()
                    formData.append("Content-Type", file.type)
                    formData.append("file", file)
                    xhr.open("POST", "/trix-editor/upload/", true)
                    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
                    xhr.upload.addEventListener("progress", function (event) {
                        progressCallback(event.loaded / event.total * 100)
                    })
                    xhr.addEventListener("load", function (event) {
                        if (xhr.status === 200) {
                            let attributes = {
                                url: JSON.parse(xhr.responseText).attachment_url
                            }
                            successCallback(attributes)
                        }
                    })
                    xhr.send(formData)
                }
            </script>
            """
        )


class CSSPath:
    def __html__(self):
        return (
            f'<link rel="stylesheet" href="https://unpkg.com/trix@{TRIX_VERSION}/dist/trix.css">'
        )


class CSSAdminCode:
    def __html__(self):
        return (
            f"""
            <style>
                div.field-{TRIX_FIELD_NAME} div.flex-container {{
                    display: block;
                }}
            </style>
            """
        )


class TrixEditorWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['hidden'] = True
        html = super().render(name, value, attrs=attrs, renderer=renderer)
        return mark_safe(f'{html}<trix-editor input="{attrs["id"]}"></trix-editor>')

    class Media:
        js = [
            JSCode(),
            JSPath(),
        ]
        css = {
            'all': [CSSAdminCode(), CSSPath()],
        }
