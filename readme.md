# TaskFlow API

TaskFlow API is a RESTful task management backend built with FastAPI and PostgreSQL. It enables users to create, organize, update, and track tasks efficiently through a clean and scalable API.
## Key Highlights

- RESTful API built with FastAPI
- PostgreSQL persistence using SQLAlchemy ORM
- Dockerized database setup
- Input validation with Pydantic
- Automatic OpenAPI/Swagger documentation
- Clean layered architecture (routes, schemas, models, database)

## Features

* Create, read, update, and delete tasks (CRUD operations)
* Task status tracking (Pending, In Progress, Completed)
* PostgreSQL database integration
* FastAPI-powered high-performance REST API
* Data validation with Pydantic
* Automatic API documentation with Swagger UI
* Modular and maintainable project structure

## Tech Stack

- **Python 3.13**
- **FastAPI** – web framework
- **PostgreSQL** – database
- **SQLAlchemy** – ORM
- **Pydantic** – data validation
- **Docker** – local database setup

## API Endpoints

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| POST   | /tasks      | Create a new task        |
| GET    | /tasks      | Retrieve all tasks       |
| GET    | /tasks/{id} | Retrieve a specific task |
| PUT    | /tasks/{id} | Update a task            |
| DELETE | /tasks/{id} | Delete a task            |


## Project Structure
taskflow-api/

├── app/
│   ├── main.py          # App entry point
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── database.py       # DB connection setup
│   └── routes/
│       └── tasks.py      # Task CRUD endpoints
├── requirements.txt
└── README.md

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Taniyakaur/taskflow-api.git
cd taskflow-api
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start PostgreSQL with Docker
```bash
docker run --name taskflow-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=taskflow \
  -p 5433:5432 \
  -d postgres
```

### 5. Create a `.env` file
DATABASE_URL=postgresql://postgres:password@localhost:5433/taskflow

### 6. Run the server
```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get a single task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example Requests

**Create a task**
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Fix login bug", "description": "Users cant log in with Google", "status": "todo"}'
```

**List tasks**
```bash
curl http://localhost:8000/tasks
```

**Update a task**
```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "in_progress"}'
```

**Delete a task**
```bash
curl -X DELETE http://localhost:8000/tasks/1
```

## Database Schema

**Task**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| title | String | Task title |
| description | String | Optional task details |
| status | String | `todo`, `in_progress`, or `done` |
| created_at | DateTime | Auto-set on creation |

## Possible Improvements

- Filter tasks by status
- Basic authentication
- Pagination


## What I Learned

- Designing RESTful APIs with FastAPI
- Managing PostgreSQL databases
- Using SQLAlchemy ORM for database interactions
- Validating data with Pydantic models
- Containerizing services with Docker for easy deployment
- Structuring backend applications using clean architecture principles
