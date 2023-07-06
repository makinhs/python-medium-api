from fastapi import APIRouter
from users.users_service import getAllUsers, createUser, deleteUser, updateUser, getUser
router = APIRouter()


@router.get("/users")
async def get_all_users():
    # Retrieve all users logic
    return getAllUsers()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    # Retrieve user by ID logic
    return getUser(user_id)

@router.post("/users")
async def create_user(user_data: dict):
    # Create user logic
    return createUser(user_data)

@router.put("/users/{user_id}")
async def update_user(user_id: int, user_data: dict):
    # Update user by ID logic
    return updateUser(user_id, user_data)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Delete user by ID logic
    return deleteUser(user_id)