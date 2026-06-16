/**
 * ═══════════════════════════════════════════════════════════════════════
 * ЛОГИКА СТРАНИЦЫ КИНОТЕАТРА
 *
 * Функциональность:
 * - Счетчик символов в textarea
 * - Валидация формы
 * - Отправка данных
 * ═══════════════════════════════════════════════════════════════════════
 */

document.addEventListener('DOMContentLoaded', function() {

    /* ─────────────────────────────────────────────────────────
       1. СЧЕТЧИК СИМВОЛОВ В TEXTAREA
       ───────────────────────────────────────────────────────── */
    const commentsTextarea = document.getElementById('comments');
    const charCountSpan = document.getElementById('charCount');

    if (commentsTextarea && charCountSpan) {
        commentsTextarea.addEventListener('input', function() {
            charCountSpan.textContent = this.value.length;
        });
    }

    /* ─────────────────────────────────────────────────────────
       2. ВАЛИДАЦИЯ И ОТПРАВКА ФОРМЫ
       ───────────────────────────────────────────────────────── */
    const bookingForm = document.getElementById('cinemaBookingForm');

    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            // Форма автоматически валидируется браузером
            // thanks to HTML5 validation attributes (required, type, etc.)
            console.log('Форма отправлена!');
        });
    }

    /* ─────────────────────────────────────────────────────────
       3. ПЛАВНАЯ ПРОКРУТКА К ФОРМЕ (опционально)
       ───────────────────────────────────────────────────────── */
    const cinemaBookingForm = document.querySelector('.booking-form-wrapper');

    // Можно добавить кнопку для прокрутки к форме
    window.scrollToBookingForm = function() {
        if (cinemaBookingForm) {
            cinemaBookingForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    };
});
