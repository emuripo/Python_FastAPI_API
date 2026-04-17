import uuid
from app.db.fake_db import task_db

class TaskService:
    @staticmethod
    async def create_task(title: str, description: str = None):
        task_id = str(uuid.uuid4())
        
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "completed": False
        }
        
        task_db[task_id] = task
        return task
    
    @staticmethod
    async def list_tasks():
        return list(task_db.values())
    @staticmethod
    async def get_task(task_id: str):
        return task_db.get(task_id)
    @staticmethod
    async def update_task(task_id: str, data: dict):
        task = task_db.get(task_id)
        if not task:
            return None
        for key, value in data.items():
            if value is not None:
                task[key] = value
        return task
    @staticmethod
    async def delete_task(task_id: str):
        return task_db.pop(task_id, None)