# SaaS Analytics Dashboard


## Description


## Features

- Basic Logging in console and file
- PostgreSQL database connection
- Multi-tenant user roles (Admin, Client, End User)
- Linting and formatting with Ruff
- CI + pre-commit hooks


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

**Database Setup**
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
Wat staat er in de .env-file?

SECRET_KEY=your-secret-key  
DEBUG=True  
ALLOWED_HOSTS=127.0.0.1,localhost  

POSTGRES_DB= saas_analytics
POSTGRES_USER= postgres
POSTGRES_PASSWORD=your-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
