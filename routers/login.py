from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

class User(BaseModel):
    username: str
    name: str
    active: bool

class UserDB(User):
    password : str 


UserDB = [{ "username": "jesus",
            "name" : "jesus gomez",
            "active" : True,
            "password" : "123456"

          }]


@app.get("/")
async def loggin():
    return "hola"