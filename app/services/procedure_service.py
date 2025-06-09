from typing import Iterable

from app.domain.interfaces import ProcedureRepository
from app.domain.entities import Procedure


class ProcedureService:
    def __init__(self, repository: ProcedureRepository):
        self.repository = repository

    def list(self) -> Iterable[Procedure]:
        return self.repository.list()

    def get(self, procedure_id: int) -> Procedure | None:
        return self.repository.get(procedure_id)

    def create(self, procedure: Procedure) -> Procedure:
        return self.repository.create(procedure)

    def update(self, procedure_id: int, procedure: Procedure) -> Procedure:
        return self.repository.update(procedure_id, procedure)

    def delete(self, procedure_id: int) -> None:
        self.repository.delete(procedure_id)
