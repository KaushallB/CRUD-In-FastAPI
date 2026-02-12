from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

data={
    1:{
        'name':'Kaushal',
        'age':16  ,
        'level': '8th Sem'
    }
}

class Users(BaseModel):
            name: str
            age: int
            level:str

class UpdateUser(BaseModel):
      name: Optional[str] = None
      age: Optional[int] = None
      level: Optional[str] = None

@app.get('/')
def index():
    return {'name':"First Data"}

@app.get('/get-all-details')
def all_details():
      return data

@app.get('/get-details/{id}')
def get_details(id: int = Path(..., description='ID of user u wanna know about')):
    return data[id]

@app.get('/get-by-name')
# def get_details(name: str = None):
def get_details(name: Optional[str] = None):
        for  id in data:
             if data[id]['name'] == name:
                   return data[id]
        return {'Data':"Not found"}

@app.get('/double-para/{id}')
def get_details(*, id  : int, name: Optional[str] = None):
        for  id in data:
             if data[id]['name'] == name:
                   return data[id]
        return {'Data':"Not found"}

@app.post('/create-user/{id}')
def create_user(id: int , user: Users):
      if id in data:
            return {'Error': 'User already exists'}
      
      data[id] = user
      return data[id]

@app.put('/update-user/{id}')
def update(id: int, user: UpdateUser):
      
      if id not in data:
            return {'Error': 'Us er not exist'}
      
      if user.name != None:
            data[id].name = user.name

      if user.age != None:
            data[id].age = user.age
        
      if user.level != None:
            data[id].level = user.level

      return data[id]   

@app.delete('/delete-user/{id}')
def delete_student(id: int):
      if id not in data:
            return {"Error" : "Student doenst exist"}

      del data[id]
      return {"Message": "Student deleted successfully"}




