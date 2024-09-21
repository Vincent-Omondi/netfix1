# Netfix: Service Request Platform

> **Note:** This website is currently under development. Many features have been implemented, but some are still in progress.

## Project Overview

Netfix is a web platform designed to connect customers with companies that offer home services. From fixing household items like bidets to cleaning and painting services, this site serves as a one-stop shop for various service needs. Developed using the Django framework, this project offers a robust and scalable platform for managing services, companies, and customer requests.

## Key Objectives

The primary goal of Netfix is to provide a platform where:

- Companies can list the services they offer.
- Customers can browse and request these services.
- Both companies and customers can register, manage their profiles, and interact with the services provided.

## Features

### User Roles

- **Company Users:** Can create services specific to their field of work.
- **Customer Users:** Can browse, request services, and manage service requests.

### User Registration

- **Customer Registration:** Requires email, password, username, and date of birth.
- **Company Registration:** Requires email, password, username, and field of work.
- Both user types must have unique email addresses and usernames, with real-time validation during registration.

### User Profiles

- **Customer Profile:** Displays personal information and a list of previously requested services.
- **Company Profile:** Shows company details and all services offered by that company.

### Services

Companies can create and list services within their field of expertise.

Available service fields:
- Air Conditioner
- Carpentry
- Electricity
- Gardening
- Home Machines
- Housekeeping
- Interior Design
- Locks
- Painting
- Plumbing
- Water Heaters
- All in One (companies can offer services in all fields except the field itself)

Each service includes:
- Name
- Description
- Field (from the predefined list)
- Price per hour
- Creation date (automatically set when a service is created)

### Service Requesting

- Customers can request services by specifying:
  - Address for service
  - Duration of the service in hours
- Once requested, the service is added to the customer's profile, showing relevant details such as service cost, service date, and company name.

### Service Browsing

- **Popular Services:** A page displays the most frequently requested services.
- **Newest Services:** A page lists all services in reverse chronological order.
- **Category Pages:** Dedicated pages for each service field (e.g., Plumbing, Housekeeping), showcasing the available services.

### Individual Service Pages

Each service has its own page, showing:
- Service details
- Company information
- The ability to navigate to the company profile to view all services offered by that company.

### Bonus Features

- **Rating System:** Customers can rate services they have requested, offering feedback for others.
- **Custom Design:** Modify the existing CSS and HTML to create a personalized look for the platform.

## Installation and Setup

To set up and run the project, follow these steps:

### Prerequisites

- Python 3.6+
- Django 3.1.14 (or compatible version)
- pip for installing dependencies

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/Vincent-Omondi/netfix.git
   cd netfix
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # For Unix/Linux
   venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. Create a superuser to access the Django admin panel:
   ```
   python3 manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python3 manage.py runserver
   ```

7. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the platform.

### Troubleshooting

If you encounter any issues while running the project, ensure that you are using Django v3.1.14. You can verify your Django version with:

```
python3 -m django --version
```

If your version does not match, install the correct version using:

```
pip install django==3.1.14
```

## Project Structure

- **netfix/:** Main project directory
- **users/:** Handles user registration, login, and profiles.
  - `views.py`: Manages user views like profile, login, registration.
  - `urls.py`: Defines URL patterns for the user-related views.
  - `templates/users/`: Contains HTML templates for user-related pages.
- **services/:** Manages service creation, listing, and details.
  - `views.py`: Handles the creation, display, and management of services.
  - `urls.py`: Defines URL patterns for service-related views.
  - `templates/services/`: HTML templates for service-related pages.
- **main/:** General project management (home page, navigation, common features).
  - `views.py`: Manages views for the home page, navigation, etc.
  - `urls.py`: URL patterns for common pages.

## Commands Overview

- Run the server:
  ```
  python3 manage.py runserver
  ```
- Create a new app:
  ```
  python3 manage.py startapp <app_name>
  ```
- Create a superuser for admin access:
  ```
  python3 manage.py createsuperuser
  ```
- Database migrations:
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

## Contribution Guidelines

1. Fork the repository and clone your fork.
2. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature-branch
   ```
3. Commit your changes and push to your fork:
   ```
   git commit -m "Description of changes"
   git push origin feature-branch
   ```
4. Submit a pull request to the main repository.

## License

This project is licensed under a **Custom License** that restricts commercial use. See the [LICENSE](./LICENSE) file for details.

## Contact

For questions or support, please contact the project maintainer at [vincentomondi251@gmail.com](mailto:vincentomondi251@.com).