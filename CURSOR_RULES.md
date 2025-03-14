# AI Interview Platform - Development Guidelines

## Project Structure

```
ai-interview/
├── backend/                 # Backend application
│   ├── app/                # Main application code
│   │   ├── api/           # API endpoints and routing
│   │   ├── core/          # Core functionality
│   │   ├── models/        # Data models
│   │   └── services/      # Business logic services
│   ├── tests/             # Test files
│   └── requirements.txt    # Python dependencies
│
├── frontend/              # Frontend application
│   ├── src/              # Source code
│   │   ├── components/   # React components
│   │   ├── pages/       # Page components
│   │   ├── services/    # API services
│   │   └── styles/      # Theme and styles
│   └── package.json     # Node.js dependencies
│
└── changelogs/          # Change documentation
    ├── api/            # API changes
    ├── core/           # Core changes
    ├── models/         # Data model changes
    ├── services/       # Service changes
    └── frontend/       # Frontend changes
```

## Coding Conventions

### General Rules

1. **File Naming**
   - Use lowercase with underscores for Python files: `user_service.py`
   - Use PascalCase for React components: `UserProfile.tsx`
   - Use camelCase for other JavaScript/TypeScript files: `apiService.ts`

2. **Code Organization**
   - Group related functionality in modules
   - Keep files focused and single-responsibility
   - Maximum file length: 500 lines
   - Maximum function length: 50 lines

### Backend Rules

1. **FastAPI Endpoints**
   ```python
   @router.http_method("path")
   async def endpoint_name(
       required_param: Type,
       optional_param: Optional[Type] = None,
       current_user: User = Depends(get_current_user)
   ):
       """Docstring explaining the endpoint"""
       # Implementation
   ```

2. **Models**
   ```python
   class ModelName(BaseModel):
       """Docstring explaining the model"""
       required_field: Type
       optional_field: Optional[Type] = None
       
       class Config:
           # Model configuration
   ```

3. **Services**
   ```python
   async def service_function(param: Type) -> ReturnType:
       """Docstring explaining the service function"""
       # Implementation
   ```

### Frontend Rules

1. **React Components**
   ```typescript
   const ComponentName: React.FC<Props> = ({ prop1, prop2 }) => {
     // Implementation
     return (
       <div>
         {/* JSX */}
       </div>
     );
   };
   ```

2. **Styling**
   - Use Material-UI's styling system
   - Follow theme configuration
   - Support RTL languages

3. **State Management**
   - Use Redux for global state
   - Use React hooks for local state
   - Follow Redux Toolkit patterns

## Error Handling

1. **Backend Errors**
   - Use custom exception classes
   - Provide meaningful error messages
   - Include appropriate HTTP status codes

2. **Frontend Errors**
   - Use error boundaries
   - Implement toast notifications
   - Handle API errors gracefully

## Documentation

1. **Code Documentation**
   - Add docstrings to all functions/classes
   - Explain complex logic with comments
   - Keep documentation up-to-date

2. **API Documentation**
   - Use FastAPI's automatic documentation
   - Include example requests/responses
   - Document all possible error responses

3. **Changelog Updates**
   - Update for all significant changes
   - Follow Keep a Changelog format
   - Include version numbers

## Testing

1. **Backend Tests**
   - Write unit tests for services
   - Write integration tests for APIs
   - Maintain 80% code coverage

2. **Frontend Tests**
   - Write component tests
   - Write integration tests
   - Test responsive design

## Security

1. **Authentication**
   - Use JWT tokens
   - Implement refresh tokens
   - Secure token storage

2. **Authorization**
   - Implement role-based access
   - Validate user permissions
   - Protect sensitive routes

3. **Data Protection**
   - Validate all inputs
   - Sanitize user data
   - Implement rate limiting

## Performance

1. **Backend Performance**
   - Use async/await
   - Implement caching
   - Optimize database queries

2. **Frontend Performance**
   - Implement code splitting
   - Use lazy loading
   - Optimize bundle size

## Version Control

1. **Branch Naming**
   - feature/feature-name
   - bugfix/bug-description
   - hotfix/issue-description

2. **Commit Messages**
   ```
   type(scope): description
   
   - type: feat, fix, docs, style, refactor, test, chore
   - scope: component affected
   - description: changes made
   ```

3. **Pull Requests**
   - Include description of changes
   - Reference related issues
   - Update changelog

## Development Workflow

1. **Local Development**
   - Use environment variables
   - Follow README instructions
   - Use provided scripts

2. **Code Review**
   - Follow review checklist
   - Address all comments
   - Update documentation

3. **Deployment**
   - Follow deployment checklist
   - Update changelog
   - Tag releases 