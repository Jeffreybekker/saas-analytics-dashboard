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

**Extra explanation**
- Pipenv creates automatically a Pipfile
- Pipfile.lock makes sure everyone uses the same version
- No need anymore for requirements.txt

## Configuration
**Create a .env-file in the root of the project**  
