from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

BASE = declarative_base()


class EmployeeModel(BASE):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    department_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    title = Column(String)
