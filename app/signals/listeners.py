from app.utils.email_utils import send_email
from app.signals.event_signals import (
    user_created,
    user_updated,
    user_deleted
)

async def send_welcome_email(user):
    await send_email(
        to_email=user["email"],
        subject="Welcome to fastAPI!",
        body=f"Hi {user['username']}, welcome to our platform!    "
    )
    print(f"[SIGNAL] Sending welcome email to {user['email']}")
    
async def log_update(user, user_id, changes):
    old_username = user["username"]
    
    await send_email(
        to_email=user["email"],
        subject="Update your data",
        body=f"Hi {old_username}, Your user data has been updated."
    )
    print(f"[SIGNAL] {user} updated with {changes}")
    
async def log_delete(username, user_id):
    print(f"[Signal] User {username['username']} deleted.")    
        
    
    
user_created.connect(send_welcome_email)  
user_updated.connect(log_update)
user_deleted.connect(log_delete)      

