import asyncio
import json
import uuid
from fastapi import FastAPI, Request, UploadFile, File
from typing import List, Optional, Dict, Any
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sse_starlette import EventSourceResponse
from starlette.responses import FileResponse

from vio.mock_db import mock_db

app = FastAPI()

# Handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Schemas
class Pagination(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    page_size: int


class Artifact(BaseModel):
    artifact_id: str
    agent_created: bool
    file_name: str
    relative_path: Optional[str]


class TaskInput(BaseModel):
    debug: bool
    mode: str


class TaskRequestBody(BaseModel):
    input: Optional[str]
    additional_input: TaskInput


class Task(TaskRequestBody):
    task_id: str
    artifacts: List[Artifact]


class TaskListResponse(BaseModel):
    tasks: List[Task]
    pagination: Pagination


# In-Memory Database Simulation
tasks_db = {}


# Route for SSE to send task updates to clients
@app.get("/sse")
async def sse_endpoint(request: Request):
    async def event_generator():
        while True:
            # Create an event to send to the client
            event_data = json.dumps(tasks_db)
            yield event_data

            # Sleep for a while before sending the next event
            await asyncio.sleep(0.1)

    return EventSourceResponse(event_generator(), media_type="text/event-stream")


# Print the generated mock data
print(mock_db)


# Request and response models
class TaskRequestBody(BaseModel):
    input: str
    additional_input: dict


class StepRequestBody(BaseModel):
    action: str
    parameters: Dict[str, Any]


# POST: Create a new task and store it in the mock database
@app.post("/ap/v1/agent/tasks", tags=["agent"])
def create_agent_task(task: TaskRequestBody):
    new_task_id = str(len(mock_db["General Challenge"]["tasks"]) + 1)
    new_task = {
        "task_id": new_task_id,
        "input": task.input,
        "additional_input": task.additional_input,
        "artifacts": [],
        "steps": [],
    }
    mock_db["General Challenge"]["tasks"].append(new_task)
    return {"task_id": new_task_id}


# GET: List paginated tasks from the mock database
@app.get("/ap/v1/agent/tasks", tags=["agent"])
def list_agent_tasks(current_page: int = 1, page_size: int = 10):
    start_idx = (current_page - 1) * page_size
    end_idx = start_idx + page_size
    tasks = mock_db["General Challenge"]["tasks"][start_idx:end_idx]
    return {"tasks": tasks}


# GET: Retrieve a task by its ID from the mock database
@app.get("/ap/v1/agent/tasks/{task_id}", tags=["agent"])
def get_agent_task(task_id: str):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    return {"task": task or {}}


# GET: List all steps for a task from the mock database
@app.get("/ap/v1/agent/tasks/{task_id}/steps", tags=["agent"])
def list_agent_task_steps(task_id: str, current_page: int = 1, page_size: int = 10):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    if task:
        start_idx = (current_page - 1) * page_size
        end_idx = start_idx + page_size
        steps = task["steps"][start_idx:end_idx]
        return {"steps": steps}
    return {"steps": []}


# POST: Execute a step in a task and update it in the mock database
@app.post("/ap/v1/agent/tasks/{task_id}/steps", tags=["agent"])
def execute_agent_task_step(task_id: str, step: StepRequestBody):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    if task:
        new_step_id = str(len(task["steps"]) + 1)
        new_step = {
            "step_id": new_step_id,
            "action": step.action,
            "parameters": step.parameters,
        }
        task["steps"].append(new_step)
        return {"step_id": new_step_id}
    return {"step_id": None}


# GET: Retrieve a specific step by its ID from the mock database
@app.get("/ap/v1/agent/tasks/{task_id}/steps/{step_id}", tags=["agent"])
def get_agent_task_step(task_id: str, step_id: str):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    if task:
        step = next((s for s in task["steps"] if s["step_id"] == step_id), None)
        return {"step": step or {}}
    return {"step": {}}


# GET: List all artifacts for a task from the mock database
@app.get("/ap/v1/agent/tasks/{task_id}/artifacts", tags=["agent"])
def list_agent_task_artifacts(task_id: str, current_page: int = 1, page_size: int = 10):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    if task:
        start_idx = (current_page - 1) * page_size
        end_idx = start_idx + page_size
        artifacts = task["artifacts"][start_idx:end_idx]
        return {"artifacts": artifacts}
    return {"artifacts": []}


# POST: Upload an artifact for a task and update it in the mock database
@app.post("/ap/v1/agent/tasks/{task_id}/artifacts", tags=["agent"])
async def upload_agent_task_artifacts(task_id: str, file: UploadFile = File(...)):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    if task:
        new_artifact_id = str(len(task["artifacts"]) + 1)
        new_artifact = {
            "artifact_id": new_artifact_id,
            "file_name": file.filename
            # you might want to actually store the file somewhere
        }
        task["artifacts"].append(new_artifact)
        return {"artifact_id": new_artifact_id}
    return {"artifact_id": None}


# GET: Download a specific artifact by its ID from the mock database
@app.get("/ap/v1/agent/tasks/{task_id}/artifacts/{artifact_id}", tags=["agent"])
def download_agent_task_artifact(task_id: str, artifact_id: str):
    task = next(
        (
            item
            for item in mock_db["General Challenge"]["tasks"]
            if item["task_id"] == task_id
        ),
        None,
    )
    if task:
        artifact = next(
            (a for a in task["artifacts"] if a["artifact_id"] == artifact_id), None
        )
        return {"artifact": artifact or {}}
    return {"artifact": {}}


@app.get("/qa/")
async def read_root(question: str):
    # In a real-world application, you would replace this with code that finds the answer using a QA model
    answer = f"The answer to your question '{question}' is 42."
    return {"question": question, "answer": answer}
