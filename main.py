# we import similarly as Typescript
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

from fastapi import FastAPI
from users.users_controller import router as users_router

app = FastAPI()
app.include_router(users_router)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}