# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from config.database.connection import Connector

Base = declarative_base()

if Base:
  try:

        conn = Connector()
        ENGIN =  conn.ConnectorMySql()

  except:

        raise

