# DRF API

A Django REST Framework API for managing messages. This project provides a RESTful API endpoint for creating and retrieving messages.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)

## ✨ Features

- **RESTful API**: Clean REST endpoints for message operations
- **Django REST Framework**: Built with DRF for robust API development
- **Message Management**: Create and retrieve messages via API
- **SQLite Database**: Lightweight database for development
- **Django Admin**: Built-in admin interface for data management


## 📦 Prerequisites

- Python 3.13 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Navigate to the project directory**:
   ```bash
   cd drf_api
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using the project configuration:
   ```bash
   pip install -e .
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## 🎯 Usage

1. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the API**:
   - API Base URL: `http://127.0.0.1:8000/api/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## 📡 API Endpoints

### Messages

#### List Messages
```http
GET /api/messages/
```

**Response:**
```json
[
  {
    "id": 1,
    "text": "Hello, world!",
    "created_at": "2024-01-01T12:00:00Z",
    "is_active": true
  }
]
```

#### Create Message
```http
POST /api/messages/
Content-Type: application/json

{
  "text": "New message",
}
```

**Response:**
```json
{
  "id": 2,
  "text": "New message",
  "created_at": "2025-01-01T12:05:00Z",
  "is_active": true
}
```

### Example with cURL

**Get all messages:**
```bash
curl http://127.0.0.1:8000/api/messages/
```

**Create a message:**
```bash
curl -X POST http://127.0.0.1:8000/api/messages/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from API", "is_active": true}'
```

## 📁 Project Structure

```
drf_api/
├── config/                 # Django project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI config
│   └── asgi.py            # ASGI config
├── message/                # Message app
│   ├── models.py          # Message model
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # App URL routing
│   └── admin.py           # Admin configuration
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── pyproject.toml         # Project configuration
├── requirements.txt       # Project required modules
└── README.md              # This file
```

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Accessing Admin Panel
1. Start the server: `python manage.py runserver`
2. Navigate to: `http://127.0.0.1:8000/admin/`
3. Login with superuser credentials

## 📚 Dependencies

- **Django** (>=6.0): Web framework
- **djangorestframework** (>=3.16.1): REST API toolkit

## 🔒 Security Notes

- Change `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for production
- Use environment variables for sensitive settings

---

**Built with Django REST Framework**

