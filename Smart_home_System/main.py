from fastapi import FastAPI
from backend.routes import users,houses, houseuser, appliances, protected_routes
from backend.routes.houseuser import router as houseuser_router
from fastapi.routing import APIRouter
from auth import authenticate_user, authorize_role
from fastapi import FastAPI, Depends

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(houses.router, prefix="/houses", tags=["Houses"])
app.include_router(houseuser.router, prefix="/houseuser", tags=["HouseUser"])
app.include_router(appliances.router, prefix="/appliances", tags=["Appliance"])
app.include_router(protected_routes.router, prefix="/protected", tags=["Protected Routes"])

@app.get("/protected-route")
def protected_route(user=Depends(authenticate_user)):
    return {"message": f"You are authenticated as {user['username']}!"}

@app.get("/admin-route")
def admin_route(user=Depends(authorize_role("Admin"))):
    return {"message": "Hello Admin!"}

@app.get("/user-route")
def user_route(user=Depends(authenticate_user)):
    return {"message": f"Hello, {user['username']}!"}

@app.on_event("startup")
async def list_routes():
    for route in app.router.routes:
        if isinstance(route, APIRouter):
            print(f"Path: {route.path} | Name: {route.name}")

@app.get("/")
def read_root():
    return {"message": "Hello, Smart Home System!"}
