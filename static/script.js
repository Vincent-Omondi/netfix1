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
