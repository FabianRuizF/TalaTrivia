from fastapi import FastAPI
from config import settings

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global settings
    settings = get_settings(env="dev")

@app.get("/")
def root():
    return {"Hello": "World"}
