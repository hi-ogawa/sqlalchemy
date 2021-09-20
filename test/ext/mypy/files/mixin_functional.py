from typing import Callable

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.decl_api import declarative_mixin


Base = declarative_base()


class Mixin:
    x = Column(Integer)
    y = Column(String)


class A(declarative_mixin(Mixin), Base):
    __tablename__ = "a"
