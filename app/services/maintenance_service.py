from typing import Iterable

from app.domain.interfaces import MaintenanceRepository
from app.domain.entities import MaintenancePlan


class MaintenanceService:
    def __init__(self, repository: MaintenanceRepository):
        self.repository = repository

    def list_plans(self) -> Iterable[MaintenancePlan]:
        return self.repository.list_plans()

    def create_plan(self, plan: MaintenancePlan) -> MaintenancePlan:
        return self.repository.create_plan(plan)
