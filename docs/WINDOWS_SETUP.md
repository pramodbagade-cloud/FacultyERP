# PostgreSQL Installation & Setup Guide for Windows

## Step 1: Download PostgreSQL

### Using Windows Package Manager (Recommended - Fastest)

Open **Command Prompt** as Administrator and run:

```cmd
winget install PostgreSQL.PostgreSQL
```

### Alternative: Direct Download

1. Visit https://www.postgresql.org/download/windows/
2. Click "Download the installer"
3. Choose version 15 or latest
4. Run the installer

---

## Step 2: Complete Installation Setup

During PostgreSQL installation:
- ✅ Keep default port: `5432`
- ✅ Set password for `postgres` user (remember this!)
- ✅ Install pgAdmin 4 (helpful GUI tool)
- ✅ Add to PATH (important!)

---

## Step 3: Verify PostgreSQL Installation

Open **Command Prompt** and run:

```cmd
psql --version
```

Expected output:
```
psql (PostgreSQL) 15.x (Windows XX-bit)
```

If you see this error:
```
'psql' is not recognized...
```

Add PostgreSQL to your PATH manually:
1. Win + R, type `sysdm.cpl`
2. Go to **Advanced** ��� **Environment Variables**
3. Add PostgreSQL bin folder: `C:\Program Files\PostgreSQL\15\bin`
4. Restart Command Prompt

---

## Step 4: Create Faculty ERP Database

Open **Command Prompt** and run:

```cmd
psql -U postgres
```

It will ask for password (enter the password you set during installation).

Then copy-paste this entire SQL script:

```sql
CREATE DATABASE faculty_erp;
\c faculty_erp

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'faculty',
    department VARCHAR(100),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    faculty_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    code VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    credits INTEGER,
    total_hours INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    roll_number VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    batch INTEGER,
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrolled_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    UNIQUE(student_id, course_id)
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    enrollment_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'absent',
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

CREATE TABLE assessment_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(50) NOT NULL UNIQUE,
    max_marks INTEGER NOT NULL,
    weight_percentage DECIMAL(5, 2),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    enrollment_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    assessment_type_id INTEGER NOT NULL,
    marks_obtained DECIMAL(5, 2),
    out_of INTEGER,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    FOREIGN KEY (assessment_type_id) REFERENCES assessment_types(id)
);

CREATE TABLE grade_summary (
    id SERIAL PRIMARY KEY,
    enrollment_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    total_marks DECIMAL(5, 2),
    percentage DECIMAL(5, 2),
    grade VARCHAR(2),
    gpa DECIMAL(4, 2),
    status VARCHAR(50) DEFAULT 'pending',
    calculated_at TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

INSERT INTO assessment_types (name, code, max_marks, weight_percentage) VALUES
('Continuous Evaluation', 'CE', 30, 30),
('Mid Semester', 'MS', 30, 30),
('End Semester', 'ES', 40, 40);

INSERT INTO sessions (name, description, start_date, end_date, is_active) VALUES
('Spring 2024', 'Spring Semester 2024', '2024-01-15', '2024-05-31', true);
```

After pasting, press `Enter` and wait for all commands to complete.

Exit psql:
```sql
\q
```

---

## Step 5: Create Test User

Open Command Prompt and run:

```cmd
psql -U postgres -d faculty_erp
```

Then paste this SQL:

```sql
INSERT INTO users (email, password_hash, full_name, role, department) 
VALUES ('teacher@college.edu', '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36DRcx3u', 'Dr. John Doe', 'faculty', 'Computer Science');
```

Exit:
```sql
\q
```

---

## Step 6: Update Backend Configuration

Navigate to backend folder:

```cmd
cd C:\Projects\GIT\FacultyERP\backend
```

Create `.env` file (copy from `.env.example`):

```cmd
copy .env.example .env
```

Edit `.env` file with notepad:

```cmd
notepad .env
```

Update these values:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=faculty_erp
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
JWT_SECRET=your_super_secret_key_12345
```

Save and close.

---

## Step 7: Install Backend Dependencies

In Command Prompt (in backend folder):

```cmd
npm install
```

This will install all required packages.

---

## Step 8: Start Backend Server

In the same Command Prompt:

```cmd
npm run dev
```

Expected output:
```
✓ Server running on port 5000
✓ Environment: development
✓ API URL: http://localhost:5000/api
```

---

## Step 9: Setup Frontend (NEW Command Prompt)

Open a **new Command Prompt** and navigate to frontend:

```cmd
cd C:\Projects\GIT\FacultyERP\frontend
```

Copy environment file:

```cmd
copy .env.example .env
```

Install dependencies:

```cmd
npm install
```

Start frontend:

```cmd
npm start
```

Expected output:
```
✓ Compiled successfully!
✓ On Your Network: http://localhost:3000
```

Browser will automatically open with login page.

---

## Step 10: Login

On the login page, use:
- **Email**: `teacher@college.edu`
- **Password**: `password`

---

## 🎯 Quick Command Reference

```cmd
# Install PostgreSQL
winget install PostgreSQL.PostgreSQL

# Verify installation
psql --version

# Connect to PostgreSQL
psql -U postgres

# Connect to faculty_erp database
psql -U postgres -d faculty_erp

# Navigate to backend
cd C:\Projects\GIT\FacultyERP\backend

# Install dependencies
npm install

# Start backend
npm run dev

# Navigate to frontend (new cmd)
cd C:\Projects\GIT\FacultyERP\frontend

# Install dependencies
npm install

# Start frontend
npm start
```

---

## ✅ Final Checklist

- [ ] PostgreSQL installed and running
- [ ] Database `faculty_erp` created
- [ ] All tables created
- [ ] Test user inserted
- [ ] Backend `.env` file configured
- [ ] Backend dependencies installed (`npm install`)
- [ ] Backend running on port 5000 (`npm run dev`)
- [ ] Frontend dependencies installed (`npm install`)
- [ ] Frontend running on port 3000 (`npm start`)
- [ ] Login successful with test credentials

---

## 🆘 Troubleshooting

### psql command not found
```cmd
# Add to PATH manually or reinstall PostgreSQL with "Add to PATH" checked
```

### Can't connect to database
```cmd
# Check PostgreSQL service is running
services.msc
# Look for "postgresql-x64-XX" and ensure it's running
```

### Port 5432 already in use
```cmd
# Change DB_PORT in backend .env to another port (5433, 5434, etc)
```

### npm install fails
```cmd
npm cache clean --force
del package-lock.json
npm install
```

---

## 📞 Need Help?

Copy any error message and share it. I'll help troubleshoot!

---

**Start with Step 1 and follow sequentially!** 🚀
