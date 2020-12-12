from pydantic import BaseModel

class userIn(BaseModel): #GET
    name: str
    password: str
    role: str

class userOut(BaseModel): #POST/
    id: int
    name: str
    password: str
    role: str