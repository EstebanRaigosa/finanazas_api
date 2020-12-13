from fastapi import FastAPI 
from pydantic import BaseModel
from user_model import userIn,userOut
from user_db import User
from user_db import get_user,update_user
from fastapi import HTTPException

app = FastAPI()

@app.get("/user/{user_id}")
async def user_get(user_id: int):
    user_in = get_user(user_id)
    if user_in == None:
        raise HTTPException (status_code=404,
                detail="El item no fue encontrado")
    user_out = userOut(**user_in.dict())
    return user_out

@app.put("/user")
async def user_update(user: userIn):
    user_in = get_user(user.id)
    if user_in == None:        
        return None
    #if item_in.name == user.name:
    #   raise HTTPException(status_code=303,
    #                     detail="El usuario ya existe")
    user_in.name = user.name
    user_in.password = user.password
    user_in.email = user.email
    update_user(user_in)
    user_out = userOut(**user_in.dict())
    return user_out





