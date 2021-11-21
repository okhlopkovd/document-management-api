from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean

BASE = declarative_base()


class EmployeeModel(BASE):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    department_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    title = Column(String)

    documents_created = relationship("DocumentModel", foreign_keys="DocumentModel.creator_id",
                                     cascade="all,delete")
    documents_in_charge_of = relationship("DocumentModel", foreign_keys="DocumentModel.employee_in_charge_id",
                                          cascade="all,delete")


class SupervisorModel(BASE):
    __tablename__ = "supervisor"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    documents = relationship("DocumentModel", cascade="all,delete")


class DocumentModel(BASE):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    document_type = Column(String)
    release_date = Column(Date)
    complete_date = Column(Date, nullable=True)
    content = Column(String)

    creator_id = Column(Integer, ForeignKey("employee.id"))
    employee_in_charge_id = Column(Integer, ForeignKey("employee.id"))
    signer_id = Column(Integer, ForeignKey("supervisor.id"))

    events = relationship("EventModel", cascade="all,delete")


class EventModel(BASE):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_completed = Column(Boolean)

    document_id = Column(Integer, ForeignKey("document.id"))
