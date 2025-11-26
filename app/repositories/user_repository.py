from bson import ObjectId
from app.db.mongodb import mongodb
from app.models.user_model import user_doc
from datetime import datetime

class UserRepository:
    
    @staticmethod
    async def create_user(data):
        doc = user_doc(data.username, data.email)
        result = await mongodb.db.users.insert_one(doc)
        doc["id"] = str(result.inserted_id)
        return doc
    
    @staticmethod
    async def get_user(user_id: str):
        doc = await mongodb.db.users.find_one({"_id": ObjectId(user_id)})
        if not doc:
            return None
        doc["id"] = str(doc["_id"])
        return doc
    
    @staticmethod
    async def get_all_users():
        users = []
        async for doc in mongodb.db.users.find():
            doc["id"] = str(doc["_id"])
            users.append(doc)
        return users 
    
    @staticmethod
    async def update_user(user_id: str, data):
        update_data = {k: v for k, v in data.dict().items() if v is not None}
        update_data["updated_at"] = datetime.utcnow()
        
        result = await mongodb.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            return None
        return await UserRepository.get_user(user_id)
    
    @staticmethod
    async def delete_user(user_id: str):
        result = await mongodb.db.users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0 