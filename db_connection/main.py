from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
import uuid

app = FastAPI()

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["fastapi-tutorial"]
collection = db["users"]

# Pydantic model for input validation
class User(BaseModel):
    name: str
    email: str

@app.get("/")
def root():
    return {"message": "MongoDB connected 🚀"}

@app.post("/user/new")
def create_user(user: User):
    user_doc = {
        "_id": ObjectId(),
        "name": user.name,
        "email": user.email
    }
    result = collection.insert_one(user_doc)
    return {"message": "User added successfully", "user_id": str(user_doc["_id"])}