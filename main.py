from fastapi import FastAPI
from app.model import PostSchema

posts = [
     {
          "id" : 1,
          "title" : "penguins",
          "content" : "pengiuns are a group of aquatic birds."
     }
]

app = FastAPI()


@app.get("/", tags=["entry point"])
async def entry():
     return {"Message":"Home"}