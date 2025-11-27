"""
FastAPI Tasks service using the shared PostgreSQL helpers.

Run locally with:
    uvicorn PythonTuan3.fastapi_tasks:app --reload --host 0.0.0.0 --port 8000
"""

from typing import List, Optional, Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from db import get_db_connection
from TaskEntity import Tasks as TaskModels


TaskEntity = TaskModels.TaskEntity

app = FastAPI(
    title="Tasks API",
    version="1.0.0",
    description="FastAPI service providing CRUD operations for Tasks table.",
)


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    status: str = Field(default="pending", min_length=1, max_length=50)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[str] = Field(default=None, min_length=1, max_length=50)


class TaskResponse(TaskBase):
    id: int


class TaskListResponse(BaseModel):
    status: str
    data: List[TaskResponse]
    count: int


class TaskSingleResponse(BaseModel):
    status: str
    data: TaskResponse


class MessageResponse(BaseModel):
    status: str
    message: str


def _row_to_entity(row: Optional[Dict[str, Any]]) -> Optional[TaskEntity]:
    if row is None:
        return None
    return TaskEntity.from_row(row)


def _fetch_all(cur) -> List[Dict[str, Any]]:
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    return [dict(zip(columns, row)) for row in rows]


def _fetch_one(cur) -> Optional[Dict[str, Any]]:
    row = cur.fetchone()
    if row is None:
        return None
    columns = [desc[0] for desc in cur.description]
    return dict(zip(columns, row))


def get_all_tasks_entities() -> List[TaskEntity]:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Tasks")
            rows = _fetch_all(cur)
            return [_row_to_entity(row) for row in rows if row is not None]
    finally:
        if conn:
            conn.close()


def get_task_entity(task_id: int) -> Optional[TaskEntity]:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Tasks WHERE id = %s", (task_id,))
            row = _fetch_one(cur)
            return _row_to_entity(row)
    finally:
        if conn:
            conn.close()


def create_task_entity(task: TaskCreate) -> Optional[TaskEntity]:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO Tasks (title, description, status)
                VALUES (%s, %s, %s)
                RETURNING id, title, description, status
                """,
                (task.title, task.description, task.status),
            )
            row = _fetch_one(cur)
            conn.commit()
            return _row_to_entity(row)
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


def update_task_entity(task_id: int, task: TaskUpdate) -> Optional[TaskEntity]:
    updates = []
    values: List[Any] = []

    if task.title is not None:
        updates.append("title = %s")
        values.append(task.title)
    if task.description is not None:
        updates.append("description = %s")
        values.append(task.description)
    if task.status is not None:
        updates.append("status = %s")
        values.append(task.status)

    if not updates:
        return get_task_entity(task_id)

    values.append(task_id)
    query = f"""
        UPDATE Tasks
        SET {', '.join(updates)}
        WHERE id = %s
        RETURNING id, title, description, status
    """

    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute(query, values)
            row = _fetch_one(cur)
            conn.commit()
            return _row_to_entity(row)
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


def delete_task_entity(task_id: int) -> bool:
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM Tasks
                WHERE id = %s
                RETURNING id
                """,
                (task_id,),
            )
            deleted = cur.fetchone() is not None
            conn.commit()
            return deleted
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


def entity_to_task_response(entity: TaskEntity) -> TaskResponse:
    return TaskResponse(**entity.to_dict())


@app.post("/api/tasks", response_model=TaskSingleResponse, status_code=201)
def create_task(task: TaskCreate):
    try:
        created = create_task_entity(task)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to create task: {exc}") from exc

    if created is None:
        raise HTTPException(status_code=500, detail="Task creation returned no data")

    return {"status": "success", "data": entity_to_task_response(created)}


@app.get("/api/tasks", response_model=TaskListResponse)
def list_tasks():
    entities = get_all_tasks_entities()
    data = [entity_to_task_response(entity) for entity in entities]
    return {"status": "success", "data": data, "count": len(data)}


@app.get("/api/tasks/{task_id}", response_model=TaskSingleResponse)
def get_task(task_id: int):
    entity = get_task_entity(task_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "data": entity_to_task_response(entity)}


@app.put("/api/tasks/{task_id}", response_model=TaskSingleResponse)
def update_task(task_id: int, update: TaskUpdate):
    try:
        entity = update_task_entity(task_id, update)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to update task: {exc}") from exc

    if entity is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"status": "success", "data": entity_to_task_response(entity)}


@app.delete("/api/tasks/{task_id}", response_model=MessageResponse)
def delete_task(task_id: int):
    try:
        deleted = delete_task_entity(task_id)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to delete task: {exc}") from exc

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"status": "success", "message": "Task deleted successfully"}


@app.get("/health", response_model=MessageResponse, tags=["Health"])
def health_check():
    return {"status": "success", "message": "Service is up"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "PythonTuan3.fastapi_tasks:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

