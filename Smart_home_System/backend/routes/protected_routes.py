from fastapi import APIRouter, Depends
from auth import authenticate_user

router = APIRouter()

@router.get("/protected-route")
def protected_route(user=Depends(authenticate_user)):
    return {"message": "You are authenticated!"}
