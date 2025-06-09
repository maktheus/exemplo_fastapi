from pydantic import BaseModel
from typing import Optional


class ProcedureBase(BaseModel):
    description: str
    equipment_type_id: int
    part_id: Optional[int] = None


class ProcedureCreate(ProcedureBase):
    pass


class ProcedureUpdate(ProcedureBase):
    pass


class Procedure(ProcedureBase):
    id: int

    class Config:
        orm_mode = True
