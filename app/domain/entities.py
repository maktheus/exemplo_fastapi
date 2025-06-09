from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class EquipmentType:
    id: int
    name: str


@dataclass
class Part:
    id: int
    name: str
    equipment_type_id: int


@dataclass
class Procedure:
    id: int
    description: str
    equipment_type_id: int
    part_id: Optional[int] = None


@dataclass
class MaintenancePlan:
    id: int
    name: str
    procedures: List[Procedure]
    created_at: datetime
