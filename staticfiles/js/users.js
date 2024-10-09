document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.registration-form');
    const inputs = form.querySelectorAll('input, select');

    form.addEventListener('submit', function(e) {
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                showError(input, `${input.previousElementSibling.textContent} is required`);
                isValid = false;
            } else {
                clearError(input);
            }
        });

        if (!isValid) {
            e.preventDefault();
        }
    });

    function showError(input, message) {
        let errorElement = input.nextElementSibling;
        if (!errorElement || !errorElement.classList.contains('error-message')) {
            errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            input.parentNode.insertBefore(errorElement, input.nextSibling);
        }
        errorElement.textContent = message;
    }

    function clearError(input) {
        const errorElement = input.nextElementSibling;
        if (errorElement && errorElement.classList.contains('error-message')) {
            errorElement.remove();
        }
    }
});