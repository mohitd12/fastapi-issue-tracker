# FastAPI Issue Tracker

A mini production-style REST API built with FastAPI for tracking issues. This project demonstrates core FastAPI concepts including routing, data validation with Pydantic, CRUD operations, and file-based persistence.

## Features

- Full CRUD operations for issues
- Data validation with `Pydantic` schemas
- UUID generation for issue IDs
- Priority levels (low, medium, high)
- Status tracking (open, in_progress, closed)
- Custom JSON file-based storage
- Auto-generated Swagger API documentation
- Custom middleware (timer, CORS)

## Requirements

- Python 3.9+

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mohitd12/fastapi-issue-tracker.git
cd fastapi-issue-tracker
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install "fastapi[standard]"
```

## Running the API

Start the development server:

```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

| Method | Endpoint                  | Description          |
| ------ | ------------------------- | -------------------- |
| GET    | `/api/health`          | Health check         |
| GET    | `/api/issues`          | Get all issues       |
| GET    | `/api/issues/{id}`     | Get issue by ID      |
| POST   | `/api/issues`          | Create a new issue   |
| PUT    | `/api/issues/{id}`     | Update an issue      |
| DELETE | `/api/issues/{id}`     | Delete an issue      |

## Middleware

This project includes custom middleware to demonstrate the middleware pattern in FastAPI.

### Timer Middleware

Adds an `X-Process-Time` header to all responses showing how long the request took to process:

```python
# app/middleware/timer.py
async def timer_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}s"
    return response
```

### CORS Middleware

Enables cross-origin requests from frontend applications:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Project Structure

```
fastapi-issue-tracker/
├── main.py              # Application entry point
├── app/
│   ├── schemas.py       # Pydantic models for validation
│   ├── storage.py       # JSON file storage functions
│   ├── middleware/
│   │   └── timer.py     # Response timer middleware
│   └── routes/
│       └── issues.py    # Issue CRUD endpoints
├── data/
    └── issues.json      # Data storage (auto-created)
```

## License

MIT