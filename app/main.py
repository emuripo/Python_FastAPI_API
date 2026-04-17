from fastapi import FastAPI
from app.routes import task

app = FastAPI(title="Task API", description="API for managing tasks", version="1.0.0")
app.include_router(task.router, prefix="/tasks", tags=["tasks"])

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy"}