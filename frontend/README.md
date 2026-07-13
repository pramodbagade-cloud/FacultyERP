# Faculty ERP - Frontend

React frontend application for Faculty ERP system.

## Setup

```bash
npm install
cp .env.example .env
```

## Running

```bash
npm start
```

The app will open at `http://localhost:3000`

## Building for Production

```bash
npm run build
```

## Project Structure

```
src/
├── pages/           # Page components
├── components/      # Reusable components (to be created)
├── services/        # API calls
├── hooks/           # Custom hooks (to be created)
├── App.jsx         # Main App component
└── index.js        # Entry point
```

## Key Features

- Login/Authentication
- Dashboard with course overview
- Student management (to be implemented)
- Attendance tracking (to be implemented)
- Grade management (to be implemented)

## Dependencies

- **React**: UI library
- **React Router**: Routing
- **Axios**: HTTP client
- **Tailwind CSS**: Styling
- **React Icons**: Icon library

## Environment Variables

- `REACT_APP_API_URL`: Backend API URL (default: `http://localhost:5000/api`)
