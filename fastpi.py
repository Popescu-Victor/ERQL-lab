from fastapi import FastAPI
from routers import items

app = FastAPI()
app.include_router(items.router)


@app.get("/users/{user_id}")

# GET http://localhost:8000/users/42
