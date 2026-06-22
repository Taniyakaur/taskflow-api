from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

# Define the Task model, which represents the "tasks" table in the database
class Task(Base):
    __tablename__ = "tasks"  #table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each task
    title = Column(String, nullable=False)  # Title of the task (required)
    description = Column(String, nullable=True)  # Description of the task (optional)
    status = Column(String, default="todo")  # Status of the task, default is "todo"
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp when the task is created