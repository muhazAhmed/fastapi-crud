from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory user list
users = [
    {"id": 1, "name": "Muhaz"},
    {"id": 2, "name": "Sahima"},
]

# Define request body structure
class User(BaseModel):
    id: int
    name: str

# POST /users
@app.post("/users")
def create_user(user: User):
    users.append(user.model_dump())
    return {"message": "User added successfully", "user": user}
