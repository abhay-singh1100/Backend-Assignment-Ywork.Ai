# Project Workflow: Ywork.ai Order Management System Template

This document describes the full workflow of the Order Management System, including authentication, data flow, and the role of each Python file in the project.

---

## 1. User Authentication with Google OAuth 2.0

### a. Initiating OAuth Flow
- **File:** `orders/oauth_views.py`
- **View:** `google_login`
- **URL:** `/auth/login/`
- **Description:**
  - When a user visits `/auth/login/`, they are redirected to Google's OAuth 2.0 consent screen.
  - The view constructs the Google OAuth URL using credentials from environment variables (`.env`).

### b. Handling OAuth Callback
- **File:** `orders/oauth_views.py`
- **View:** `google_callback`
- **URL:** `/auth/callback/`
- **Description:**
  - Google redirects the user back to this endpoint with an authorization code.
  - The view exchanges the code for access and refresh tokens using the Google API.
  - It fetches the user's email/profile from Google, creates or updates a Django user, and stores the tokens in the `UserSocialAuth` model (`orders/oauth_models.py`).
  - The user is logged in to the Django session.

### c. Token Storage
- **File:** `orders/oauth_models.py`
- **Model:** `UserSocialAuth`
- **Description:**
  - Stores the user's Google access token, refresh token, and expiry.
  - Linked to the Django `User` model via a one-to-one relationship.

---

## 2. API Authentication for Orders

### a. Custom Authentication Class
- **File:** `orders/authentication.py`
- **Class:** `GoogleOAuth2Authentication`
- **Description:**
  - Checks for a Bearer token in the `Authorization` header of API requests.
  - Validates the token against those stored in `UserSocialAuth`.
  - If valid, authenticates the user for the request.

### b. DRF Settings
- **File:** `ywork_oms/settings.py`
- **Section:** `REST_FRAMEWORK`
- **Description:**
  - Sets `GoogleOAuth2Authentication` as the default authentication class for all DRF endpoints.
  - Ensures all API endpoints require authentication by default.

---

## 3. Order Management API

### a. Order Model
- **File:** `orders/models.py`
- **Model:** `Order`
- **Fields:** `user`, `title`, `description`, `created_at`
- **Description:**
  - Represents an order belonging to a user.

### b. Serializer
- **File:** `orders/serializers.py`
- **Class:** `OrderSerializer`
- **Description:**
  - Serializes and deserializes `Order` instances for API input/output.

### c. API View
- **File:** `orders/views.py`
- **Class:** `OrderListCreateView`
- **Endpoints:**
  - `GET /orders/` — List orders for the authenticated user (optionally filter by `title`)
  - `POST /orders/` — Create a new order for the authenticated user
- **Description:**
  - Uses DRF's `ListCreateAPIView`.
  - Filters orders by the current user and optional title query.
  - On creation, associates the order with the authenticated user.

### d. URL Routing
- **File:** `orders/urls.py`, `ywork_oms/urls.py`
- **Description:**
  - Maps `/orders/`, `/auth/login/`, and `/auth/callback/` to their respective views.

---

## 4. Admin Management
- **File:** `orders/admin.py`
- **Description:**
  - Registers `Order` and `UserSocialAuth` models for management in the Django admin interface.

---

## 5. Environment Variables
- **File:** `.env` (not committed), `.env.example`
- **Description:**
  - Stores sensitive credentials for Google OAuth (client ID, secret, redirect URI).
  - Loaded using `python-dotenv` in `orders/oauth_views.py`.

---

## 6. Project Flow Summary

1. **User visits `/auth/login/`** → Redirected to Google for authentication.
2. **User authenticates with Google** → Redirected back to `/auth/callback/`.
3. **Callback view exchanges code for tokens** → User info and tokens are stored in the database.
4. **User is logged in** → Can now access protected API endpoints.
5. **User sends API requests to `/orders/`** with Bearer token → Custom authentication class validates the token and grants access.
6. **Orders are created and retrieved** only for the authenticated user.

---

## 7. File Reference Table

| File                        | Purpose                                                      |
|-----------------------------|--------------------------------------------------------------|
| `orders/oauth_views.py`     | Google OAuth login/callback views                            |
| `orders/oauth_models.py`    | Model for storing OAuth tokens                               |
| `orders/authentication.py`  | Custom DRF authentication class                              |
| `orders/models.py`          | Order model                                                  |
| `orders/serializers.py`     | Order serializer                                             |
| `orders/views.py`           | Order API view                                               |
| `orders/urls.py`            | App URL routing                                              |
| `ywork_oms/urls.py`         | Project URL routing                                          |
| `orders/admin.py`           | Admin registration for models                                |
| `.env.example`              | Example environment variable file                            |
| `README.md`                 | Project documentation                                        |
| `REPORT.md`                 | Project summary and report                                   |

---

## 8. Extending the Project
- Add more fields to the `Order` model as needed.
- Implement order update/delete endpoints.
- Add user profile endpoints or additional OAuth providers.
- Integrate with frontend frameworks or external APIs.

---

For further details, see the code comments and the `README.md` documentation. 