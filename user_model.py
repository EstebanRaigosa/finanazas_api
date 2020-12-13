from pydantic import BaseModel

class userIn(BaseModel): #GET
    id: int
    name: str
    password: str
    email: str

class userOut(BaseModel): #POST/
    name: str
    password: str
    email: str