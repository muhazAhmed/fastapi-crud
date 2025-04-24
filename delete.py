from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = [
    {"id": 1, "name": "Muhaz"},
    {"id": 2, "name": "Sahima"},    
]

class User(BaseModel):
    id: int
    name: str

@app.delete("/user/{id}")
def delete_user(id: int):
    for index, user in enumerate(users):
        if user["id"] == id:
            del users[index]
            return {"message": "User deleted successfully", "data": users}
    raise HTTPException(status_code=404, detail="User not found")