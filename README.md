# Universal FastAPI Interview Framework

Guide for solving API technical challenges with Python and FastAPI in a clean, fast, and explainable way.

## Purpose

This framework is designed for real interview-style backend challenges. The goal is to help you:

- move fast
- structure the solution clearly
- avoid overengineering
- explain decisions like a senior engineer
- adapt to different API challenge types

Typical prompts may ask you to build:

- a CRUD API
- a document processing API
- a search API
- an AI-oriented API
- a mixed workflow API

## Golden Rule

In technical interviews:

> Working + clean + explainable beats complex + incomplete.

Your priorities should be:

1. Make it run.
2. Make it clear.
3. Make it easy to explain.

## Part 1: Foundations

### First Step: Classify the Challenge

Before coding, identify what kind of API you are dealing with.

#### A. CRUD API

Examples:

- tasks
- users
- products
- orders
- books

Typical operations:

- create
- list
- get by id
- update
- delete

#### B. Workflow / Processing API

Examples:

- upload document
- process text
- generate chunks
- convert files
- check processing status

Typical operations:

- create resource
- process resource
- retrieve status
- retrieve result

#### C. Search API

Examples:

- search products
- search documents
- filter users
- query tasks

Typical operations:

- receive query
- optionally apply filters
- return matching results

#### D. AI-Oriented API

Examples:

- summarize text
- chunk text
- embedding placeholder
- retrieval pipeline
- prompt execution

Typical characteristics:

- processing logic
- async-oriented thinking
- external integration placeholders
- future extensibility

#### E. Mixed API

Examples:

- CRUD + Search
- CRUD + Workflow
- Workflow + Search
- AI + Processing + Search

### Identify the Main Entity

Once you identify the API type, define the main entity.

#### Task

Reasonable fields:

- id
- title
- description
- completed

#### Document

Reasonable fields:

- id
- title
- content
- status

#### Product

Reasonable fields:

- id
- name
- description
- price
- stock

### Default Project Structure

Use this by default for most interview challenges:

```text
app/
├── main.py
├── routes/
├── schemas/
├── services/
└── db/
```

Why this structure works well:

- clear separation of concerns
- speed during the interview
- easy to explain
- flexible enough for most API challenges

### Folder Responsibilities

#### `main.py`

Application entry point.

Responsibilities:

- create the FastAPI app
- register routes
- expose the health endpoint

#### `routes/`

HTTP layer only.

Responsibilities:

- define endpoints
- receive request data
- return responses
- raise HTTP errors when needed

#### `schemas/`

Contract layer.

Responsibilities:

- request validation
- response structure
- typed models with Pydantic

#### `services/`

Business logic layer.

Responsibilities:

- implement actual behavior
- keep routes thin
- centralize logic for reuse

#### `db/`

Temporary in-memory storage.

Responsibilities:

- fake persistence for interview exercises
- avoid losing time with real database setup

### Extended Structure: Only If Needed

Use extra folders only if the challenge clearly requires more complexity:

```text
app/
├── main.py
├── routes/
├── schemas/
├── services/
├── repositories/
├── integrations/
├── core/
└── db/
```

When to add more folders:

#### `repositories/`

Add when:

- real database access is needed
- persistence should be separated from business logic

#### `integrations/`

Add when:

- Azure/OpenAI/Blob/Search is required
- the challenge explicitly mentions external services

#### `core/`

Add when:

- config management is needed
- environment variables are needed
- logging is needed

### Universal Mental Model

For almost every API interview challenge, think in this order:

```text
Entity → Schema → Storage → Service → Routes → Test
```

### High-Level Interview Strategy

Always optimize for:

- speed
- clarity
- correctness
- explainability

Avoid trying to impress with unnecessary complexity.

A practical way to explain your approach is:

> I want to get the API running first, then define the contract, then connect the business logic incrementally.

## Part 2: Execution Phases

### Phase 1: Understand the Challenge

Before coding, stop for a few seconds and answer these questions mentally:

- What is the main entity?
- What operations are required?
- Is it CRUD?
- Is there processing logic?
- Is search required?
- Is status tracking required?
- Do I need a real database?
- Do I need async behavior?
- What is the minimum working version?

#### Example Thinking: Task Challenge

Prompt:

> Build a simple API to manage tasks.

Mental model:

- Entity = Task
- CRUD = yes
- Search = no
- DB = not required
- Use fake storage

#### Example Thinking: Document Challenge

Prompt:

> Build an API to upload and process documents.

Mental model:

- Entity = Document
- CRUD = partial
- Processing = yes
- Status = yes
- Output = chunks or results
- Fake storage is enough

#### Example Thinking: Search Challenge

Prompt:

> Build an API to search products.

Mental model:

- Entity = Product
- Search = yes
- Filters = maybe
- No heavy persistence needed

#### Goal of Phase 1

Know what not to build.

Time is limited in interviews. Avoid building things that were never requested.

### Phase 2: Create the Skeleton

Always start by making the project run.

Create:

- `main.py`
- one route file
- `/health`

Goal:

Have a running API immediately.

#### Universal `main.py` Template

```python
from fastapi import FastAPI
from app.routes import items

app = FastAPI(title="Interview API")

app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/health")
async def health():
    return {"status": "ok"}
```

Replace:

- `items`
- `Items`

with the real entity name, for example:

- `tasks`
- `documents`
- `products`
- `users`

#### Universal Route Template

Create a route file such as `app/routes/items.py`:

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_items():
    return {"message": "route works"}
```

This confirms routing works before adding logic.

#### Why This Is Smart

Many candidates lose time building logic before confirming that:

- imports work
- folders work
- routes load
- FastAPI starts correctly

#### Commands on Windows with `.venv`

```powershell
cd "C:\path\to\project"
.\.venv\Scripts\Activate.ps1
python -m pip install fastapi uvicorn pydantic
python -m uvicorn app.main:app --reload
```

#### Commands Without `.venv`

```powershell
cd "C:\path\to\project"
python -m pip install fastapi uvicorn pydantic
python -m uvicorn app.main:app --reload
```

#### Safer Version Using the Absolute Python Path

```powershell
cd "C:\path\to\project"
& ".\.venv\Scripts\python.exe" -m pip install fastapi uvicorn pydantic
& ".\.venv\Scripts\python.exe" -m uvicorn app.main:app --reload
```

#### Validation Immediately After Startup

Open:

- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

Expected:

For `/health`:

```json
{
  "status": "ok"
}
```

For `/docs`:

- Swagger UI loads successfully

#### Why Swagger Matters in Interviews

Swagger gives you:

- fast endpoint testing
- visible schemas
- visible professionalism
- easier demos during the interview

#### Goal of Phase 2

At the end of this phase you should have:

- project starts
- docs work
- route imports work
- health endpoint works

That means the skeleton is complete.

#### Common Errors and Fixes

##### Error: `No module named app`

Cause:

- running the command from the wrong folder

Fix:

- run from the project root

##### Error: Route import fails

Cause:

- wrong file name or missing `router`

Fix:

Check files like:

- `routes/tasks.py`
- `routes/documents.py`

and make sure the import matches the file name and the file exposes `router = APIRouter()`.

##### Error: FastAPI highlighted in the editor

Cause:

- wrong interpreter selected

Fix:

- select the correct Python environment in VS Code

#### What to Say in an Interview

If something small fails, a practical answer is:

> Looks like the local interpreter is different. Let me quickly align the environment and continue.

#### Golden Rule of Phase 2

Do not move to business logic until:

- the API runs
- `/docs` works
- the route loads

### Phase 3: Define the Contract

Create the schemas first.

Typical examples:

- `TaskCreate`
- `TaskResponse`
- `TaskUpdate`

Define clearly what comes in and what goes out.

Useful check for `pydantic`:

```powershell
python -c "import pydantic; print(pydantic.__version__)"
```

If the project uses `.venv`, the safer version is:

```powershell
& ".\.venv\Scripts\python.exe" -c "import pydantic; print(pydantic.__version__)"
```

### Phase 4: Add Simple Storage

Start with something simple, for example in `fake_db.py`:

```python
tasks_db = {}
```

### Phase 5: Add Business Logic

Create a service such as `TaskService` with functions like:

- `create_task`
- `list_tasks`
- `get_task`
- `update_task`
- `delete_task`

Do not put business logic in the router.

### Phase 6: Connect Endpoints

Implement the routes and HTTP error handling.

### Phase 7: Validate the Full Flow

Test:

- create
- list
- get by id
- update
- delete
- 404 case

Useful commands while the server is running:

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health | Select-Object -ExpandProperty Content
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/tasks | Select-Object -ExpandProperty Content
```

You can also validate interactively in Swagger:

```text
http://127.0.0.1:8000/docs
```

### Phase 8: Final Explanation

Be ready to explain:

- why you chose that structure
- how you would scale it
- what you would change in production

## Quick Checklist

### 1. Setup

- create `main.py`
- create the route file
- start the app
- test `/health`
- identify whether the project uses `.venv` or global Python

### 2. Contract

- create `TaskCreate`
- create `TaskResponse`
- create `TaskUpdate`

### 3. Data

- create `tasks_db = {}`

### 4. Logic

- create
- list
- get by id
- update
- delete

### 5. Validation

- return 404 if not found
- keep the response format clear
- test the flow in Swagger

## Reusable Mental Framework

```text
Entity → Schema → Storage → Service → Routes → Test
```