document.addEventListener('DOMContentLoaded', function() {
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



// document.getElementById('rate-form').addEventListener('submit', function(e) {
//   e.preventDefault();
//   const form = e.target;
//   const formData = new FormData(form);
  
//   fetch(form.action, {
//       method: 'POST',
//       body: formData,
//       headers: {
//           'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
//       }
//   })
//   .then(response => response.json())
//   .then(data => {
//       if (data.success) {
//           alert('Rating submitted successfully! New average rating: ' + data.average_rating);
//       } else {
//           alert('Error submitting rating: ' + data.error);
//       }
//   });
// });