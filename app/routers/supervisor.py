from fastapi import APIRouter

from . import Session
from ..models import SupervisorModel

router = APIRouter()
session = Session()
supervisor_query = session.query(SupervisorModel)


@router.get("/")
async def get_supervisors():
    return supervisor_query.all()


@router.get("/{supervisor_id}")
async def get_supervisor(supervisor_id: int):
    return supervisor_query.filter_by(id=supervisor_id).one()


@router.post("/{first_name}/{last_name}")
async def add_supervisor(first_name: str, last_name: str):
    new_supervisor = SupervisorModel(first_name=first_name, last_name=last_name)
    session.add(new_supervisor)
    session.commit()


@router.delete("/{supervisor_id}")
async def delete_employee(supervisor_id: str):
    supervisor = supervisor_query.filter_by(id=supervisor_id).one()
    session.delete(supervisor)
    session.commit()


@router.put("/{supervisor_id}/{first_name}/{last_name}")
async def update_employee(supervisor_id: int, first_name: str, last_name: str):
    supervisor = supervisor_query.filter_by(id=supervisor_id).one()
    supervisor.first_name = first_name
    supervisor.last_name = last_name
    session.commit()
