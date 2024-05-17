function previewImage(event) {
    const input = event.target;
    if (input.files?.[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imagePreview = document.getElementById('image-preview');

            const imgSrc = e.target.result;
            if (typeof imgSrc === 'string') {
                imagePreview.innerHTML = `<img src="${imgSrc}" alt="Image Preview" style="max-height: 20rem;">`;
            } else {
                console.error('FileReader result is not a string:', result);
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}
