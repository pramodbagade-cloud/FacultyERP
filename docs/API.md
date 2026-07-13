# Faculty ERP - API Documentation

Complete API reference for Faculty ERP backend.

## Base URL

```
http://localhost:5000/api
```

## Authentication

All protected endpoints require JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

---

## Health Check

### GET /health

Check if API is running.

**Response (200 OK):**
```json
{
  "status": "ok"
}
```

---

## Authentication Endpoints

### POST /auth/register

Register a new faculty/admin user.

**Request Body:**
```json
{
  "email": "teacher@college.edu",
  "password": "securePassword123",
  "full_name": "Dr. John Doe",
  "role": "faculty",
  "department": "Computer Science"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "teacher@college.edu",
    "full_name": "Dr. John Doe",
    "role": "faculty"
  },
  "message": "User registered successfully"
}
```

---

### POST /auth/login

Login to get JWT token.

**Request Body:**
```json
{
  "email": "teacher@college.edu",
  "password": "securePassword123"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "email": "teacher@college.edu",
      "full_name": "Dr. John Doe",
      "role": "faculty"
    }
  },
  "message": "Login successful"
}
```

---

## Sessions (Semesters) Endpoints

### GET /sessions

List all academic sessions.

**Query Parameters:**
- `active`: `true|false` (filter by active status)

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Spring 2024",
      "description": "Spring Semester 2024",
      "start_date": "2024-01-15",
      "end_date": "2024-05-31",
      "is_active": true
    }
  ]
}
```

---

### POST /sessions

Create a new session (Admin only).

**Request Body:**
```json
{
  "name": "Spring 2024",
  "description": "Spring Semester 2024",
  "start_date": "2024-01-15",
  "end_date": "2024-05-31",
  "is_active": true
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": { /* session object */ },
  "message": "Session created successfully"
}
```

---

## Courses Endpoints

### GET /courses

List all courses for the logged-in faculty.

**Query Parameters:**
- `session_id`: Filter by session

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "code": "CS101",
      "name": "Data Structures",
      "description": "Learn data structures",
      "credits": 4,
      "total_hours": 60,
      "session_id": 1,
      "faculty_id": 1
    }
  ]
}
```

---

### POST /courses

Create a new course.

**Request Body:**
```json
{
  "session_id": 1,
  "code": "CS101",
  "name": "Data Structures",
  "description": "Learn data structures and algorithms",
  "credits": 4,
  "total_hours": 60
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": { /* course object */ },
  "message": "Course created successfully"
}
```

---

### GET /courses/:courseId

Get course details.

**Response (200 OK):**
```json
{
  "success": true,
  "data": { /* course object */ }
}
```

---

### PATCH /courses/:courseId

Update course.

**Request Body:** (all fields optional)
```json
{
  "name": "Data Structures & Algorithms",
  "total_hours": 62
}
```

---

### DELETE /courses/:courseId

Delete course.

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Course deleted successfully"
}
```

---

## Students Endpoints

### GET /students

List all students.

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20)
- `batch`: Filter by batch year

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "roll_number": "CS001",
      "email": "student@college.edu",
      "full_name": "Alice Johnson",
      "batch": 2024,
      "is_active": true
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
```

---

### POST /students

Create/Add a new student.

**Request Body:**
```json
{
  "roll_number": "CS001",
  "email": "student@college.edu",
  "full_name": "Alice Johnson",
  "batch": 2024,
  "phone": "9876543210"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": { /* student object */ },
  "message": "Student created successfully"
}
```

---

### GET /students/:studentId

Get student details.

---

### PATCH /students/:studentId

Update student information.

---

### DELETE /students/:studentId

Delete student.

---

## Enrollment Endpoints

### GET /courses/:courseId/enrollments

List students enrolled in a course.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "student_id": 1,
      "course_id": 1,
      "student": {
        "roll_number": "CS001",
        "full_name": "Alice Johnson"
      },
      "status": "active",
      "enrolled_date": "2024-01-15"
    }
  ]
}
```

---

### POST /courses/:courseId/enrollments

Enroll students in a course.

**Request Body:**
```json
{
  "student_ids": [1, 2, 3]
}
```

---

### DELETE /courses/:courseId/enrollments/:enrollmentId

Remove a student from course.

---

## Attendance Endpoints

### GET /courses/:courseId/attendance

Get attendance records for a course.

**Query Parameters:**
- `date`: Filter by date (YYYY-MM-DD)
- `page`: Pagination

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "student_id": 1,
      "attendance_date": "2024-01-20",
      "status": "present",
      "student": {
        "roll_number": "CS001",
        "full_name": "Alice Johnson"
      }
    }
  ]
}
```

---

### POST /courses/:courseId/attendance/mark

Mark attendance for a class.

**Request Body:**
```json
{
  "attendance_date": "2024-01-20",
  "attendance": [
    { "student_id": 1, "status": "present" },
    { "student_id": 2, "status": "absent" },
    { "student_id": 3, "status": "leave" }
  ]
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Attendance marked successfully",
  "data": { /* attendance summary */ }
}
```

---

### GET /courses/:courseId/students/:studentId/attendance

Get attendance statistics for a student in a course.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "student_id": 1,
    "course_id": 1,
    "total_classes": 30,
    "present": 28,
    "absent": 2,
    "leave": 0,
    "attendance_percentage": 93.33
  }
}
```

---

## Grades Endpoints

### GET /courses/:courseId/grades

Get all grades for a course.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "enrollment_id": 1,
      "student": {
        "roll_number": "CS001",
        "full_name": "Alice Johnson"
      },
      "grades": [
        {
          "assessment_type": "CE",
          "marks_obtained": 28,
          "out_of": 30
        }
      ]
    }
  ]
}
```

---

### POST /courses/:courseId/grades

Add/Update grades for students.

**Request Body:**
```json
{
  "enrollments": [
    {
      "enrollment_id": 1,
      "grades": [
        {
          "assessment_type_id": 1,
          "marks_obtained": 28
        }
      ]
    }
  ]
}
```

---

### GET /courses/:courseId/students/:studentId/grade-summary

Get final grade for a student in a course.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "student_id": 1,
    "course_id": 1,
    "total_marks": 95,
    "percentage": 79.17,
    "grade": "A",
    "gpa": 3.67,
    "status": "pass"
  }
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "error": "Validation error",
  "details": {
    "email": "Email is required"
  }
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "error": "Unauthorized",
  "message": "Please provide valid authentication token"
}
```

### 403 Forbidden
```json
{
  "success": false,
  "error": "Forbidden",
  "message": "You don't have permission to access this resource"
}
```

### 404 Not Found
```json
{
  "success": false,
  "error": "Not found",
  "message": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "Server error",
  "message": "An unexpected error occurred"
}
```

---

## Rate Limiting

- Default: 100 requests per 15 minutes per IP
- Auth endpoints: 5 requests per 15 minutes

---

## Pagination

Default page size is 20. Maximum is 100.

```
GET /students?page=2&limit=50
```

---

## Timestamps

All timestamps are in ISO 8601 format (UTC):
```
2024-01-20T14:30:00Z
```

---

## To-Do

- [ ] Export grades to CSV/Excel
- [ ] Bulk operations (import students, grade sheet)
- [ ] Email notifications
- [ ] Advanced analytics endpoints
- [ ] Student dashboard endpoints
- [ ] Report generation endpoints
