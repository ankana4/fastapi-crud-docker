from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    return await UserRepository.create_user(user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    doc = await UserRepository.get_user(user_id)
    if not doc:
        raise HTTPException(404, "User not found")
    return doc

@router.get("/", response_model=list[UserResponse])
async def get_all_users():
    return await UserRepository.get_all_users()

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, data: UserUpdate):
    updated = await UserRepository.update_user(user_id, data)
    if not updated:
        raise HTTPException(404, "user not found or failed to update")
    return updated

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    deleted = await UserRepository.delete_user(user_id)
    if not deleted:
        raise HTTPException(404, "user not found")
    return {"status": "deleted"}