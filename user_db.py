from typing import Dict
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    password: str
    role: str

database_users = Dict[int, User]
database_users = {  "Paola":User(**{"id":1,
                            "name": "Paola",
                            "password": "1234",
                            "role": "user" }),
                    "Francisco":User(**{"id":2,
                            "name": "Francisco",
                            "password": "250",
                            "role": "user"}),  
                            }

def get_user(llave: str):
    if llave in database_users.keys():
        return database_users[llave]
    else:
        return None

def update_user(user: User):
    database_users[user.name] = user
    return user