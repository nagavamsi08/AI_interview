# API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication

### Login
```http
POST /auth/login
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "password123"
}
```

### Register
```http
POST /auth/register
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "password123",
    "full_name": "John Doe"
}
```

## Interviews

### Create Interview
```http
POST /interviews
Authorization: Bearer <token>
Content-Type: application/json

{
    "role_id": "role123",
    "language": "en"
}
```

### Get Interview
```http
GET /interviews/{interview_id}
Authorization: Bearer <token>
```

### Submit Answer
```http
POST /interviews/{interview_id}/answers
Authorization: Bearer <token>
Content-Type: multipart/form-data

audio: <audio_file>
video: <video_file>
text: "Answer text"
code: "Code submission (optional)"
```

### Complete Interview
```http
POST /interviews/{interview_id}/complete
Authorization: Bearer <token>
```

## Resumes

### Upload Resume
```http
POST /resumes/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

file: <resume_file>
```

### Get Resume
```http
GET /resumes/{resume_id}
Authorization: Bearer <token>
```

## Roles

### List Roles
```http
GET /roles
Authorization: Bearer <token>
Query Parameters:
- category
- specialization
- experience_level
```

### Create Role
```http
POST /roles
Authorization: Bearer <token>
Content-Type: application/json

{
    "name": "Software Engineer",
    "category": "Engineering",
    "specialization": "Backend",
    "experience_level": "Senior",
    "required_skills": [
        {
            "name": "Python",
            "level": "Expert"
        }
    ],
    "interview_structure": {
        "technical": 5,
        "behavioral": 3
    }
}
```

## Response Formats

### Success Response
```json
{
    "status": "success",
    "data": {
        // Response data
    }
}
```

### Error Response
```json
{
    "status": "error",
    "detail": "Error message"
}
```

## Rate Limiting
- 100 requests per minute per user
- Rate limit headers included in response:
  ```
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 99
  X-RateLimit-Reset: 1635789600
  ```

## Security
1. **Authentication**
   - JWT tokens
   - 8-day expiration
   - Refresh token support

2. **CORS**
   - Whitelisted origins
   - Secure headers
   - CSRF protection

## Endpoints Summary

### Authentication
- POST `/auth/login`
- POST `/auth/register`
- POST `/auth/refresh-token`
- POST `/auth/logout`

### Interviews
- POST `/interviews`
- GET `/interviews/{id}`
- GET `/interviews`
- POST `/interviews/{id}/answers`
- POST `/interviews/{id}/complete`
- GET `/interviews/{id}/feedback`

### Resumes
- POST `/resumes/upload`
- GET `/resumes/{id}`
- GET `/resumes/user`
- PUT `/resumes/{id}`
- DELETE `/resumes/{id}`

### Roles
- GET `/roles`
- POST `/roles`
- GET `/roles/{id}`
- PUT `/roles/{id}`
- DELETE `/roles/{id}`

### Users
- GET `/users/me`
- PUT `/users/me`
- GET `/users/statistics` 