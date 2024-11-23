from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global project_settings
    project_settings = settings.get_settings(env="test")

@app.get("/")
def root():
    return {"Hello": "World"}
