import { configureStore } from '@reduxjs/toolkit';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';
import authReducer from './features/auth/authSlice';

// Reducers will be imported here
// import userReducer from './features/user/userSlice';
// import interviewReducer from './features/interview/interviewSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    // Add reducers here
    // user: userReducer,
    // interview: interviewReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Use throughout your app instead of plain `useDispatch` and `useSelector`
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

export default store; 