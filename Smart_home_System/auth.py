from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

# Mock database
users_db = {
    "admin": {"username": "admin", "password": "admin123", "role": "Admin"},
    "user": {"username": "user", "password": "user123", "role": "User"}
}

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Authenticate user with username and password.
    """
    user = users_db.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def authorize_role(required_role: str):
    """
    Check if the user has the required role.
    """
    def role_dependency(user=Depends(authenticate_user)):
        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Not authorized")
        return user
    return role_dependency
