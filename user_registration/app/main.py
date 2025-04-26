from fastapi import FastAPI
from app.routers import user  # Import your user router from app/routers

# Create FastAPI instance
app = FastAPI()

# Include the user router
app.include_router(user.router)
