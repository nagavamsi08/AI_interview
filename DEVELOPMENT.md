# Development Guide

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   ├── tests/
│   ├── .env
│   └── requirements.txt
│
└── frontend/
    ├── components/
    ├── pages/
    ├── public/
    ├── styles/
    ├── utils/
    ├── .env
    └── package.json
```

## Development Setup

### Backend Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

2. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Update environment variables

4. **Run Development Server**
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. **Install Dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Configure Environment**
   - Copy `.env.example` to `.env.local`
   - Update environment variables

3. **Run Development Server**
   ```bash
   npm run dev
   ```

## Development Workflow

### Git Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/feature-name
   ```

2. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add feature description"
   ```

3. **Push Changes**
   ```bash
   git push origin feature/feature-name
   ```

4. **Create Pull Request**
   - Create PR on GitHub
   - Request review
   - Address feedback

### Code Style

1. **Python (Backend)**
   - Follow PEP 8
   - Use Black formatter
   - Use isort for imports
   ```bash
   black .
   isort .
   ```

2. **TypeScript (Frontend)**
   - Follow Prettier config
   - Use ESLint
   ```bash
   npm run format
   npm run lint
   ```

## Testing

### Backend Testing

1. **Run Tests**
   ```bash
   pytest
   ```

2. **Test Coverage**
   ```bash
   pytest --cov=app
   ```

3. **Test Structure**
   ```python
   def test_feature():
       # Arrange
       data = {"key": "value"}
       
       # Act
       result = feature(data)
       
       # Assert
       assert result == expected
   ```

### Frontend Testing

1. **Run Tests**
   ```bash
   npm test
   ```

2. **Component Testing**
   ```typescript
   describe('Component', () => {
     it('should render correctly', () => {
       render(<Component />);
       expect(screen.getByText('text')).toBeInTheDocument();
     });
   });
   ```

## API Development

### Adding New Endpoints

1. **Create Route**
   ```python
   @router.post("/endpoint")
   async def create_item(item: ItemCreate):
       return await create_item_service(item)
   ```

2. **Add Schema**
   ```python
   class ItemCreate(BaseModel):
       name: str
       description: str
   ```

3. **Add Service**
   ```python
   async def create_item_service(item: ItemCreate):
       return await db.items.insert_one(item.dict())
   ```

### API Documentation

1. **OpenAPI Docs**
   - Available at `/docs`
   - Update descriptions
   - Add examples

2. **API Testing**
   ```bash
   curl -X POST http://localhost:8000/api/endpoint \
        -H "Content-Type: application/json" \
        -d '{"key": "value"}'
   ```

## Component Development

### Creating New Components

1. **Component Structure**
   ```tsx
   interface Props {
     prop1: string;
     prop2: number;
   }
   
   export const Component: React.FC<Props> = ({ prop1, prop2 }) => {
     return (
       <div>
         {prop1}: {prop2}
       </div>
     );
   };
   ```

2. **Styling**
   ```tsx
   import styles from './Component.module.css';
   
   <div className={styles.container}>
     {content}
   </div>
   ```

3. **Testing**
   ```tsx
   import { render, screen } from '@testing-library/react';
   import { Component } from './Component';
   
   test('renders component', () => {
     render(<Component prop1="test" prop2={42} />);
     expect(screen.getByText('test: 42')).toBeInTheDocument();
   });
   ```

## State Management

### Redux Setup

1. **Create Slice**
   ```typescript
   const slice = createSlice({
     name: 'feature',
     initialState,
     reducers: {
       action: (state, action) => {
         state.value = action.payload;
       }
     }
   });
   ```

2. **Use Hooks**
   ```typescript
   const value = useSelector((state) => state.feature.value);
   const dispatch = useDispatch();
   
   dispatch(action(newValue));
   ```

## Error Handling

### Backend Errors

1. **Custom Exceptions**
   ```python
   class CustomException(HTTPException):
       def __init__(self, detail: str):
           super().__init__(status_code=400, detail=detail)
   ```

2. **Error Handlers**
   ```python
   @app.exception_handler(CustomException)
   async def custom_exception_handler(request, exc):
       return JSONResponse(
           status_code=exc.status_code,
           content={"detail": exc.detail}
       )
   ```

### Frontend Errors

1. **Error Boundaries**
   ```tsx
   class ErrorBoundary extends React.Component {
     componentDidCatch(error, errorInfo) {
       logError(error, errorInfo);
     }
     
     render() {
       return this.props.children;
     }
   }
   ```

2. **API Error Handling**
   ```typescript
   try {
     const response = await api.get('/endpoint');
   } catch (error) {
     handleError(error);
   }
   ```

## Performance Optimization

### Backend Optimization

1. **Database Queries**
   - Use indexes
   - Optimize queries
   - Use aggregation

2. **Caching**
   ```python
   @cache(ttl=3600)
   async def get_cached_data():
       return await expensive_operation()
   ```

### Frontend Optimization

1. **React Optimization**
   - Use memo
   - Use callbacks
   - Lazy loading
   ```typescript
   const Component = React.lazy(() => import('./Component'));
   ```

2. **Bundle Optimization**
   - Code splitting
   - Tree shaking
   - Image optimization

## Security Best Practices

1. **Input Validation**
   ```python
   def validate_input(data: str):
       if not re.match(r'^[a-zA-Z0-9]+$', data):
           raise ValidationError('Invalid input')
   ```

2. **Authentication**
   ```python
   def verify_token(token: str):
       try:
           return jwt.decode(token, SECRET_KEY)
       except jwt.InvalidTokenError:
           raise AuthenticationError()
   ```

3. **CORS Configuration**
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=ALLOWED_ORIGINS,
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

## Debugging

1. **Backend Debugging**
   ```python
   import logging
   
   logging.debug('Debug message')
   logging.error('Error message')
   ```

2. **Frontend Debugging**
   ```typescript
   console.log('Debug:', data);
   console.error('Error:', error);
   ```

## Documentation

1. **Code Documentation**
   ```python
   def function(param: str) -> dict:
       """
       Function description.
       
       Args:
           param: Parameter description
           
       Returns:
           dict: Return value description
       """
   ```

2. **API Documentation**
   ```python
   @app.get("/endpoint")
   async def endpoint():
       """
       Endpoint description.
       
       Returns:
           dict: Response description
       """
   ``` 