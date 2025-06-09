from abc import ABC, abstractmethod
from typing import Iterable, Protocol

from .entities import EquipmentType, Part, Procedure, MaintenancePlan


class EquipmentRepository(Protocol):
    @abstractmethod
    def list_types(self) -> Iterable[EquipmentType]:
        ...

    @abstractmethod
    def list_parts(self, equipment_type_id: int | None = None) -> Iterable[Part]:
        ...


class ProcedureRepository(Protocol):
    @abstractmethod
    def list(self) -> Iterable[Procedure]:
        ...

    @abstractmethod
    def get(self, procedure_id: int) -> Procedure | None:
        ...

    @abstractmethod
    def create(self, procedure: Procedure) -> Procedure:
        ...

    @abstractmethod
    def update(self, procedure_id: int, procedure: Procedure) -> Procedure:
        ...

    @abstractmethod
    def delete(self, procedure_id: int) -> None:
        ...


class MaintenanceRepository(Protocol):
    @abstractmethod
    def list_plans(self) -> Iterable[MaintenancePlan]:
        ...

    @abstractmethod
    def create_plan(self, plan: MaintenancePlan) -> MaintenancePlan:
        ...
