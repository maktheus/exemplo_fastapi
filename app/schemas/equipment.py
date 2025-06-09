from pydantic import BaseModel


class EquipmentType(BaseModel):
    id: int
    name: str


class Part(BaseModel):
    id: int
    name: str
    equipment_type_id: int
