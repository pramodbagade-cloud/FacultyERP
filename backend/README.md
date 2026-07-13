# Faculty ERP - Backend

Express.js backend API for Faculty ERP system.

## Setup

```bash
npm install
cp .env.example .env
# Edit .env with your database credentials
```

## Running

```bash
# Development
npm run dev

# Production
npm start
```

## API

API documentation: See `../../docs/API.md`

Base URL: `http://localhost:5000/api`

## Testing

```bash
npm test
npm run test:watch
```

## Project Structure

```
src/
├── server.js          # Express server entry point
├── app.js            # Express app setup
├── config/           # Configuration files
├── middleware/       # Express middleware
├── routes/           # API routes (to be created)
├── controllers/      # Route handlers (to be created)
├── services/         # Business logic (to be created)
├── models/           # Database models (to be created)
└── utils/            # Helper functions
```

## Next Steps

1. Setup PostgreSQL database
2. Create database tables (see `docs/DATABASE.md`)
3. Implement authentication routes
4. Implement CRUD routes
5. Add tests
