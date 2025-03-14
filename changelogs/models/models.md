# Data Models Changelog

## [1.0.0] - 2024-03-20

### Added
- Created User model
  - Basic user information (email, name)
  - Password hashing
  - Language preferences
  - Subscription status
  - Activity tracking

- Created Interview model
  - Interview session management
  - Question and answer tracking
  - Voice and facial metrics
  - Performance scoring
  - Status management

- Created Resume model
  - File storage and parsing
  - Education history
  - Work experience
  - Skills tracking
  - Project portfolio
  - Certifications

- Created Role model
  - Role categories and specializations
  - Required and preferred skills
  - Experience level requirements
  - Interview structure configuration
  - Difficulty distribution

### Changed
- Enhanced model validation using Pydantic
- Added MongoDB ObjectId support
- Implemented JSON serialization for all models

### Security
- Added password hashing for user model
- Implemented data validation
- Added file type restrictions 