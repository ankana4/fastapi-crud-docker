from fastapi import FastAPI
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.routes.user_routes import router as user_router

app = FastAPI(title='FastAPI Mongo CRUD')

app.include_router(user_router)

@app.on_event("startup")
async def startup():
    import app.signals.listeners
    await connect_to_mongo()
    
@app.on_event("shutdown")
async def shitdown():
    await close_mongo_connection()