import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_URL,
});

// Add token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Handle responses
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const authService = {
  login: (email, password) => api.post('/auth/login', { email, password }),
  register: (data) => api.post('/auth/register', data),
};

export const studentService = {
  getAll: (page = 1, limit = 20) => api.get(`/students?page=${page}&limit=${limit}`),
  getById: (id) => api.get(`/students/${id}`),
  create: (data) => api.post('/students', data),
  update: (id, data) => api.patch(`/students/${id}`, data),
  delete: (id) => api.delete(`/students/${id}`),
};

export const courseService = {
  getAll: () => api.get('/courses'),
  getById: (id) => api.get(`/courses/${id}`),
  create: (data) => api.post('/courses', data),
  update: (id, data) => api.patch(`/courses/${id}`, data),
  delete: (id) => api.delete(`/courses/${id}`),
};

export const attendanceService = {
  getBycourse: (courseId) => api.get(`/courses/${courseId}/attendance`),
  mark: (courseId, data) => api.post(`/courses/${courseId}/attendance/mark`, data),
};

export const gradeService = {
  getByStudent: (courseId, studentId) => api.get(`/courses/${courseId}/students/${studentId}/grade-summary`),
  submit: (courseId, data) => api.post(`/courses/${courseId}/grades`, data),
};

export default api;
