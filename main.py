from bson import ObjectId
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from pymongo import MongoClient

app = FastAPI()
client = MongoClient(
    'mongodb+srv://infinato:XpFQwqAX8raTnCz2@librarymgmt.rsex8dg.mongodb.net/?retryWrites=true&w=majority&appName=libraryMgmt')
db = client['student_db']
collection = db['students']

"""

MongoDB Database Connection
Username: infinato
Password: XpFQwqAX8raTnCz2

Connection Url: mongodb+srv://infinato:XpFQwqAX8raTnCz2@librarymgmt.rsex8dg.mongodb.net/?retryWrites=true&w=majority&appName=libraryMgmt

"""


# Pydantic models
class Address(BaseModel):
    city: str
    country: str


class Student(BaseModel):
    name: str
    age: int
    address: Address


class StudentInDB(Student):
    id: str


# Routes
@app.post("/students", response_model=StudentInDB, status_code=201)
async def create_student(student: Student):
    inserted_student = collection.insert_one(student.dict())
    return {"id": str(inserted_student.inserted_id), **student.dict()}


@app.get("/students", response_model=list[StudentInDB])
async def get_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = age

    students = []
    for student in collection.find(query):
        students.append({**student, "id": str(student["_id"])})

    return students


@app.get("/students/{id}", response_model=StudentInDB)
async def get_student(id: str):
    student = collection.find_one({"_id": ObjectId(id)})
    if student:
        return {**student, "id": str(student["_id"])}
    else:
        raise HTTPException(status_code=404, detail="Student not found")


@app.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: Student):
    student_dict = student.dict(exclude_unset=True)
    if student_dict:
        collection.update_one({"_id": ObjectId(id)}, {"$set": student_dict})
    else:
        raise HTTPException(status_code=400, detail="No fields provided for update")


@app.delete("/students/{id}", status_code=200)
async def delete_student(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
