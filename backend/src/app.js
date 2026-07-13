require('dotenv').config();
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

const app = express();

// Middleware
app.use(helmet());
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true
}));
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Root endpoint
app.get('/api', (req, res) => {
  res.json({
    message: 'Faculty ERP API',
    version: '1.0.0',
    endpoints: {
      health: '/api/health',
      auth: '/api/auth',
      students: '/api/students',
      courses: '/api/courses',
      attendance: '/api/attendance',
      grades: '/api/grades'
    }
  });
});

// Routes (to be implemented)
// app.use('/api/auth', require('./routes/authRoutes'));
// app.use('/api/students', require('./routes/studentRoutes'));
// app.use('/api/courses', require('./routes/courseRoutes'));
// app.use('/api/attendance', require('./routes/attendanceRoutes'));
// app.use('/api/grades', require('./routes/gradeRoutes'));

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message || 'Internal server error'
  });
});

module.exports = app;
