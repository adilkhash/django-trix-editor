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