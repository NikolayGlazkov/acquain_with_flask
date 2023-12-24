"""Задание №1
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.

Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа."""
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Task(BaseModel):
    id:int
    title:str
    description: str
    status: bool

#список для получения списка задачь
tasks = []

#гет запрос
@app.get('/tasks/',response_model=List[Task])
async def get_tasks():

    return tasks

@app.post('/task/{id}',response_model=Task)
async def add_task(task:Task):
    task.id = len(Task)
    tasks.append(task)

    return task

@app.put('/tasks/{task_id}',response_model=Task)
async def update_task(task_id:int,task:Task):
    for indx in range(len(tasks)):
        if tasks[indx].id == task_id:
            tasks[indx] = task
            return task
        return HTTPException(status_code=404,detail="Task not found")
    

@app.delete('/tasks/{task_id}')
async def delete_task(task_id:int,task:Task):
    for task in tasks:
        if task.id == task_id:
            del task
            return {'message':"Task whos delited"}
        raise HTTPException(status_code=404,detail="Task not found")
