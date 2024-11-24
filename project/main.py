from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.user import User
from config import settings
from routers import user,question

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global project_settings
    project_settings = settings.get_settings(env="test")



@app.get("/")
def root():
    return {"Hello": "World"}



app.include_router(user.router)
app.include_router(question.router)
