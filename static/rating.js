// static/rating.js

document.addEventListener('DOMContentLoaded', function() {
    const starContainer = document.getElementById('star-container');
    const ratingInput = document.getElementById('rating-input');
    const rateForm = document.getElementById('rate-form');
    const starCount = 5;
    let isDragging = false;
    let currentRating = parseFloat(ratingInput.value) || 0;

    function createStar(index) {
        const star = document.createElement('div');
        star.classList.add('star');
        star.innerHTML = '★';
        star.dataset.index = index + 1;

        const starFill = document.createElement('div');
        starFill.classList.add('star-fill');
        starFill.innerHTML = '★';
        star.appendChild(starFill);

        return star;
    }

    function updateStars(rating) {
        const stars = starContainer.children;
        for (let i = 0; i < stars.length; i++) {
            const starFill = stars[i].querySelector('.star-fill');
            if (i < Math.floor(rating)) {
                starFill.style.width = '100%';
            } else if (i === Math.floor(rating)) {
                starFill.style.width = `${(rating % 1) * 100}%`;
            } else {
                starFill.style.width = '0';
            }
        }
    }

    function calculateRating(event) {
        const containerRect = starContainer.getBoundingClientRect();
        const x = event.clientX - containerRect.left;
        let rating = (x / containerRect.width) * starCount;
        rating = Math.max(0, Math.min(starCount, rating));
        return Math.round(rating * 10) / 10; // Round to nearest 0.1
    }

    function handleStarEvent(event) {
        const rating = calculateRating(event);
        updateStars(rating);
        currentRating = rating;
        ratingInput.value = rating;
    }

    function submitRating() {
        ratingInput.value = currentRating.toFixed(1);
        
        const formData = new FormData(rateForm);
        fetch(rateForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Rating submitted successfully');
                // You might want to update the UI here, e.g., show a success message
                // or update the displayed average rating
                updateStars(data.new_rating);
            } else {
                console.error('Error submitting rating:', data.error);
                // You might want to show an error message to the user here
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // You might want to show a generic error message to the user here
        });
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Create stars
    for (let i = 0; i < starCount; i++) {
        starContainer.appendChild(createStar(i));
    }

    // Event listeners
    starContainer.addEventListener('mousedown', (e) => {
        isDragging = true;
        handleStarEvent(e);
    });

    starContainer.addEventListener('mousemove', (e) => {
        if (isDragging) {
            handleStarEvent(e);
        }
    });

    starContainer.addEventListener('mouseup', () => {
        isDragging = false;
        submitRating();
    });

    starContainer.addEventListener('mouseleave', () => {
        if (isDragging) {
            isDragging = false;
            submitRating();
        }
    });

    starContainer.addEventListener('touchstart', (e) => {
        isDragging = true;
        handleStarEvent(e.touches[0]);
    });

    starContainer.addEventListener('touchmove', (e) => {
        if (isDragging) {
            e.preventDefault();
            handleStarEvent(e.touches[0]);
        }
    });

    starContainer.addEventListener('touchend', () => {
        isDragging = false;
        submitRating();
    });

    // Initial star update
    updateStars(currentRating);
});
