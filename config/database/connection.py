# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database.dbconfig import MySQLInfo
from config.database.dbconfig import PostgresInfo

class Connector():

    def ConnectorMySql(self):
        try:
            info = MySQLInfo()
            con = 'mysql://%s:%s@%s:%s/%s?charset=utf8'% (info.USERNAME,info.PASSWORD,info.IPADDRESSDATABASE,info.PORT,info.DBNAME)
            self.engine = create_engine(con, echo=True)
            return self.engine

        except Exception as e:
            raise Exception("Error : %s" % e)


class ConnectorPostgres():


    try:

        def connect(self):
            self.con = 'postgresql://{}:{}@{}:{}/{}?charset=utf-8'.format(PostgresInfo().USERNAME,PostgresInfo().PASSWORD,PostgresInfo().IPADDRESSDATABASE,PostgresInfo().PostgresInfo().PORT,PostgresInfo().DBNAME)
            self.engine = create_engine(self.con, echo=True)
            return self.engine

    except Exception as e:
        raise e


class ConnectorOracle():

    try:

        def connect(self):
            self.engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname?charset=utf-8', echo=True)
            Session = sessionmaker(bind=self.engine)
            session = Session()

    except Exception as e:
        raise Exception("Error : %s" % e)


class ConnectorSQLite():

    try:

        def connect(self):
            self.engine = create_engine('sqlite:////absolute/path/to/foo.db?charset=utf-8', echo=True)
            Session = sessionmaker(bind=self.engine)
            session = Session()

    except Exception as e:
        raise Exception("Error : %s" % e)
