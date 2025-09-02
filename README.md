# SaaS Analytics Dashboard

## Description
This project is a SaaS Analytics Dashboard built with Django and PostgreSQL.
It is designed to collect, store, and analyze event data for multiple clients in a secure way.  
At this moment the project is still in development.

## Features

- Multi-tenant user roles (Admin, Client, End User)  
- PostgreSQL database connection  
- Event logging (console and file)  
- Continuous Integration with GitHub Actions  
- Pre-commit hooks, linting and formatting with Ruff 

## Installation

1. **Clone the repository:**
```
git clone https://github.com/Jeffreybekker/saas-analytics-dashboard.git
```

2. **Install pipenv:**
```
pip install --user pipenv
```

3. **Install dependencies:**
```
pipenv install --dev
```

4. **Activate the environment:**
```
pipenv shell
```

5. **Run migrations and start the server:**
```
python manage.py migrate
```
```
python manage.py runserver
```

**Extra explanation:**
- Pipenv creates automatically a Pipfile
- Pipfile.lock makes sure everyone uses the same version
- No need anymore for requirements.txt

## Database Setup
Make sure you have PostgreSQL running locally.

1. Create a new database:
```
CREATE DATABASE saas_analytics;
```
2. Use the default PostgreSQL user (postgres) or your own.  
3. Check that PostgreSQL is running on the default port 5432 (or change it in your .env file).  

## Configuration
Create a .env-file in the root of the project.  

**Example:**  

SECRET_KEY=your-secret-key  
DEBUG=True  
ALLOWED_HOSTS=localhost,127.0.0.1  

POSTGRES_DB= saas_analytics
POSTGRES_USER= postgres
POSTGRES_PASSWORD=your-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

## Planned Features
- Event model with JSON metadata
- API endpoints for event tracking
- Swagger / OpenAPI documentation
- Basic dashboard for clients
