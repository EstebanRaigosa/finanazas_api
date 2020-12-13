from typing import Dict
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    password: str
    email: str

database_users = Dict[int, User]
database_users = {  1 :User(**{"id":1,
                            "name": "Paola",
                            "password": "1234",
                            "email": "p@correo.com" }),
                    2 :User(**{"id":2,
                            "name": "Francisco",
                            "password": "250ss3fd",
                            "email" : "f@correo.com"}),
                    3: User(**{"id":3,
                            "name": "Ivan",
                            "password": "sfsf",
                            "email" : "IdeIvan@correo.com"})  
                            }


def get_userById(llave: int):
    if llave in database_users.keys():
        return database_users[llave]
    else:
        return None

def get_userByName(llave: str):
    i = 1
    while i <= len(database_users):
            if database_users[i].name == llave:
                    return database_users[i]
            i+=1
def count_Repeteat(llave: str):
    cont = 0
    i = 1
    while i <= len(database_users):
            if database_users[i].name == llave:
                    cont+=1
            i+=1
    return cont

def update_user(user: User):
    database_users[user.id] = user
    return user