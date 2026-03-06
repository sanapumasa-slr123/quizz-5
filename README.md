# Python Syntax & Debugging Assistant - Backend API

A Django REST Framework API that provides intelligent Python debugging assistance using OpenAI's GPT-3.5. Users can create conversations, send messages, and receive AI-powered responses about Python concepts, debugging, and library recommendations.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Environment Configuration](#environment-configuration)

## ✨ Features

- **User Authentication**: JWT token-based authentication for secure API access
- **Conversation Management**: Create, list, and manage conversation threads
- **AI-Powered Responses**: OpenAI integration for intelligent Python assistance
- **Message History**: Full conversation history with user and assistant messages
- **Admin Dashboard**: Django admin interface for managing users, conversations, and products
- **CORS Support**: Configured for cross-origin requests from frontend applications
- **Product API**: RESTful endpoints for product management

## 📁 Project Structure

```
quiz-5/backend/
├── backend/              # Main Django project configuration
│   ├── settings.py       # Project settings (INSTALLED_APPS, middleware, etc.)
│   ├── urls.py           # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── base/                 # Base app with main routes and products
│   ├── models.py         # Product model
│   ├── views.py          # Product views and routes
│   ├── serializers.py    # Product serializer
│   └── urls.py           # Base app URLs
├── conversations/        # Chat conversations and messaging
│   ├── models.py         # Conversation and Message models
│   ├── views.py          # Conversation views
│   ├── serializers.py    # Conversation and Message serializers
│   ├── ai_service.py     # OpenAI integration logic
│   ├── urls.py           # Conversation routes
│   └── admin.py          # Admin configuration
├── authentication/       # User registration and login
│   ├── views.py          # Auth views (register, login)
│   ├── serializers.py    # Auth serializers
│   └── urls.py           # Auth routes
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
├── .env                  # Environment variables (create this file)
├── .env.example          # Environment variables template
└── requirements.txt      # Python dependencies
```

## 🛠 Tech Stack

- **Backend**: Django 6.0.3
- **API Framework**: Django REST Framework
- **Authentication**: djangorestframework-simplejwt (JWT)
- **AI Integration**: OpenAI API (GPT-3.5)
- **Database**: SQLite (development)
- **CORS**: django-cors-headers
- **Environment**: python-dotenv

## 📦 Installation

### Prerequisites
- Python 3.13+
- pip (Python package manager)
- Virtual environment support

### Step 1: Clone the Repository
```bash
git clone https://github.com/sanapumasa-slr123/QUIZ-5.git
cd quiz-5/backend
```

### Step 2: Create Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install django django-rest-framework djangorestframework-simplejwt django-cors-headers openai python-dotenv
```

## ⚙️ Setup Instructions

### Step 1: Configure Environment Variables
Create a `.env` file in the backend directory:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your_openai_api_key_here
```

Get your API key from: https://platform.openai.com/api-keys

### Step 2: Run Database Migrations
```bash
python manage.py migrate
```

This creates the SQLite database and applies all migrations for:
- User authentication
- Products
- Conversations
- Messages

### Step 3: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. You'll use these credentials to access `/admin/`

### Step 4: Start Development Server
```bash
python manage.py runserver
```

Server runs on: `http://127.0.0.1:8000/`

## 🔌 API Endpoints

### Base Routes
- **GET** `/api/v1/` - View all available API routes
- **GET** `/api/v1/products/` - List all products
- **GET** `/api/v1/products/<id>/` - Get specific product details

### Authentication Routes (No JWT Required)
- **POST** `/api/v1/auth/signup/` - Register new user
- **POST** `/api/v1/auth/signin/` - Login and get JWT token

### Conversation Routes (JWT Required)
- **POST** `/api/v1/conversations/` - Create new conversation with message
- **GET** `/api/v1/conversations/list/` - Get all user conversations
- **GET** `/api/v1/conversations/<id>/` - Get specific conversation with all messages
- **POST** `/api/v1/conversations/<id>/message/` - Add message to existing conversation and get AI response

### Admin (JWT Required)
- **GET** `/admin/` - Django admin dashboard

## 📮 Testing with Postman

### 1. Register User
**POST** `http://127.0.0.1:8000/api/v1/auth/signup/`

Headers: `Content-Type: application/json`

Body:
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123",
  "password_confirm": "password123"
}
```

### 2. Login (Get JWT Token)
**POST** `http://127.0.0.1:8000/api/v1/auth/signin/`

Headers: `Content-Type: application/json`

Body:
```json
{
  "username": "testuser",
  "password": "password123"
}
```

Response includes `access` and `refresh` tokens. Copy the `access` token.

### 3. Create Conversation (With JWT Token)
**POST** `http://127.0.0.1:8000/api/v1/conversations/`

Headers:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

Body:
```json
{
  "title": "Python Debugging Help",
  "message": "How do I fix a TypeError in Python?"
}
```

The AI will automatically respond with helpful Python debugging advice.

### 4. List All Conversations
**GET** `http://127.0.0.1:8000/api/v1/conversations/list/`

Headers:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 5. Get Conversation Details
**GET** `http://127.0.0.1:8000/api/v1/conversations/1/`

Headers:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 6. Add Message to Conversation
**POST** `http://127.0.0.1:8000/api/v1/conversations/1/message/`

Headers:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

Body:
```json
{
  "message": "What's the difference between == and is in Python?"
}
```

## 🔐 Environment Configuration

Create a `.env` file with the following:

```env
# Required: OpenAI API Key
OPENAI_API_KEY=sk-your_key_here

# Optional: Django settings
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Important**: Never commit `.env` to version control. It's in `.gitignore`.

## 📝 API Response Examples

### Successful Authentication Response
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "username": "testuser",
  "email": "test@example.com"
}
```

### Conversation Response
```json
{
  "_id": 1,
  "title": "Python Debugging Help",
  "created_at": "2026-03-05T12:30:00Z",
  "updated_at": "2026-03-05T12:30:00Z",
  "user": 1,
  "messages": [
    {
      "id": 1,
      "conversation": 1,
      "role": "user",
      "content": "How do I fix a TypeError?",
      "created_at": "2026-03-05T12:30:00Z"
    },
    {
      "id": 2,
      "conversation": 1,
      "role": "assistant",
      "content": "A TypeError occurs when you try to use an operation on the wrong data type...",
      "created_at": "2026-03-05T12:30:05Z"
    }
  ]
}
```

## 🤖 AI Assistant Rules

The Python Syntax & Debugging Assistant follows these rules:

✅ **Can Help With:**
- Python syntax and concepts
- Debugging Python code
- Recommending Python libraries
- Fixing Python code snippets

❌ **Will Refuse:**
- Writing code in other languages (JavaScript, C++, Java, etc.)
- Discussing general tech news
- Computer hardware discussions

If you ask for non-Python code, the assistant responds:
> "I can only help with Python code. Please ask me something related to Python."

## 📚 Models

### User Model
- Uses Django's built-in User model
- Fields: username, email, password, first_name, last_name

### Conversation Model
- `_id`: Primary key (AutoField)
- `title`: Conversation title (CharField)
- `created_at`: Creation timestamp (DateTimeField)
- `updated_at`: Last update timestamp (DateTimeField)
- `user`: Foreign key to User (ForeignKey)

### Message Model
- `id`: Primary key (AutoField)
- `conversation`: Foreign key to Conversation (ForeignKey)
- `role`: 'user' or 'assistant' (CharField)
- `content`: Message text (TextField)
- `created_at`: Creation timestamp (DateTimeField)

### Product Model
- `id`: Primary key (AutoField)
- `name`: Product name (CharField)
- `price`: Product price (DecimalField)
- `created_at`: Creation timestamp (DateTimeField)
- `updated_at`: Last update timestamp (DateTimeField)

## 🐛 Troubleshooting

### Server won't start on port 8000
```bash
# Check if port 8000 is already in use
lsof -i :8000

# Kill the process (on macOS/Linux)
kill -9 <PID>

# Or use a different port
python manage.py runserver 8001
```

### "ModuleNotFoundError: No module named 'django'"
Ensure your virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### "Couldn't import Django. Did you forget to activate a virtual environment?"
Same issue - activate your virtual environment first.

### OpenAI API Key Error
1. Verify your API key is correct in `.env`
2. Check your OpenAI account has credits
3. Ensure the key starts with `sk-`

## 📄 License

This project is part of a quiz assignment. All rights reserved.

## 👤 Author

- **Name**: Sana Pumasa
- **GitHub**: https://github.com/sanapumasa-slr123
- **Repository**: https://github.com/sanapumasa-slr123/QUIZ-5

---

**Last Updated**: March 6, 2026

