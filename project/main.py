from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from models.user import User
from routers import user,question,trivia, trivia_participation
from utils.startup_database import startup_database

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    startup_database()




app.include_router(user.router)
app.include_router(question.router)
app.include_router(trivia.router)
app.include_router(trivia_participation.router)
