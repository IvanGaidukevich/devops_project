from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskPatch(BaseModel):
    completed: bool


class TaskResponse(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
