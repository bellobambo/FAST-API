from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app= FastAPI()


fakeDB =[{
    "id" :1 ,
    "name" : 'BEE6!X',
    "price" : '$50k'
    },
    {
    "id" :2 ,
    "name" : 'SIRJSON',
    "price" : '$45k'
    },
    {
    "id" :3 ,
    "name" : 'SIRVIC',
    "price" : '$45'
    },

]

class Course(BaseModel):
    id : int
    name : str
    price : float
    is_early_bird : Optional[bool] = None
     

@app.get('/')
def read_root():
 return {
        "Greetings": "Welcome to SWEP200",
        "Note": "Simple CRUD API using FASTAPI",
        "GitHub": "https://github.com/bellobambo/FAST-API",
        "routes" : "https://fast-api-ocrl.onrender.com/docs"
    }

@app.get('/courses')
def get_courses():
    return fakeDB


@app.get('/courses/{courses_id}')
def get_a_courses(course_id : int):
    course = course_id - 1
    return fakeDB[course]


@app.post('/courses')
def add_courses(course : Course):
    fakeDB.append(course.dict())
    return fakeDB[-1]


@app.delete('/courses/{course_id}')
def delete_a_courses(course_id : int):
    fakeDB.pop(course_id - 1)
    return {"task" :"Item Deleted"}




