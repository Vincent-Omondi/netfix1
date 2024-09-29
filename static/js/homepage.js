// static/js/homepage.js

document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const servicesDropdown = document.querySelector('.services-dropdown');

    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
    });

    servicesDropdown.addEventListener('click', function(e) {
        if (window.innerWidth <= 768) {
            if (e.target === this.querySelector('.dropdown-toggle')) {
                e.preventDefault();
                this.classList.toggle('active');
            } else if (e.target.classList.contains('mobile-only')) {
                // Allow the "All in One" link to work without preventing default
                this.classList.remove('active');
                navLinks.classList.remove('active');
            }
        }
    });

    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
        navLinks.classList.remove('active');
        servicesDropdown.classList.remove('active');
        }
    });
});