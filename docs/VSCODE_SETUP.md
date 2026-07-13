# Faculty ERP Setup Guide - Visual Studio Code

Complete step-by-step guide to setup Faculty ERP using Visual Studio Code.

## Prerequisites

- ✅ Visual Studio Code installed
- ✅ Node.js installed (v16+)
- ✅ Git installed

Check installations:
- Open VS Code Terminal: `Ctrl + ~`
- Run: `node --version` and `npm --version`

---

## Step 1: Open Project in VS Code

1. Open VS Code
2. Click **File** → **Open Folder**
3. Navigate to: `C:\Projects\GIT\FacultyERP`
4. Click **Select Folder**

You'll see the project structure on the left side.

---

## Step 2: Install PostgreSQL GUI (pgAdmin)

### Option A: Install pgAdmin (Recommended for Visual Setup)

1. Visit: https://www.pgadmin.org/download/
2. Download pgAdmin for Windows
3. Run installer and follow defaults
4. Launch pgAdmin (it opens in browser at `http://localhost:5050`)

### Option B: PostgreSQL + pgAdmin Bundle

1. Visit: https://www.postgresql.org/download/windows/
2. Download installer
3. During installation, **check "pgAdmin 4"**
4. Complete installation
5. Launch pgAdmin from Start Menu

---

## Step 3: Create Database with pgAdmin GUI

### 3.1 Open pgAdmin

1. Search for **pgAdmin** in Windows Start Menu
2. Click to open (opens in browser)
3. You may see a password prompt - set a master password

### 3.2 Connect to PostgreSQL Server

1. On left panel, click **Servers**
2. Right-click → **Register** → **Server**
3. Fill in:
   - **Name**: `PostgreSQL Local`
   - Click **Connection** tab
   - **Host name**: `localhost`
   - **Username**: `postgres`
   - **Password**: (your PostgreSQL password from installation)
4. Click **Save**

### 3.3 Create Database

1. Expand **Servers** → **PostgreSQL Local**
2. Right-click **Databases** → **Create** → **Database**
3. In "Database" field, type: `faculty_erp`
4. Click **Save**

---

## Step 4: Create Database Tables with pgAdmin GUI

### 4.1 Open Query Editor

1. In pgAdmin, click on **faculty_erp** database
2. Click **Tools** → **Query Tool** (or press Ctrl+Alt+Q)
3. A SQL editor window opens

### 4.2 Copy-Paste SQL Script

Copy this entire SQL script into the Query Tool:

```sql
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

### 4.3 Execute SQL

1. Select all SQL (Ctrl + A)
2. Click **Execute** button (▶️ icon) or press F5
3. Wait for "Query executed successfully"
4. Close Query Tool

---

## Step 5: Insert Test User

### 5.1 Open New Query

1. In pgAdmin, click **Tools** → **Query Tool** again
2. Paste this SQL:

```sql
INSERT INTO users (email, password_hash, full_name, role, department) 
VALUES ('teacher@college.edu', '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36DRcx3u', 'Dr. John Doe', 'faculty', 'Computer Science');
```

3. Click Execute (▶️) or press F5
4. You should see: "INSERT 0 1"

---

## Step 6: Setup Backend in VS Code

### 6.1 Open Terminal in VS Code

1. In VS Code, press **Ctrl + ~** (backtick)
2. Terminal opens at bottom

### 6.2 Navigate to Backend

Type in terminal:
```bash
cd backend
```

### 6.3 Create .env File

Right-click on **backend** folder → **New File** → Name it `.env`

Or in terminal:
```bash
code .env
```

This opens `.env` file in editor.

### 6.4 Copy Environment Variables

Paste this in `.env`:

```env
PORT=5000
NODE_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_NAME=faculty_erp
DB_USER=postgres
DB_PASSWORD=postgres
DB_POOL_MIN=2
DB_POOL_MAX=10

JWT_SECRET=your_super_secret_key_change_this_in_production
JWT_EXPIRE=7d

FRONTEND_URL=http://localhost:3000

LOG_LEVEL=info
```

⚠️ **Change `DB_PASSWORD` to your PostgreSQL password!**

Save: **Ctrl + S**

### 6.5 Install Backend Dependencies

In terminal (should be in `backend` folder):
```bash
npm install
```

Wait for installation to complete (1-2 minutes).

### 6.6 Start Backend Server

```bash
npm run dev
```

Expected output:
```
✓ Server running on port 5000
✓ Environment: development
✓ API URL: http://localhost:5000/api
```

**Keep this terminal running!**

---

## Step 7: Setup Frontend in VS Code

### 7.1 Open New Terminal

1. In VS Code, click **+** button next to terminal tab
2. New terminal opens

### 7.2 Navigate to Frontend

```bash
cd frontend
```

### 7.3 Create .env File

In terminal:
```bash
code .env
```

Paste:
```env
REACT_APP_API_URL=http://localhost:5000/api
```

Save: **Ctrl + S**

### 7.4 Install Frontend Dependencies

```bash
npm install
```

Wait for installation.

### 7.5 Start Frontend

```bash
npm start
```

Expected output:
```
✓ Compiled successfully!
✓ On Your Network: http://localhost:3000
```

Browser will automatically open at `http://localhost:3000`.

---

## Step 8: Login to Your App

### Login Page

You'll see a beautiful login page. Use:

- **Email**: `teacher@college.edu`
- **Password**: `password`

Click **Login**.

### Dashboard

After login, you'll see:
- Welcome message
- Your courses
- Dashboard stats

---

## 📁 VS Code Layout

You should now have:

**Terminal 1** (Backend - keep running):
```
✓ Server running on port 5000
```

**Terminal 2** (Frontend - keep running):
```
✓ Compiled successfully!
http://localhost:3000
```

**Browser**:
```
http://localhost:3000 - Faculty ERP Login
```

---

## 🔧 Useful VS Code Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + ~` | Toggle terminal |
| `Ctrl + S` | Save file |
| `Ctrl + Shift + D` | Debug view |
| `Ctrl + B` | Toggle sidebar |
| `Ctrl + /` | Comment/uncomment |
| `Ctrl + F` | Find |
| `F5` | Start debugging |

---

## 📝 Project Structure in VS Code

Click on file names to view code:

```
FacultyERP/
├── backend/
│   ├── src/
│   │   ├── server.js           ← Backend entry point
│   │   ├── app.js              ← Express setup
│   │   ├── config/database.js  ← DB connection
│   │   └── ...
│   ├── .env                    ← Your settings
│   └── package.json
│
└── frontend/
    ├── src/
    │   ├── pages/LoginPage.jsx ← Login UI
    │   ├── pages/DashboardPage.jsx ← Dashboard UI
    │   ├── App.jsx             ← Main component
    │   └── ...
    ├── .env                    ← Your settings
    └── package.json
```

---

## ✅ Verification Checklist

- [ ] pgAdmin opened and PostgreSQL connected
- [ ] Database `faculty_erp` created
- [ ] All tables created successfully
- [ ] Test user inserted
- [ ] Backend `.env` file created with correct password
- [ ] Backend `npm install` completed
- [ ] Backend running on port 5000 (`npm run dev`)
- [ ] Frontend `.env` file created
- [ ] Frontend `npm install` completed
- [ ] Frontend running on port 3000 (`npm start`)
- [ ] Browser shows login page
- [ ] Login successful with test credentials
- [ ] Dashboard displays

---

## 🆘 Troubleshooting in VS Code

### "Cannot find module" error in backend

```bash
cd backend
npm install
```

### Port 5000 already in use

In backend `.env`, change:
```env
PORT=5001
```

### Frontend not loading

1. Stop frontend: Press **Ctrl + C** in frontend terminal
2. Clear cache: `npm cache clean --force`
3. Restart: `npm start`

### Database connection failed

1. Check `DB_PASSWORD` in backend `.env`
2. Verify pgAdmin connection works
3. Check PostgreSQL service is running (Task Manager)

### Can't see database changes

1. In pgAdmin, right-click database → **Refresh**
2. Or press F5 in Query Tool

---

## 🚀 Next Steps

After successful login:

1. **Test Backend API** - Open `http://localhost:5000/api/health`
   - Should return: `{"status":"ok","timestamp":"..."}`

2. **Create Sample Data** - In pgAdmin Query Tool:
   ```sql
   INSERT INTO students (roll_number, email, full_name, batch) 
   VALUES ('CS001', 'student1@college.edu', 'Alice Johnson', 2024);
   ```

3. **Start Building Features** - See `docs/DEVELOPMENT.md`

---

## 📞 Getting Help

If you encounter errors:

1. Check terminal output for error messages
2. Copy the full error message
3. Check `docs/WINDOWS_SETUP.md` troubleshooting section
4. Share error message for help

---

**Happy coding! You're all set up! 🎉**
