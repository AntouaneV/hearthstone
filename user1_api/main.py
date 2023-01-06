from fastapi import FastAPI,Request
import os
from typing import Union
from pydantic import BaseModel
import users as u

    
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

#find all users
@app.get("/users")
async def users_info():
    json_reponse = []
    data = u.InsertUser()
    for user in data:
        response = {
            'user_id':user[0],
            'username':user[1],
            'Email':user[2],
            'Password':user[3],
            'Nb_games_played':user[4],
            'Nb_games_won':user[5],
            'Nb_unit_played':user[6],
            'Nb_hero_power':user[7],
            'Nb_spells_played':user[8],
            'Nb_gold':user[8],
            'Nb_arcone_dust':user[9],
            'Nb_xp':user[10]
        }
        json_reponse.append(response)
    return json_reponse

#find user by id  
@app.get("/users/{id}")
def find_user(id):
    json_reponse = []
    data = u.FindUser(id)
    for user in data:
        response = {
            'user_id':user[0],
            'username':user[1],
            'Email':user[2],
            'Password':user[3],
            'Nb_games_played':user[4],
            'Nb_games_won':user[5],
            'Nb_unit_played':user[6],
            'Nb_hero_power':user[7],
            'Nb_spells_played':user[8],
            'Nb_gold':user[8],
            'Nb_arcone_dust':user[9],
            'Nb_xp':user[10]
        }
    json_reponse.append(response)
    return json_reponse
   

#create user
@app.post("/users/create")
async def create_users(info : Request):      
        request_data = await info.json()
        usernamedata = request_data['username']
        passworddata = request_data['password']
        emaildata = request_data['email']
        u.create_user(usernamedata,passworddata,emaildata)
        return '''
           username: {}
           password: {}
           email: {}'''.format(usernamedata,passworddata,emaildata)    
        
        
if __name__=="__main__":
    os.system("uvicorn main:app --reload")