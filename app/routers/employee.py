from fastapi import APIRouter

from . import Session
from ..models import EmployeeModel

router = APIRouter()
session = Session()
employee_query = session.query(EmployeeModel)


@router.get("/")
async def get_employees():
    return employee_query.all()


@router.get("/{employee_id}")
async def get_employee(employee_id: int):
    return employee_query.filter_by(id=employee_id).one()


@router.post("/{first_name}/{last_name}/{department_name}/{title}")
async def add_employee(first_name: str, last_name: str, department_name: str, title: str):
    new_employee = EmployeeModel(
        department_name=department_name,
        first_name=first_name,
        last_name=last_name,
        title=title)
    session.add(new_employee)
    session.commit()


@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    employee_query.filter_by(id=employee_id).delete()
    session.commit()


@router.put("/{employee_id}/{first_name}/{last_name}/{department_name}/{title}")
async def update_employee(employee_id: int, first_name: str, last_name: str, department_name: str, title: str):
    employee = employee_query.filter_by(id=employee_id).one()
    employee.first_name = first_name
    employee.last_name = last_name
    employee.department_name = department_name
    employee.title = title
    session.commit()
