from datetime import datetime
from pydantic import BaseModel
from typing import List

from .procedure import Procedure


class MaintenancePlanBase(BaseModel):
    name: str


class MaintenancePlanCreate(MaintenancePlanBase):
    procedure_ids: List[int]


class MaintenancePlan(MaintenancePlanBase):
    id: int
    procedures: List[Procedure]
    created_at: datetime

    class Config:
        orm_mode = True
