# user_management_system
## Overview
This application provides a comprehensive user management system, enabling functionalities such as user registration, login, password reset, and password change. It's built using Django, a high-level Python web framework, ensuring robust and secure handling of user accounts. Through this project, we demonstrate the customization of Django's default user management templates and the integration of email functionality for password resets. Additionally, the application supports authentication via external services, offering users a seamless and flexible login experience.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- `python 3.12.2`
- `pip`
- `virtualenv`

### Installing
A step-by-step series of examples that tell you how to get a development environment running:

1. clone the repo
2. create virtual environment 
```
python -m venv .env
```
3. install modules
```
pip install -r requirement.txt
```
4. Make migration and migrate 
```
python manage.py makemigrations
python manage.py migrate
```
5. Run the server! 
```
python manage.py runserver
```