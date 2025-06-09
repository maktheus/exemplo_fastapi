from pydantic import BaseModel
from typing import Optional


class ReportRequest(BaseModel):
    equipment_type_id: Optional[int] = None
    part_id: Optional[int] = None


class ReportResponse(BaseModel):
    filename: str
    content_type: str = "application/pdf"
    data: bytes

