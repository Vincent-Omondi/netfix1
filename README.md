<html><head><base href="https://readme-netfix.com/" />
<style>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: #333;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f4;
}

h1, h2, h3 {
  color: #2c3e50;
}

h1 {
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 30px;
  text-transform: uppercase;
  letter-spacing: 2px;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
}

h2 {
  font-size: 1.8em;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #e74c3c;
  padding-left: 10px;
}

h3 {
  font-size: 1.3em;
  margin-top: 25px;
  margin-bottom: 10px;
  color: #16a085;
}

p, ul, ol {
  margin-bottom: 15px;
}

ul, ol {
  padding-left: 30px;
}

li {
  margin-bottom: 5px;
}

code {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 3px;
  font-family: Consolas, Monaco, 'Andale Mono', monospace;
  font-size: 0.9em;
  padding: 2px 4px;
}

pre {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 10px;
  overflow-x: auto;
}

a {
  color: #3498db;
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: #2980b9;
  text-decoration: underline;
}

.highlight {
  background-color: #ffffd0;
  padding: 2px 4px;
  border-radius: 3px;
}

.button {
  display: inline-block;
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #2980b9;
}

.note {
  background-color: #e8f4f8;
  border-left: 4px solid #3498db;
  padding: 10px;
  margin-bottom: 15px;
}

.warning {
  background-color: #fff5f5;
  border-left: 4px solid #e74c3c;
  padding: 10px;
  margin-bottom: 15px;
}

@media (max-width: 600px) {
  body {
    padding: 10px;
  }
  
  h1 {
    font-size: 2em;
  }
  
  h2 {
    font-size: 1.5em;
  }
  
  h3 {
    font-size: 1.2em;
  }
}
</style>
</head>
<body>

<h1>Netfix: Service Request Platform</h1>

<div class="note">
  <strong>Note:</strong> This website is currently under development. Many features have been implemented, but some are still in progress.
</div>

<h2>Project Overview</h2>

<p>Netfix is a web platform designed to connect customers with companies that offer home services. From fixing household items like bidets to cleaning and painting services, this site serves as a one-stop shop for various service needs. Developed using the Django framework, this project offers a robust and scalable platform for managing services, companies, and customer requests.</p>

<h2>Key Objectives</h2>

<p>The primary goal of Netfix is to provide a platform where:</p>

<ul>
  <li>Companies can list the services they offer.</li>
  <li>Customers can browse and request these services.</li>
  <li>Both companies and customers can register, manage their profiles, and interact with the services provided.</li>
</ul>

<h2>Features</h2>

<h3>User Roles</h3>

<ul>
  <li><strong>Company Users:</strong> Can create services specific to their field of work.</li>
  <li><strong>Customer Users:</strong> Can browse, request services, and manage service requests.</li>
</ul>

<h3>User Registration</h3>

<ul>
  <li><strong>Customer Registration:</strong> Requires email, password, username, and date of birth.</li>
  <li><strong>Company Registration:</strong> Requires email, password, username, and field of work.</li>
  <li>Both user types must have unique email addresses and usernames, with real-time validation during registration.</li>
</ul>

<h3>User Profiles</h3>

<ul>
  <li><strong>Customer Profile:</strong> Displays personal information and a list of previously requested services.</li>
  <li><strong>Company Profile:</strong> Shows company details and all services offered by that company.</li>
</ul>

<h3>Services</h3>

<p>Companies can create and list services within their field of expertise.</p>

<p>Available service fields:</p>
<ul>
  <li>Air Conditioner</li>
  <li>Carpentry</li>
  <li>Electricity</li>
  <li>Gardening</li>
  <li>Home Machines</li>
  <li>Housekeeping</li>
  <li>Interior Design</li>
  <li>Locks</li>
  <li>Painting</li>
  <li>Plumbing</li>
  <li>Water Heaters</li>
  <li>All in One (companies can offer services in all fields except the "All in One" field itself)</li>
</ul>

<p>Each service includes:</p>
<ul>
  <li>Name</li>
  <li>Description</li>
  <li>Field (from the predefined list)</li>
  <li>Price per hour</li>
  <li>Creation date (automatically set when a service is created)</li>
</ul>

<h3>Service Requesting</h3>

<ul>
  <li>Customers can request services by specifying:
    <ul>
      <li>Address for service</li>
      <li>Duration of the service in hours</li>
    </ul>
  </li>
  <li>Once requested, the service is added to the customer's profile, showing relevant details such as service cost, service date, and company name.</li>
</ul>

<h3>Service Browsing</h3>

<ul>
  <li><strong>Popular Services:</strong> A page displays the most frequently requested services.</li>
  <li><strong>Newest Services:</strong> A page lists all services in reverse chronological order.</li>
  <li><strong>Category Pages:</strong> Dedicated pages for each service field (e.g., Plumbing, Housekeeping), showcasing the available services.</li>
</ul>

<h3>Individual Service Pages</h3>

<p>Each service has its own page, showing:</p>
<ul>
  <li>Service details</li>
  <li>Company information</li>
  <li>The ability to navigate to the company profile to view all services offered by that company.</li>
</ul>

<h3>Bonus Features</h3>

<ul>
  <li><strong>Rating System:</strong> Customers can rate services they have requested, offering feedback for others.</li>
  <li><strong>Pagination:</strong> Service listings are paginated to improve navigation across multiple pages of services.</li>
  <li><strong>Custom Design:</strong> Modify the existing CSS and HTML to create a personalized look for the platform.</li>
</ul>

<h2>Installation and Setup</h2>

<p>To set up and run the project, follow these steps:</p>

<h3>Prerequisites</h3>

<ul>
  <li>Python 3.6+</li>
  <li>Django 3.1.14 (or compatible version)</li>
  <li>pip for installing dependencies</li>
</ul>

<h3>Installation Steps</h3>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/Vincent-Omondi/netfix1.git
cd netfix1</code></pre>
  </li>
  <li>Create a virtual environment:
    <pre><code>python3 -m venv venv
source venv/bin/activate  # For Unix/Linux
venv\Scripts\activate  # For Windows</code></pre>
  </li>
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Apply migrations to set up the database:
    <pre><code>python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
  </li>
  <li>Create a superuser to access the Django admin panel:
    <pre><code>python3 manage.py createsuperuser</code></pre>
  </li>
  <li>Run the development server:
    <pre><code>python3 manage.py runserver</code></pre>
  </li>
  <li>Visit <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> to access the platform.</li>
</ol>

<h3>Troubleshooting</h3>

<p>If you encounter any issues while running the project, ensure that you are using Django v3.1.14. You can verify your Django version with:</p>

<pre><code>python3 -m django --version</code></pre>

<p>If your version does not match, install the correct version using:</p>

<pre><code>pip install django==3.1.14</code></pre>

<h2>Project Structure</h2>

<ul>
  <li><strong>netfix/:</strong> Main project directory</li>
  <li><strong>users/:</strong> Handles user registration, login, and profiles.
    <ul>
      <li><code>views.py</code>: Manages user views like profile, login, registration.</li>
      <li><code>urls.py</code>: Defines URL patterns for the user-related views.</li>
      <li><code>templates/users/</code>: Contains HTML templates for user-related pages.</li>
    </ul>
  </li>
  <li><strong>services/:</strong> Manages service creation, listing, and details.
    <ul>
      <li><code>views.py</code>: Handles the creation, display, and management of services.</li>
      <li><code>urls.py</code>: Defines URL patterns for service-related views.</li>
      <li><code>templates/services/</code>: HTML templates for service-related pages.</li>
    </ul>
  </li>
  <li><strong>main/:</strong> General project management (home page, navigation, common features).
    <ul>
      <li><code>views.py</code>: Manages views for the home page, navigation, etc.</li>
      <li><code>urls.py</code>: URL patterns for common pages.</li>
    </ul>
  </li>
</ul>

<h2>Commands Overview</h2>

<ul>
  <li>Run the server:
    <pre><code>python3 manage.py runserver</code></pre>
  </li>
  <li>Create a new app:
    <pre><code>python3 manage.py startapp &lt;app_name&gt;</code></pre>
  </li>
  <li>Create a superuser for admin access:
    <pre><code>python3 manage.py createsuperuser</code></pre>
  </li>
  <li>Database migrations:
    <pre><code>python3 manage.py makemigrations
python3 manage.py migrate</code></pre>
  </li>
</ul>

<h2>Contribution Guidelines</h2>

<ol>
  <li>Fork the repository and clone your fork.</li>
  <li>Create a new branch for your feature or bug fix:
    <pre><code>git checkout -b feature-branch</code></pre>
  </li>
  <li>Commit your changes and push to your fork:
    <pre><code>git commit -m "Description of changes"
git push origin feature-branch</code></pre>
  </li>
  <li>Submit a pull request to the main repository.</li>
</ol>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

<h2>Contact</h2>

<p>For questions or support, please contact the project maintainer at <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>

<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Add smooth scrolling to all links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();

      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Add hover effect to buttons
  const buttons = document.querySelectorAll('.button');
  buttons.forEach(button => {
    button.addEventListener('mouseover', () => {
      button.style.transform = 'scale(1.05)';
    });
    button.addEventListener('mouseout', () => {
      button.style.transform = 'scale(1)';
    });
  });

  // Add a back-to-top button
  const backToTopButton = document.createElement('a');
  backToTopButton.href = '#';
  backToTopButton.classList.add('button');
  backToTopButton.style.position = 'fixed';
  backToTopButton.style.bottom = '20px';
  backToTopButton.style.right = '20px';
  backToTopButton.style.display = 'none';
  backToTopButton.textContent = 'Back to Top';

  document.body.appendChild(backToTopButton);

  window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
      backToTopButton.style.display = 'block';
    } else {
      backToTopButton.style.display = 'none';
    }
  });

  backToTopButton.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});
</script>
</body></html>