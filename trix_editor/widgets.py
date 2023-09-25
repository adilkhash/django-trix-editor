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
class JSCode:
    def __str__(self):
        return (
            """
            <script>
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


@html_safe
class CSSPath:
    def __str__(self):
        return (
            f'<link rel="stylesheet" href="https://unpkg.com/trix@{TRIX_VERSION}/dist/trix.css">'
        )


class TrixEditorWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['hidden'] = True
        html = super().render(name, value, attrs=attrs, renderer=renderer)
        return f'{html}<trix-editor input="{attrs["id"]}"></trix-editor>'

    class Media:
        js = [JSPath(), JSCode()]
        css = {
            'all': [CSSPath()],
        }
