"""SQLAlchemy implementations of domain repository interfaces."""

from sqlalchemy.orm import Session

from app.domain.entities import EquipmentType, Part, Procedure, MaintenancePlan
from app.domain.interfaces import (
    EquipmentRepository,
    ProcedureRepository,
    MaintenanceRepository,
)


class SQLEquipmentRepository(EquipmentRepository):
    def __init__(self, db: Session):
        self.db = db

    def list_types(self):
        # placeholder implementation
        return []

    def list_parts(self, equipment_type_id: int | None = None):
        return []


class SQLProcedureRepository(ProcedureRepository):
    def __init__(self, db: Session):
        self.db = db

    def list(self):
        return []

    def get(self, procedure_id: int):
        return None

    def create(self, procedure: Procedure):
        return procedure

    def update(self, procedure_id: int, procedure: Procedure):
        return procedure

    def delete(self, procedure_id: int) -> None:
        pass


class SQLMaintenanceRepository(MaintenanceRepository):
    def __init__(self, db: Session):
        self.db = db

    def list_plans(self):
        return []

    def create_plan(self, plan: MaintenancePlan):
        return plan
