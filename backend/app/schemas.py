from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskPatch(BaseModel):
    completed: bool


class TaskResponse(TaskBase):
    id: int


    class Config:
        from_attributes = True

