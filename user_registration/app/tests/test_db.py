import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

# Now you can import config and database
from config import database

import asyncio

# Define an asynchronous function to test the connection
async def test_database_connection():
    try:
        # Connect to the database
        await database.connect()
        print("Database connection successful!")

        # Disconnect after testing
        await database.disconnect()
    except Exception as e:
        print(f"Error: {e}")

# Run the test
if __name__ == "__main__":
    asyncio.run(test_database_connection())
