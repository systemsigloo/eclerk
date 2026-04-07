
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import user, login


#pip3.14 install "pwdlib[argon2]"
#pip3.14 install pyjwt   

app = FastAPI()

app.include_router(user.router)
app.include_router(login.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}   

@app.get("/jesus")
async def root():
    return {"message": "todo va a salir bien"}   



