from fastapi import FastAPI

from routers import user_get
from routers import user_post


app = FastAPI()
app.include_router(user_get.router)
app.include_router(user_post.router)

@app.get("/")
async def home():
    return {"data": "Hello Task Manager Web"}
