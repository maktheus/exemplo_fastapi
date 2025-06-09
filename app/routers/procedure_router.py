from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.procedure_service import ProcedureService
from app.adapters.repository_sql import SQLProcedureRepository
from app.domain.entities import Procedure

router = APIRouter()


def get_service(db: Session = Depends(get_db)) -> ProcedureService:
    repo = SQLProcedureRepository(db)
    return ProcedureService(repo)


@router.get("/")
def list_procedures(service: ProcedureService = Depends(get_service)):
    return service.list()


@router.post("/")
def create_procedure(procedure: Procedure, service: ProcedureService = Depends(get_service)):
    return service.create(procedure)


@router.get("/{procedure_id}")
def get_procedure(procedure_id: int, service: ProcedureService = Depends(get_service)):
    return service.get(procedure_id)


@router.put("/{procedure_id}")
def update_procedure(procedure_id: int, procedure: Procedure, service: ProcedureService = Depends(get_service)):
    return service.update(procedure_id, procedure)


@router.delete("/{procedure_id}")
def delete_procedure(procedure_id: int, service: ProcedureService = Depends(get_service)):
    service.delete(procedure_id)
    return {"ok": True}
