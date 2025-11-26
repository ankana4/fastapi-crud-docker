#MongoDB document schema not Pydantic

from typing import Optional
from datetime import datetime

def user_doc(username: str, email: str) -> dict:
    return {
        "username" : username,
        "email": email,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        
}