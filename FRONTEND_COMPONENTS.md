# Frontend Components Documentation

## Core Components

### AuthProvider
- **Purpose**: Manages authentication state and user sessions
- **Key Features**:
  - JWT token management
  - User session persistence
  - Login/logout functionality
  - Protected route handling

### InterviewProvider
- **Purpose**: Manages interview state and progression
- **Key Features**:
  - Question management
  - Answer submission
  - Interview progress tracking
  - Real-time feedback

### MediaProvider
- **Purpose**: Handles audio/video recording and playback
- **Key Features**:
  - Camera/microphone access
  - Recording controls
  - Media upload
  - Playback functionality

## Page Components

### LoginPage
- **Path**: `/login`
- **Features**:
  - Email/password login
  - Form validation
  - Error handling
  - Redirect on success

### RegisterPage
- **Path**: `/register`
- **Features**:
  - User registration form
  - Password validation
  - Email verification
  - Success/error handling

### DashboardPage
- **Path**: `/dashboard`
- **Features**:
  - Interview history
  - Performance metrics
  - Resume management
  - Role selection

### InterviewPage
- **Path**: `/interview/:id`
- **Features**:
  - Question display
  - Timer management
  - Media recording
  - Answer submission
  - Real-time feedback

### ProfilePage
- **Path**: `/profile`
- **Features**:
  - User information
  - Settings management
  - Resume upload
  - Statistics view

## UI Components

### Button
```tsx
<Button 
  variant="primary" | "secondary" | "danger"
  size="sm" | "md" | "lg"
  loading={boolean}
  disabled={boolean}
  onClick={() => void}
>
  Button Text
</Button>
```

### Input
```tsx
<Input
  type="text" | "password" | "email"
  placeholder="Enter value"
  value={string}
  onChange={(e) => void}
  error={string}
/>
```

### Modal
```tsx
<Modal
  isOpen={boolean}
  onClose={() => void}
  title="Modal Title"
>
  Modal Content
</Modal>
```

### Card
```tsx
<Card
  title="Card Title"
  subtitle="Optional subtitle"
  footer={ReactNode}
>
  Card Content
</Card>
```

### Avatar
```tsx
<Avatar
  src="image-url"
  size="sm" | "md" | "lg"
  alt="User name"
/>
```

## Utility Components

### ErrorBoundary
- **Purpose**: Catches and handles React errors
- **Usage**:
```tsx
<ErrorBoundary fallback={<ErrorPage />}>
  <App />
</ErrorBoundary>
```

### LoadingSpinner
- **Purpose**: Shows loading state
- **Usage**:
```tsx
<LoadingSpinner size="sm" | "md" | "lg" />
```

### Toast
- **Purpose**: Shows notifications
- **Usage**:
```tsx
toast.show({
  type: "success" | "error" | "info",
  message: "Notification message"
});
```

## Layout Components

### Header
- **Features**:
  - Navigation menu
  - User profile
  - Notifications
  - Search bar

### Sidebar
- **Features**:
  - Navigation links
  - Collapsible sections
  - Quick actions
  - User stats

### Footer
- **Features**:
  - Copyright info
  - Links
  - Social media
  - Contact info

## Form Components

### FormGroup
```tsx
<FormGroup
  label="Field Label"
  error={string}
  required={boolean}
>
  <Input />
</FormGroup>
```

### Select
```tsx
<Select
  options={[
    { value: "option1", label: "Option 1" }
  ]}
  value={string}
  onChange={(value) => void}
  placeholder="Select an option"
/>
```

### Checkbox
```tsx
<Checkbox
  checked={boolean}
  onChange={(checked) => void}
  label="Checkbox label"
/>
```

## Interview Components

### QuestionCard
- **Purpose**: Displays interview questions
- **Features**:
  - Question text
  - Timer
  - Difficulty level
  - Category indicator

### MediaRecorder
- **Purpose**: Handles audio/video recording
- **Features**:
  - Record controls
  - Preview
  - Upload progress
  - Error handling

### FeedbackDisplay
- **Purpose**: Shows interview feedback
- **Features**:
  - Score display
  - Detailed feedback
  - Improvement suggestions
  - Performance metrics

## State Management

### Redux Store Structure
```typescript
interface RootState {
  auth: {
    user: User | null;
    token: string | null;
    loading: boolean;
    error: string | null;
  };
  interview: {
    current: Interview | null;
    questions: Question[];
    answers: Answer[];
    feedback: Feedback | null;
  };
  media: {
    recording: boolean;
    audioStream: MediaStream | null;
    videoStream: MediaStream | null;
    error: string | null;
  };
}
```

## Styling

### Theme Configuration
```typescript
const theme = {
  colors: {
    primary: "#007AFF",
    secondary: "#5856D6",
    success: "#34C759",
    danger: "#FF3B30",
    warning: "#FF9500",
    info: "#5AC8FA",
    gray: {
      100: "#F2F2F7",
      200: "#E5E5EA",
      300: "#D1D1D6",
      400: "#C7C7CC",
      500: "#AEAEB2",
    }
  },
  spacing: {
    xs: "0.25rem",
    sm: "0.5rem",
    md: "1rem",
    lg: "1.5rem",
    xl: "2rem"
  },
  breakpoints: {
    sm: "640px",
    md: "768px",
    lg: "1024px",
    xl: "1280px"
  }
};
``` 