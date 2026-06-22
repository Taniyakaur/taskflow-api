from pydantic import BaseModel  # Base class for creating Pydantic models
from datetime import datetime  
from typing import Optional  # For optional fields

# Schema for creating a new task
class TaskCreate(BaseModel):
    title: str  # Title of the task (required)
    description: Optional[str] = None  # Optional description of the task
    status: Optional[str] = "todo"  # Optional status, default is "todo"

# Schema for updating an existing task
class TaskUpdate(BaseModel):
    title: Optional[str] = None  # Optional title for updating
    description: Optional[str] = None  # Optional description for updating
    status: Optional[str] = None  # Optional status for updating

# Schema for returning task data to the client
class TaskOut(BaseModel):
    id: int  # Unique identifier of the task
    title: str  # Title of the task
    description: Optional[str]  # Optional description of the task
    status: str  # Status of the task
    created_at: datetime  # Timestamp when the task was created

    class Config:
        from_attributes = True  # Enables ORM mode to map attributes from SQLAlchemy models