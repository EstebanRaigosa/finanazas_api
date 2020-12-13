from fastapi import FastAPI 
from pydantic import BaseModel
from user_model import userIn,userOut
from user_db import User, get_userById, get_userByName
from user_db import update_user
from fastapi import HTTPException

app = FastAPI()

@app.get("/user/{user_id}")
async def user_get(user_id: int):
    user_in = get_userById(user_id)            
    if user_in == None:
        raise HTTPException (status_code=404,
                detail="El usuario con la id " +user_id+" no fue encontrado")
    user_out = userOut(**user_in.dict())
    return user_out

@app.get("/user_name/{user_name}")
async def user_getByName(user_name: str):
    user_in = get_userByName(user_name)
    if user_in == None:
        raise HTTPException (status_code=404,
                detail="El usuario " +user_name+ " no fue encontrado")
    user_out = userOut(**user_in.dict())
    return user_out

@app.put("/user")
async def user_update(user: userIn): #user = objeto que mandan 
    user_in = get_userById(user.id)  #user_in = objeto base de datos 
    if user_in == None:        
        return None
    user_in.name = user.name
    user_in.password = user.password
    user_in.email = user.email
    update_user(user_in)
    user_out = userOut(**user_in.dict())
    return user_out





