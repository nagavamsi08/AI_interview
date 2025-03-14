# API Endpoints Changelog

## [1.0.0] - 2024-03-20

### Added
- Created user endpoints (`/api/v1/users/`)
  - User registration with email validation
  - User login with JWT authentication
  - User profile management
  - User statistics endpoint

- Created interview endpoints (`/api/v1/interviews/`)
  - Create new interview sessions
  - List user interviews with status filtering
  - Get interview details
  - Submit answers with audio/video support
  - Update metrics (voice and facial)
  - Complete, pause, resume, and abandon interviews

- Created resume endpoints (`/api/v1/resumes/`)
  - Upload resume files with PDF validation
  - Create resume entries with parsing
  - Get user's active resume
  - Update resume details
  - Delete resumes
  - Analyze resume against roles

- Created role endpoints (`/api/v1/roles/`)
  - Create new roles (superuser only)
  - List roles with category/experience filtering
  - Update role details
  - Manage role skills
  - Role statistics endpoint

### Security
- Added authentication middleware
- Implemented role-based access control
- Added request validation
- Added file upload restrictions 