# -*- coding: utf-8 -*-
from app.models.UsersModel import UserBase
from sqlalchemy import Column, Integer, String
from config.database.dbconfig import CONNECTOR
from app.models.BaseModel import ENGIN
from sqlalchemy.orm import relationship , backref
from sqlalchemy.sql.schema import ForeignKey


class Logs(UserBase):

        __tablename__ = 'logs'

        ID = Column(Integer, primary_key=True,autoincrement=True)
        UserLog = Column(String(50))
        user_id = Column(Integer, ForeignKey('users.ID'))
        user = relationship("Users",lazy="joined", backref=backref('logs'))



if CONNECTOR:

        UserBase.metadata.create_all(ENGIN)