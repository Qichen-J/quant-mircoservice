# task-microservice

A Flask-based task management microservice example, covering:

* RESTful CRUD API
* SQLite ORM (SQLAlchemy)
* Unit testing (pytest)
* Docker containerization
* GitHub Actions CI

---

## Project Overview

This project demonstrates how to build a simple microservice from scratch, including:

1. **Flask** for HTTP API
2. **SQLAlchemy** for data persistence
3. **pytest** for automated unit tests
4. **Docker** for packaging and deployment
5. **GitHub Actions** for continuous integration

---

## Requirements

* Python 3.8 or higher
* Docker (optional)
* GitHub account (for CI)

---

## Local Setup

1. Clone the repository and navigate into it

   ```bash
   git clone https://github.com/<your-username>/quant-microservice.git
   cd quant-microservice
   ```

2. Create and activate a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   # venv\Scripts\activate   # Windows PowerShell (optional)
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the service

   ```bash
   python app.py
   ```

   The API is available at `http://127.0.0.1:5000`:

   * `POST /tasks` – Create a new task
   * `GET  /tasks` – Retrieve all tasks
   * `GET  /tasks/{id}` – Retrieve a single task by ID
   * `PUT  /tasks/{id}` – Update a task
   * `DELETE /tasks/{id}` – Delete a task

---

## Unit Testing

Run tests with pytest:

```bash
pytest -q
```

You should see `..` indicating two tests passed.

---

## Docker Deployment

1. Build the Docker image

   ```bash
   docker build -t quant-service:latest .
   ```

2. Run the Docker container

   ```bash
   docker run -d -p 5000:5000 --name quant-svc quant-service:latest
   ```

3. Test the API

   ```bash
   curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title":"Docker Task Example"}'
   ```

---

## CI/CD (GitHub Actions)

A workflow is defined in `.github/workflows/ci.yml`, which runs on every push and pull request to `main`:

1. Install dependencies
2. Run pytest
3. Build the Docker image (without pushing to a registry)

---

## Project Structure

```
quant-microservice/
├── app.py                   # Flask application entrypoint
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image build script
├── tests/
│   └── test_app.py          # Unit tests
└── .github/
    └── workflows/
        └── ci.yml           # CI workflow configuration
```

