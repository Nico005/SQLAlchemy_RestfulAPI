# -*- coding: utf-8 -*-
from app.models.BaseModel import Base
from sqlalchemy import Column, Integer, String, Date
from config.database.dbconfig import CONNECTOR
from app.models.BaseModel import ENGIN
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

UserBase = Base

from app.models.LogsModel import Logs




class Users(Base):

        __tablename__ = 'users'

        ID = Column(Integer, primary_key=True,autoincrement=True)
        Username = Column(String(50),nullable=False,unique=True)
        Email = Column(String(200),nullable=False,unique=True)
        Name = Column(String(20))
        Password = Column(String(50))
        Date = Column(Date)

if CONNECTOR:

        Base.metadata.create_all(ENGIN)