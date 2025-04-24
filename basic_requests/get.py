from fastapi import FastAPI

app = FastAPI()

# Get api's
@app.get("/")
def read_root():
    return {"message": "API is working"}

users = [
    {"id": 1, "name": "Muhaz"},
    {"id": 2, "name": "Sahima"},
]

@app.get("/users")
def get_users():
    return {"message": str(len(users)) + " users found", "data" : users}

@app.get("/user/{id}")
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    return {"message": "User not found"}