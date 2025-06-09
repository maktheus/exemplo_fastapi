from fastapi import APIRouter, Depends

from app.services.report_service import ReportService
from app.adapters.pdf_generator import PDFGenerator
from app.schemas.report import ReportRequest

router = APIRouter()


def get_service() -> ReportService:
    generator = PDFGenerator()
    return ReportService(generator)


@router.get("/procedures")
def generate_report(request: ReportRequest = Depends(), service: ReportService = Depends(get_service)):
    return service.generate_procedure_report(request)
