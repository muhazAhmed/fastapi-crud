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

@app.put("/user/{id}")
def update_user(id: int, data: User):
    if data.id != id:
        raise HTTPException(status_code=400, detail="ID mismatch")
    if id is None:
        raise HTTPException(status_code=400, detail="ID is required")
    for index, user in enumerate(users):
        if user["id"] == id:
            users[index] = data.model_dump()
            return {"message": "User updated successfully", "user": data, "allUsers": users}
    raise HTTPException(status_code=404, detail="User not found")
