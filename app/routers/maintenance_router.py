from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.maintenance_service import MaintenanceService
from app.adapters.repository_sql import SQLMaintenanceRepository
from app.domain.entities import MaintenancePlan

router = APIRouter()


def get_service(db: Session = Depends(get_db)) -> MaintenanceService:
    repo = SQLMaintenanceRepository(db)
    return MaintenanceService(repo)


@router.get("/plans")
def list_plans(service: MaintenanceService = Depends(get_service)):
    return service.list_plans()


@router.post("/plans")
def create_plan(plan: MaintenancePlan, service: MaintenanceService = Depends(get_service)):
    return service.create_plan(plan)
