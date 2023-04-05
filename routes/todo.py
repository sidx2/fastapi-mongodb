from bson import ObjectId
from fastapi import APIRouter
from models.todo import Todo
from config.db import conn
from schemas.todo import todoEntity, todosEntity
from bson.json_util import dumps

todo_router = APIRouter()

# get all tood
@todo_router.get("/api/todo/")
async def fn():
    return {"res": todosEntity(conn.test.todos.find())}

# get one todo by id
@todo_router.get("/api/todo/{id}")
async def fn(id):
    return todoEntity(conn.test.todos.find_one({"_id": ObjectId(id)}))

# create  a new todo
@todo_router.post("/api/todo/")
async def fn(todo: Todo):
    newTodo = conn.test.todos.insert_one(dict(todo))
    # print("newTodo: ", jsonify(newTodo))
    # print("newTodo todoEntity: ", todoEntity(newTodo))
    todos = todosEntity(conn.test.todos.find())
    return {"res": todos}

# update a todo
@todo_router.put("/api/todo/{id}")
async def fn(id, todo: Todo):
    return {"res": todoEntity(conn.test.todos.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)}))}

# delete a todo
@todo_router.delete("/api/todo/{id}")
async def fn(id):
    deleted_todo = conn.test.todos.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "Todo deleted successfully", "todo": todoEntity(deleted_todo)}