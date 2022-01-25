from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import List
import time

class Project(BaseModel):
    id: str
    name: str
    create_user: str
    create_timestamp: int
    images: List[str]

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/project/list/")
async def get_list():
    pass

@app.post("/project/create/")
async def create(_name: str = Form(...), _images: List[str] = Form(...)):
    project = Project(
        id = "1",
        name = _name,
        create_user = "User1",
        create_timestamp = int(time.time()),
        images = _images.copy()
    )
    return project
