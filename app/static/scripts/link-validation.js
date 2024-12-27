function validateYouTubeUrl() {
    const urlInput = document.getElementById('videoUrl');

    const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)([A-Za-z0-9_-]{11})(.*)?$/;

    if (!youtubeRegex.test(urlInput.value)) {
        urlInput.value = '';
        urlInput.placeholder = 'Please enter a valid YouTube URL';
        urlInput.classList.add('error-placeholder');
        return false;
    } else {
        document.getElementById('loader').style.display = 'flex';
        return true;
    }
}