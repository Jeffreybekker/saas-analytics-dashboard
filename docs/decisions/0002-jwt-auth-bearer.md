# 0002: JWT Authentication with Bearer Tokens

## Context
We need a way for users (admin, client, end user) to log in and use the API safely.  
The frontend (e.g. React/Next.js) and backend (Django REST Framework) run on different domains.  
Because of this, we cannot rely on cookies and traditional sessions.

## Decision
- We use **JWT tokens** with `djangorestframework-simplejwt`.  
- On login, the backend returns:
  - **Access token** (short lifetime, used in requests)  
  - **Refresh token** (longer lifetime, used to get a new access token)  
- Clients must send the access token in the **Authorization header** using the **Bearer** scheme:  


- **CORS** is handled via `django-cors-headers`:
  - Only trusted frontend domains are allowed to call the API.  
  - This prevents requests from unknown websites.  

- **CSRF** is not needed:
  - CSRF protection is only required for cookie-based authentication.  
  - Since we use JWT in headers, we can safely skip CSRF.

## Outcome
- Frontend and backend communicate easily without cookies.  
- Tokens expire and can be refreshed securely.  
- Each request includes the **Bearer JWT token**, ensuring the backend knows who the user is and their role.  
- Only trusted domains can access the API, and CSRF is not needed.  
