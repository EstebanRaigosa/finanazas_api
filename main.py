from fastapi import FastAPI 
from pydantic import BaseModel
from user_model import userIn,userOut
from user_db import User
from user_db import get_user,update_user
from fastapi import HTTPException

app = FastAPI()

@app.get("/login/{user_name}")
async def user_get(user_name: str):
    user_in = get_user(user_name)
    if user_in == None:
        raise HTTPException (status_code=404,
                detail="El item no fue encontrado")
    user_out = userOut(**user_in.dict())
    return user_out

@app.put("/register")
async def user_update(user: userIn):
    user_in = get_user(user.name)
    if user_in == None:        
        return None
    #if item_in.name == user.name:
     #   raise HTTPException(status_code=303,
    #                     detail="El usuario ya existe")
    
    
    user_in.name = user.name
    user_in.password = user.password
    user_in.role = user.role
    update_user(user_in)
    user_out = userOut(**user_in.dict())
    return user_out





