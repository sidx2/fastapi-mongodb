from fastapi import FastAPI
from routes.todo import todo_router
app = FastAPI()

@app.get("/")
def fn():
    return {"res": "success"}

app.include_router(todo_router)

