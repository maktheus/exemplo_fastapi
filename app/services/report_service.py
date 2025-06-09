from app.adapters.pdf_generator import PDFGenerator
from app.schemas.report import ReportRequest, ReportResponse


class ReportService:
    def __init__(self, pdf_generator: PDFGenerator):
        self.pdf_generator = pdf_generator

    def generate_procedure_report(self, request: ReportRequest) -> ReportResponse:
        html = "<html><body><h1>Report</h1></body></html>"
        pdf_bytes = self.pdf_generator.generate(html)
        return ReportResponse(filename="report.pdf", data=pdf_bytes)
