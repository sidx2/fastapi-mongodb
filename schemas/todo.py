def todoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": str(item["title"]),
        "desc": str(item["desc"]),
    }

def todosEntity(items):
    return [todoEntity(item) for item in items]