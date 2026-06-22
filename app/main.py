from fastapi import FastAPI
from app.database import engine, Base
from app.routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "TaskFlow API is running"}