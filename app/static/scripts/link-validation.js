function validateYouTubeUrl() {
    const urlInput = document.getElementById('videoUrl');

    const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)([A-Za-z0-9_-]{11})(.*)?$/;

    if (!youtubeRegex.test(urlInput.value)) {
        urlInput.value = ''; // Очистити поле введення
        urlInput.placeholder = 'Please enter a valid YouTube URL'; // Змінити placeholder
        urlInput.classList.add('error-placeholder'); // Додати стиль помилки (опціонально)
        return false; // Зупинити відправку форми
    }

    errorMessage.style.display = 'none';
    document.querySelector('form').addEventListener('submit', function () {
        document.getElementById('loader').style.display = 'flex';
    });
    return true;
}