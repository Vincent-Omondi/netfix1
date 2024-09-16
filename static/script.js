document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.querySelector('.search-bar input');
    const searchButton = document.querySelector('.search-bar button');

    searchButton.addEventListener('click', function() {
      const searchTerm = searchBar.value.trim();
      if (searchTerm) {
        alert(`Searching for: ${searchTerm}`);
        // Here you would typically redirect to a search results page
        // window.location.href = `/search?q=${encodeURIComponent(searchTerm)}`;
      }
    });

    // Enable search on Enter key press
    searchBar.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        searchButton.click();
      }
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
});


let currentPosition = 0;
const taskGrid = document.getElementById('taskGrid');
const taskItems = document.querySelectorAll('.task-item');
const itemWidth = 330; // 300px width + 30px margin-right

function slideServices(direction) {
    const maxPosition = (taskItems.length - 3) * itemWidth;
    currentPosition += direction * itemWidth;
    
    if (currentPosition < 0) currentPosition = 0;
    if (currentPosition > maxPosition) currentPosition = maxPosition;

    taskGrid.style.transform = `translateX(-${currentPosition}px)`;
}

// Optional: Auto-slide every 5 seconds
// setInterval(() => {
//     slideServices(1);
// }, 5000);

document.getElementById('rate-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  
  fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: {
          'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert('Rating submitted successfully! New average rating: ' + data.average_rating);
      } else {
          alert('Error submitting rating: ' + data.error);
      }
  });
});