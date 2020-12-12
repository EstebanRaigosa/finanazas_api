from typing import Dict
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    password: str
    role: str


database_items = Dict[int, Item]
database_items = {  1:Item(**{"id":1,
                                "name": "Paola",
                                "password": "1234",
                                "role": "user" }),
                        2:Item(**{"id":2,
                                "name": "Francisco",
                                "password": "250",
                                "role": "user"}),  
                            }
llave = 2

if llave in database_items.keys():
        item_in = database_items[llave]
else:
        print (None)
database_items[3]= Item(**{"id":3,
                                "name": "Alberto",
                                "password": "36",
                                "role": "user"})                            
print(database_items)
#print(database_items)
#for clave in database_items.keys(): 
   # print(clave)