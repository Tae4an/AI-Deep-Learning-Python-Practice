from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()

todo_data = {
    1:{ "id":1,  "contents":"아침먹기", "is_done":True},
    2:{ "id":2, "contents": "점심먹기", "is_done": False},
    3:{ "id":3, "contents":"저녁먹기",  "is_done":False}
}

@app.get("/")       #HTTP GET 요청에 대한 루트 경로("/")를 정의
def root():         #루트 경로에 대한 요청을 처리하는 함수
    return {"hello":"테스트"}   #클라이언트에게 반환할 JSON 형식의 응답

@app.get("/todos")   #HTTP GET 요청에 대한 루트 경로("/todos")를 정의
def get_todos(order:str | None = None):
    ret = list(todo_data.values())
    if order and order == "DESC":
        return ret[::-1]
    return ret

@app.get('/todos/{todo_id}')
def get_todo_id(todo_id:int):
    ret = todo_data.get(todo_id, {})
    return ret


class Create_TodoList(BaseModel):
    id:int
    contents:str
    is_done:bool


@app.post('/todos')
def create_todo(request:Create_TodoList):
    todo_data[request.id] = request
    return todo_data[request.id]

@app.patch('/todos//{todo_id}')
def update_todo(todo_id:int, is_done:bool= Body(..., embed=True)):
    entry = todo_data.get(todo_id)
    if entry:
        entry['is_done'] = is_done
    return entry    

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id:int):
    todo_data.pop(todo_id,None)

    if todo_data:
        return todo_data