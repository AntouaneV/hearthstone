from fastapi import FastAPI
import os
from typing import Union
from pydantic import BaseModel




class User(BaseModel):
    username: str
    password: str
    
app = FastAPI()


@app.post("/users/")
async def create_item(user: User):
    return user
   

@app.get("/")
async def root():
    return {"message": "Hello World"}

# login 
@app.get("/users/{id}/{password}")
async def login(id,password):
    return {
        "id": id,
        "password": password,
}

  
    

# @app.get("/users/{id}")
# async def login(id):
#     return {"id": id, "mot de pass": 'password'}
    


if __name__=="__main__":
    os.system("uvicorn main:app --reload")