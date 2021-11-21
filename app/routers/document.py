import datetime
from datetime import datetime as d

from typing import List
from fastapi import APIRouter

from . import Session
from ..models import DocumentModel, EventModel

router = APIRouter()
session = Session()
document_query = session.query(DocumentModel)


@router.get("/")
async def get_documents():
    return document_query.all()


@router.get("/{document_id}")
async def get_document(document_id: int):
    return document_query.filter_by(id=document_id).one()


@router.post("/{document_type}/{release_date}/{complete_date}/{content}/"
             "{creator_id}/{employee_in_charge_id}/{signer_id}")
async def add_document(document_type: str, release_date: datetime.date, complete_date: str,
                       content: str, creator_id: int, employee_in_charge_id: int, signer_id: int, events: List[str]):
    if complete_date == "none":
        complete_date = None
    else:
        complete_date = d.fromisoformat(complete_date)

    new_document = DocumentModel(document_type=document_type,
                                 release_date=release_date,
                                 complete_date=complete_date,
                                 content=content,
                                 creator_id=creator_id,
                                 employee_in_charge_id=employee_in_charge_id,
                                 signer_id=signer_id)
    session.add(new_document)
    session.commit()

    for event_name in events:
        new_event = EventModel(name=event_name,
                               is_completed=complete_date is not None,
                               document_id=new_document.id)
        session.add(new_event)
    session.commit()


@router.delete("/{document_id}")
async def delete_document(document_id: str):
    document = document_query.filter_by(id=document_id).one()
    session.delete(document)
    session.commit()


@router.put("{document_id}/{document_type}/{release_date}/{complete_date}/{content}/"
            "{creator_id}/{employee_in_charge_id}/{signer_id}")
async def update_document(document_id: int, document_type: str, release_date: datetime.date,
                          complete_date: datetime.date, content: str, creator_id: int, employee_in_charge_id: int,
                          signer_id: int):
    document = document_query.filter_by(id=document_id).one()
    document.document_type = document_type
    document.release_date = release_date
    document.complete_date = complete_date
    document.content = content
    document.creator_id = creator_id
    document.employee_in_charge_id = employee_in_charge_id
    document.signer_id = signer_id
    session.commit()
