function previewImage(event) {
    const input = event.target;
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imagePreview = document.getElementById('image-preview');
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview" style="max-width: 300px;">`;
        }
        reader.readAsDataURL(input.files[0]);
    }
}
