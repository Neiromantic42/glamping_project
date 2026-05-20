// =========================================================
// Открытие/закрытие формы отзыва
// =========================================================
const openFormBtn = document.getElementById('openReviewForm');
const closeFormBtn = document.getElementById('closeReviewForm');
const reviewFormCard = document.getElementById('reviewFormCard');

if (openFormBtn) {
    openFormBtn.addEventListener('click', () => {
        reviewFormCard.style.display = 'block';
        reviewFormCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
}

if (closeFormBtn) {
    closeFormBtn.addEventListener('click', () => {
        reviewFormCard.style.display = 'none';
    });
}

// =========================================================
// Счетчик символов
// =========================================================
const textarea = document.getElementById('text');
const charCount = document.getElementById('charCount');

if (textarea && charCount) {
    textarea.addEventListener('input', () => {
        charCount.textContent = textarea.value.length;
    });
}

// =========================================================
// Превью загруженных изображений
// =========================================================
const imageInput = document.getElementById('images');
const imagePreviews = document.getElementById('imagePreviews');

if (imageInput && imagePreviews) {
    imageInput.addEventListener('change', (e) => {
        imagePreviews.innerHTML = '';
        const files = Array.from(e.target.files);

        files.forEach(file => {
            const reader = new FileReader();
            reader.onload = (event) => {
                const img = document.createElement('img');
                img.src = event.target.result;
                imagePreviews.appendChild(img);
            };
            reader.readAsDataURL(file);
        });
    });
}

// =========================================================
// Кнопка "Показать целиком"
// =========================================================
document.querySelectorAll('.btn-show-more').forEach(button => {
    button.addEventListener('click', function() {
        const textContent = this.previousElementSibling;
        const fullText = textContent.getAttribute('data-full');

        textContent.textContent = fullText;
        this.style.display = 'none';
    });
});

// =========================================================
// Настройки Lightbox
// =========================================================
if (typeof lightbox !== 'undefined') {
    lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true,
        'albumLabel': 'Фото %1 из %2'
    });
}