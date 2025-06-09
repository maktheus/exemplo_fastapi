from fastapi import FastAPI

from app.routers import (
    equipment_router,
    procedure_router,
    maintenance_router,
    report_router,
)

app = FastAPI(title="Preventive Maintenance API")

app.include_router(equipment_router.router, prefix="/equipment", tags=["Equipment"])
app.include_router(procedure_router.router, prefix="/procedures", tags=["Procedure"])
app.include_router(maintenance_router.router, prefix="/maintenance", tags=["Maintenance"])
app.include_router(report_router.router, prefix="/reports", tags=["Report"])


def get_app() -> FastAPI:
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
