from fastapi import FastAPI

from .routers import employee, supervisor, document
from .config import EMPLOYEE_PREFIX, SUPERVISOR_PREFIX, DOCUMENT_PREFIX

# app.main

app = FastAPI()

app.include_router(employee.router, prefix=EMPLOYEE_PREFIX)
app.include_router(supervisor.router, prefix=SUPERVISOR_PREFIX)
app.include_router(document.router, prefix=DOCUMENT_PREFIX)
