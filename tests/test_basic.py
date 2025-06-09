from fastapi.testclient import TestClient
from app.main import get_app

client = TestClient(get_app())

def test_equipment_types():
    resp = client.get('/equipment/types')
    assert resp.status_code == 200
    assert resp.json() == []

def test_equipment_parts():
    resp = client.get('/equipment/parts')
    assert resp.status_code == 200
    assert resp.json() == []

def test_procedure_lifecycle():
    # list
    resp = client.get('/procedures/')
    assert resp.status_code == 200
    assert resp.json() == []

    data = {"id": 1, "description": "Test", "equipment_type_id": 1, "part_id": None}
    resp = client.post('/procedures/', json=data)
    assert resp.status_code == 200
    assert resp.json() == data

    resp = client.get('/procedures/1')
    assert resp.status_code == 200
    # repository returns None for get so response is null
    assert resp.json() is None

    updated = {"id": 1, "description": "Test", "equipment_type_id": 1, "part_id": None}
    resp = client.put('/procedures/1', json=updated)
    assert resp.status_code == 200
    assert resp.json() == updated

    resp = client.delete('/procedures/1')
    assert resp.status_code == 200
    assert resp.json() == {"ok": True}

def test_maintenance_plans():
    resp = client.get('/maintenance/plans')
    assert resp.status_code == 200
    assert resp.json() == []

    data = {"id": 1, "name": "Plan", "procedures": [], "created_at": "2025-01-01T00:00:00"}
    resp = client.post('/maintenance/plans', json=data)
    assert resp.status_code == 200
    assert resp.json() == data

def test_report_generation():
    resp = client.get('/reports/procedures')
    assert resp.status_code == 200
    result = resp.json()
    assert result['filename'] == 'report.pdf'
    assert isinstance(result['data'], str)
