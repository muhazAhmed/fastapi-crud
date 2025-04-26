from dotenv import load_dotenv
import os
from databases import Database

# Load environment variables
load_dotenv()

# Get environment variables
DB_URL = os.getenv("DB_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

# Database connection
database = Database(DB_URL)