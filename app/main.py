from fastapi import FastAPI
from app.routes import documents

app = FastAPI(title="Document Management API")
app.include_router(documents.router, prefix="/documents", tags=["documents"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}