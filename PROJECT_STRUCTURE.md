# AI Interview Platform - Project Structure

## Backend Structure

```
backend/
├── app/
│   ├── api/
│   │   └── api_v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py
│   │       │   ├── interviews.py
│   │       │   ├── resumes.py
│   │       │   └── users.py
│   │       └── api.py
│   ├── core/
│   │   ├── config.py
│   │   ├── deps.py
│   │   ├── exceptions.py
│   │   ├── middleware.py
│   │   ├── redis.py
│   │   └── security.py
│   ├── db/
│   │   └── mongodb.py
│   ├── models/
│   │   ├── interview.py
│   │   ├── resume.py
│   │   ├── role.py
│   │   └── user.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── interview_service.py
│   │   ├── resume_service.py
│   │   ├── role_service.py
│   │   └── user_service.py
│   └── main.py
├── tests/
├── .env
└── requirements.txt
```

## Key Components

1. **API Layer (`/api`)**: 
   - RESTful endpoints
   - Route definitions
   - Request/Response handling

2. **Core (`/core`)**:
   - Application configuration
   - Dependencies
   - Security
   - Middleware
   - Exception handling
   - Redis integration

3. **Database (`/db`)**:
   - MongoDB connection
   - Database utilities

4. **Models (`/models`)**:
   - Pydantic models
   - Data validation
   - Schema definitions

5. **Services (`/services`)**:
   - Business logic
   - External service integration
   - AI/ML functionality

## External Services Integration

1. **AI Services**:
   - OpenAI GPT-4 (Question generation)
   - OpenAI Whisper (Speech-to-text)
   - OpenAI TTS (Text-to-speech)

2. **Cloud Services**:
   - MongoDB Atlas (Database)
   - AWS S3 (File storage)
   - AWS Rekognition (Facial analysis)
   - Redis Cloud (Caching/Rate limiting)

## Environment Configuration
- Environment variables in `.env`
- Production/Development settings
- API keys and credentials 