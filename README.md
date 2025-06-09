**Preventive Maintenance API**

**Objetivo**
Apresentar a organizacao da API de Manutencao Preventiva segundo os principios SOLID e Clean Code, enfatizando geracao de relatorios em PDF e filtros de consulta, incluindo estrutura de codigo e principais rotas.

---

## 1. Principios Gerais

* **Single Responsibility Principle (SRP)**: Cada modulo possui uma unica responsabilidade.
* **Open/Closed Principle (OCP)**: Sistema aberto para extensao e fechado para modificacao.
* **Liskov Substitution Principle (LSP)**: Subtipos intercambiaveis sem alteracao de comportamento.
* **Interface Segregation Principle (ISP)**: Interfaces especificas para cada cliente, evitando metodos irrelevantes.
* **Dependency Inversion Principle (DIP)**: Dependencia em abstracoes (interfaces), nao em implementacoes.

---

## 2. Camadas de Arquitetura

1. **Presentation Layer**

   * FastAPI routers: recebe requisicoes HTTP e retorna respostas.
   * Validacoes de entrada (Pydantic) e formatacao de saida.

2. **Application Layer (Services/Use Cases)**

   * Orquestra a logica de negocio: servicos puros que executam casos de uso.
   * Define interfaces (abstracoes) para repositorios e modulos de relatorio.

3. **Domain Layer**

   * Entidades e regras de negocio: EquipmentType, Part, Procedure, MaintenancePlan.
   * Validacoes e invariantes de dominio.

4. **Infrastructure Layer**

   * Implementacoes de repositorios (SQLAlchemy).
   * Gerador de PDF (ReportLab, WeasyPrint, etc.).
   * Modulos de filtros e paginacao genericos.
   * Configuracao de banco e dependencias.

---

## 3. Estrutura de Codigo

```
project/
└─ app/
   ├─ main.py               # Instancia FastAPI e inclui routers
   ├─ settings.py           # Configuracoes gerais e variaveis de ambiente
   ├─ db.py                 # Engine, SessionLocal, Base e dependencia get_db
   ├─ domain/
   │   ├─ entities.py       # Definicoes de classes de dominio
   │   └─ interfaces.py     # Protocolos (abstracoes) de repositorios
   ├─ schemas/
   │   ├─ equipment.py      # Pydantic models: EquipmentType, Part
   │   ├─ procedure.py      # Pydantic models: Procedure, Create/Update
   │   ├─ maintenance.py    # Pydantic models: MaintenancePlan, Execute, Validate
   │   └─ report.py         # Pydantic models: ReportRequest, ReportResponse
   ├─ adapters/
   │   ├─ repository_sql.py # Implementacoes SQLAlchemy dos repositorios
   │   └─ pdf_generator.py  # Servico para criacao de PDF
   ├─ services/
   │   ├─ equipment_service.py   # Logica de EquipmentType e Part
   │   ├─ procedure_service.py   # Logica de CRUD e filtros de Procedure
   │   ├─ maintenance_service.py # Logica de planos, execucao e validacao
   │   └─ report_service.py      # Logica de geracao de relatorios
   └─ routers/
       ├─ equipment_router.py    # Endpoints de Equipment
       ├─ procedure_router.py    # Endpoints de Procedure
       ├─ maintenance_router.py  # Endpoints de MaintenancePlan
       └─ report_router.py       # Endpoints de geracao de PDF
```

---

## 4. Principais Rotas HTTP

| Metodo     | Rota                                      | Descricao                                            |
| ---------- | ----------------------------------------- | ---------------------------------------------------- |
| **GET**    | `/equipment/types`                        | Lista todos os tipos de equipamento                  |
| **GET**    | `/equipment/parts?equipment_type_id={id}` | Lista pecas, opcionalmente filtradas por tipo        |
| **GET**    | `/procedures`                             | Lista procedimentos com filtros e paginacao          |
| **POST**   | `/procedures`                             | Cria um novo procedimento                            |
| **GET**    | `/procedures/{id}`                        | Detalha um procedimento                              |
| **PUT**    | `/procedures/{id}`                        | Atualiza um procedimento                             |
| **DELETE** | `/procedures/{id}`                        | Remove um procedimento                               |
| **GET**    | `/maintenance/plans`                      | Lista planos de manutencao                           |
| **POST**   | `/maintenance/plans`                      | Cria um novo plano de manutencao                     |
| **POST**   | `/maintenance/plans/{id}/execute`         | Executa tarefa de manutencao (marca como concluida)  |
| **POST**   | `/maintenance/plans/{id}/validate`        | Valida checklist e finaliza execucao                 |
| **GET**    | `/reports/procedures?equipment_type=&...` | Gera e retorna PDF de procedimentos conforme filtros |

**Exemplo de `main.py`:**

```python
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
```

---

## 5. Consideracoes de Clean Code

* **Nomes Descritivos**: Classes, funcoes e variaveis refletindo proposito claro.
* **Baixo Acoplamento**: Injecao de dependencias e uso de interfaces.
* **Alta Coesao**: Modulos focados em responsabilidades especificas.
* **Tratamento de Erros**: Erros de dominio distintos de erros de infraestrutura.
* **Testabilidade**: Servicos desacoplados de framework, facilitando testes unitarios.

---

*Este documento serve de guia para implementacao e escalabilidade da API.*
