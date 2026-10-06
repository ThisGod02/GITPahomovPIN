#!/usr/bin/env python3
"""Todo API - основное приложение."""
from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI(title="Todo API", description="REST API для управления задачами", version="1.0.0")
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category: str = "general"
class TodoResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    category: str
    status: str
    created_at: datetime
    updated_at: datetime
todos: dict = {}
@app.get("/")
async def root():
    return {"message": "Todo API v1.0.0", "docs": "/docs"}
@app.get("/health")
async def health():
    return {"status": "healthy"}
@app.get("/todos", response_model=List[TodoResponse])
async def get_todos():
    return list(todos.values())
@app.post("/todos", response_model=TodoResponse, status_code=201)
async def create_todo(todo: TodoCreate):
    todo_id = str(uuid4())
    new_todo = {"id": todo_id, **todo.model_dump(), "status": "active", "created_at": datetime.now(), "updated_at": datetime.now()}
    todos[todo_id] = new_todo
    return new_todo
@app.get("/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]
@app.delete("/todos/{todo_id}", status_code=204)
async def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return None
