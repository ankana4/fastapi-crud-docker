from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    
class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    
class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime