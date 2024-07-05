import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';

const storev = configureStore({
  reducer: {
    user: userReducer,
  },
});

export type RootState = ReturnType<typeof storev.getState>;
export type AppDispatch = typeof storev.dispatch;

export default storev;
