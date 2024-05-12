function previewImage(event) {
    const input = event.target;
    if (input.files?.[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imagePreview = document.getElementById('image-preview');
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Image Preview" style="max-height: 20rem;">`;
        };
        reader.readAsDataURL(input.files[0]);
    }
}
