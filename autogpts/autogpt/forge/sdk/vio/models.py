from pydantic import BaseModel
from typing import List, Optional, Any, Union

# Pagination Model
class Pagination(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    page_size: int

# TaskInput Model
class TaskInput(BaseModel):
    debug: bool
    mode: str

# Artifact Model
class Artifact(BaseModel):
    artifact_id: str
    agent_created: bool
    file_name: str
    relative_path: Optional[str]

# TaskRequestBody Model
class TaskRequestBody(BaseModel):
    input: Optional[str]
    additional_input: TaskInput

# Task Model
class Task(TaskRequestBody):
    task_id: str
    artifacts: List[Artifact]

# TaskListResponse Model
class TaskListResponse(BaseModel):
    tasks: List[Task]
    pagination: Pagination

# ArtifactUpload Model
class ArtifactUpload(BaseModel):
    file: bytes
    relative_path: str

# StepInput Model
class StepInput(BaseModel):
    file_to_refactor: str

# StepOutput Model
class StepOutput(BaseModel):
    tokens: int
    estimated_cost: str

# StepRequestBody Model
class StepRequestBody(BaseModel):
    input: Optional[str]
    additional_input: StepInput

# Step Model
class Step(StepRequestBody):
    step_id: str
    task_id: str
    status: str
    is_last: bool
    artifacts: List[Artifact]
