from fastapi import FastAPI

from src.routes import tasks

app = FastAPI(title="AI DevX Task API")

app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the AI DevX Task API", "status": "running"}
