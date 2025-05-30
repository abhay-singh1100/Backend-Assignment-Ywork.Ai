# Project Report: Ywork.ai Order Management System Template

## 1. Introduction
This project is a Django Rest Framework (DRF) template for an Order Management System, designed to demonstrate secure API development and Google OAuth 2.0 integration. It provides a solid foundation for scalable, secure, and extensible backend solutions.

---

## 2. Architecture Overview
- **Backend Framework:** Django 5.x with Django Rest Framework
- **Authentication:** Google OAuth 2.0 (access and refresh tokens stored securely)
- **API:** RESTful endpoints for order creation and retrieval
- **Database:** SQLite (default, can be swapped for PostgreSQL/MySQL)
- **Admin:** Django admin for managing users, orders, and OAuth tokens

---

## 3. Key Features
- **Google OAuth 2.0 Authentication:**
  - Users authenticate via Google, tokens are stored in the database.
  - Only authenticated users can access the API.
- **Order Management API:**
  - Users can create and retrieve their own orders.
  - Filtering by title is supported.
- **Security:**
  - All sensitive credentials are loaded from environment variables.
  - API endpoints are protected by a custom authentication class.
- **Extensibility:**
  - Modular codebase for easy feature addition.

---

## 4. Setup & Configuration
1. **Clone the repository and install dependencies:**
   ```sh
   git clone <your-repo-url>
   cd <project-directory>
   pip install -r requirements.txt
   ```
2. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your Google OAuth credentials.
3. **Run migrations and create a superuser:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser --email admin@ywork.ai --username admin
   ```
4. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

---

## 5. Google OAuth 2.0 Flow
- User visits `/auth/login/` to start authentication.
- After Google login, user is redirected to `/auth/callback/`.
- Access and refresh tokens are stored in the database.
- User is logged in and can access protected endpoints.

---

## 6. API Usage
- **POST /orders/**: Create a new order (requires Bearer token)
- **GET /orders/**: Retrieve orders for the authenticated user (filter by `title` optional)
- **Authentication:**
  - Use the access token from the database as a Bearer token in the `Authorization` header.

---

## 7. Testing
- Use Postman or curl to test endpoints.
- Example:
  ```sh
  curl -H "Authorization: Bearer <access_token>" http://localhost:8000/orders/
  ```
- All endpoints require a valid Google OAuth token.

---

## 8. Security & Best Practices
- Do not commit `.env` or secrets to version control.
- Use strong, unique credentials for Google OAuth.
- Review and restrict OAuth scopes as needed.

---

## 9. Conclusion
This template demonstrates secure, modern backend development with Django and Google OAuth. It is ready for extension into a full-featured order management or similar system.

---

## 10. References
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) 