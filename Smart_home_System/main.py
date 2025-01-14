from fastapi import FastAPI
from backend.routes import users,houses, houseuser, appliances
from backend.routes.houseuser import router as houseuser_router
from fastapi.routing import APIRouter

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(houses.router, prefix="/houses", tags=["Houses"])
app.include_router(houseuser.router, prefix="/houseuser", tags=["HouseUser"])
app.include_router(appliances.router, prefix="/appliances", tags=["Appliance"])


@app.on_event("startup")
async def list_routes():
    for route in app.router.routes:
        if isinstance(route, APIRouter):
            print(f"Path: {route.path} | Name: {route.name}")

@app.get("/")
def read_root():
    return {"message": "Hello, Smart Home System!"}
