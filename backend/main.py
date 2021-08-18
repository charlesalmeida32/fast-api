from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.Project_version)

@app.get('/')
def hello_api():
    return {'hey':'hello'}