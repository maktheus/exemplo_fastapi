from typing import Iterable

from app.domain.interfaces import EquipmentRepository
from app.domain.entities import EquipmentType, Part


class EquipmentService:
    def __init__(self, repository: EquipmentRepository):
        self.repository = repository

    def list_types(self) -> Iterable[EquipmentType]:
        return self.repository.list_types()

    def list_parts(self, equipment_type_id: int | None = None) -> Iterable[Part]:
        return self.repository.list_parts(equipment_type_id)
