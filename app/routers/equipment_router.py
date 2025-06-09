from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.equipment_service import EquipmentService
from app.adapters.repository_sql import SQLEquipmentRepository

router = APIRouter()


def get_service(db: Session = Depends(get_db)) -> EquipmentService:
    repo = SQLEquipmentRepository(db)
    return EquipmentService(repo)


@router.get("/types")
def list_types(service: EquipmentService = Depends(get_service)):
    return service.list_types()


@router.get("/parts")
def list_parts(equipment_type_id: int | None = None, service: EquipmentService = Depends(get_service)):
    return service.list_parts(equipment_type_id)
