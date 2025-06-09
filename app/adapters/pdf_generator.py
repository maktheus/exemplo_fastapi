"""Simple PDF generator placeholder."""

from io import BytesIO


class PDFGenerator:
    def generate(self, html: str) -> bytes:
        # Placeholder implementation; real implementation would render HTML to PDF
        return BytesIO(b"PDF content").getvalue()
