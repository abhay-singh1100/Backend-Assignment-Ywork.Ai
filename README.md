# Ywork.ai Order Management System Template

## Overview
This project is a robust Django Rest Framework (DRF) template for an Order Management System, featuring:
- Google OAuth 2.0 authentication
- Secure, protected API endpoints for order entry and retrieval
- Clean, extensible codebase following best practices

---

## Features
- **Google OAuth 2.0 Authentication**: Users authenticate via Google, and tokens are securely stored.
- **Order API**: Authenticated users can create and retrieve their own orders.
- **Admin Panel**: Manage users, orders, and OAuth tokens via Django admin.
- **Security**: All sensitive keys are loaded from environment variables. Endpoints are protected and only accessible to authenticated users.

---

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <project-directory>
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in your project root (see `.env.example`):
```
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/
```

### 4. Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```sh
python manage.py createsuperuser --email admin@ywork.ai --username admin
```

### 6. Start the Server
```sh
python manage.py runserver
```

---

## Google OAuth 2.0 Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or use an existing one).
3. Go to **APIs & Services > Credentials**.
4. Create OAuth 2.0 Client ID credentials:
   - Application type: Web application
   - Authorized redirect URI: `http://localhost:8000/auth/callback/`
5. Copy the client ID and secret into your `.env` file.

---

## API Endpoints

### 1. Google OAuth
- `GET /auth/login/` — Redirects to Google for authentication
- `GET /auth/callback/` — Handles the OAuth callback, exchanges code for tokens, saves them, and logs in the user

### 2. Orders
- `GET /orders/` — List orders for the authenticated user (optionally filter by `title`)
- `POST /orders/` — Create a new order for the authenticated user

#### Example Request (using Bearer token):
```http
GET /orders/
Authorization: Bearer <access_token>
```

#### Example POST Body:
```json
{
  "title": "Test Order",
  "description": "This is a test order."
}
```

---

## Testing the API
1. Authenticate via `http://127.0.0.1:8000/auth/login/` in your browser.
2. After login, your access token is stored in the database (see Django admin > User social auths)`http://127.0.0.1:8000/admin/`  in your browser.
3. Use the access token as a Bearer token in your API requests (e.g., with Postman or curl).

---

---

## Project Structure
```
ywork_oms/
├── manage.py
├── requirements.txt
├── README.md
├── ywork_oms/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── orders/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── oauth_models.py
    ├── oauth_views.py
    ├── authentication.py
    └── ...
```

---


---
