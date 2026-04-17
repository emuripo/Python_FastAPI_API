# Interview-Style Prompt

# "Build a simple REST API using Python and FastAPI to manage tasks. The API should allow:
- creating a task,
- listing tasks,
- retrieving a task by id,
- updating its status,
- and deleting a task."

# Project Structure
app/
├── main.py
├── routes/
│   └── tasks.py
├── schemas/
│   └── task.py
├── services/
│   └── task_service.py
└── db/
    └── fake_db.py

# Why this structure

Because it gives you:

- clear separation
- speed
- an easier structure to explain

I would not add `repositories/` or `integrations/` here unless you have extra time.

# Main entity

The main entity is `Task`.

Reasonable fields:
- `id`
- `title`
- optional `description`
- `completed`

# Expected endpoints
Minimum:
GET /health
POST /tasks
GET /tasks
GET /tasks/{task_id}
PATCH /tasks/{task_id}
DELETE /tasks/{task_id}

# Phases to follow from start to finish

# Phase 1 — understand the challenge
Ask yourself these questions mentally:

What is the entity? → `Task`
What operations are required? → partial CRUD
Do I need a real database? → no
Do I need complex async behavior? → no, but FastAPI can still be async

# Phase 2 — create the skeleton
Create:
- `main.py`
- an empty router
- the `/health` endpoint
- Objective

Get the API running first.

Recommended commands if the project uses `.venv`:

```powershell
cd "C:\Users\esteb\Desktop\Code Challenges\Python_Apis\API_code_challenge_1"
.\.venv\Scripts\Activate.ps1
python -m pip install fastapi uvicorn pydantic
python -m uvicorn app.main:app --reload
```

Recommended commands if the project does not use `.venv`:

```powershell
cd "C:\path\to\your\project"
python -m pip install fastapi uvicorn pydantic
python -m uvicorn app.main:app --reload
```

Safer version using the absolute Python path from `.venv`:

```powershell
cd "C:\Users\esteb\Desktop\Code Challenges\Python_Apis\API_code_challenge_1"
& "C:\Users\esteb\Desktop\Code Challenges\Python_Apis\API_code_challenge_1\.venv\Scripts\python.exe" -m pip install fastapi uvicorn pydantic
& "C:\Users\esteb\Desktop\Code Challenges\Python_Apis\API_code_challenge_1\.venv\Scripts\python.exe" -m uvicorn app.main:app --reload
```

# Phase 3 — define the contract
Create schemas:

- `TaskCreate`
- `TaskResponse`
- `TaskUpdate`

Define clearly what comes in and what goes out.

Useful command to verify `pydantic` is installed when using `.venv`:

```powershell
& "C:\Users\esteb\Desktop\Code Challenges\Python_Apis\API_code_challenge_1\.venv\Scripts\python.exe" -c "import pydantic; print(pydantic.__version__)"
```

Equivalent command without `.venv`:

```powershell
python -c "import pydantic; print(pydantic.__version__)"
```

# Phase 4 — simple storage
Create `fake_db.py`:
- `tasks_db = {}`

# Phase 5 — business logic

Create `TaskService` with functions:

- `create_task`
- `list_tasks`
- `get_task`
- `update_task`
- `delete_task`
- Objective

Do not put business logic in the router.

# Phase 6 — connect endpoints
- Implement routes and error handling.

# Phase 7 — validate the full flow
Test:

- create
- list
- get by id
- update
- delete
- 404 case

Useful commands for validation with the server running:

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health | Select-Object -ExpandProperty Content
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/tasks | Select-Object -ExpandProperty Content
```

You can also validate interactively in Swagger at:

```text
http://127.0.0.1:8000/docs
```

# Phase 8 — final explanation
Be ready to explain:

- why that structure
- how you would scale it
- what you would change in production

# Specific checklist for this challenge
1. Setup
[] create `main.py`
[] create `tasks.py`
[] start the app
[] test `/health`
[] know whether the project uses `.venv` or global Python

2. Contract
[] create `TaskCreate`
[] create `TaskResponse`
[] create `TaskUpdate`

3. Data
[] create `tasks_db = {}`

4. Logic
[] create
[] list
[] get by id
[] update
[] delete

5. Validation
[] return 404 if not found
[] clear response format
[] test the flow in Swagger

# Your mental framework for this kind of challenge
Entity → Schema → Storage → Service → Routes → Test