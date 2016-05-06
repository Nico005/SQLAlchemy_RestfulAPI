# -*- coding: utf-8 -*-
from symbol import return_stmt
from app.models.BaseModel import Base
from config.database.connection import Connector
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm.scoping import scoped_session

connect = Connector()

class Repository():

        def Insert(self,pmodel):
            try:
                    Session = scoped_session(sessionmaker(bind=connect.ConnectorMySql()))
                    Base.query = Session.query_property()
                    ses = Session()
                    ses.add(pmodel)
                    ses.commit()
                    ses.refresh(pmodel)
                    ses.close()
                    return pmodel.ID

            except Exception as e:

                    raise Exception('Type Error In Insert :'+ str(e))

        def InsertWithOutGetID(self,pmodel):
            try:
                Session = scoped_session(sessionmaker(bind=connect.ConnectorMySql()))
                Base.query = Session.query_property()
                ses = Session()
                ses.add(pmodel)
                ses.commit()
                ses.close()
                return 

            except Exception as e:

                raise Exception('Type Error In Insert :'+ str(e))

        def Insert_InTransaction(self, pmodel, session):
            try:
                    session.add(pmodel)
                    #return id

            except Exception as e:

                    raise Exception('Type Error In Insert :'+ str(e))

        def Update(self, pmodel):
            try:
                    Session = sessionmaker(bind=connect.ConnectorMySql())
                    ses = Session()
                    ses.merge(pmodel)
                    ses.commit()
                    ses.close()
                    return 1

            except Exception as e:

                    raise Exception('Type Error In Update :'+ str(e))

        def Update_InTransaction(self, pmodel, session):
            try:
                    session.merge(pmodel)
                    return 1
            except Exception as e:

                    raise Exception('Type Error In Update :'+ str(e))

        def Delete_InTransaction(self, pModel, pID, session):
                try:
                   query = "DELETE FROM " + pModel.__tablename__ + " WHERE id=:pidd"
                   session.execute(query,{'pidd':pID})
                   return 1
                except Exception as e:
                    if "ForeignKey" in e.message:
                        return 0
                    raise Exception('Type Error In Delete :'+ str(e))

        def Delete(self,pModel,pID):

            try:
                   Session = sessionmaker(bind=connect.ConnectorMySql())
                   ses = Session()
                   our_model =  ses.query(pModel).filter_by(ID=pID).first()
                   ses.delete(our_model)
                   ses.commit()
                   ses.close()
                   return 1
            except Exception as e:

                    raise Exception('Type Error In Delete1 :'+ str(e))

        def SelectAll(self,pModel):

                try:
                        Session = scoped_session(sessionmaker(bind=connect.ConnectorMySql()))
                        ses = Session()
                        lst =  ses.query(pModel).all()
                        return lst

                except Exception as e:
                        raise Exception('Type Error In SelectAll :'+ str(e))

        def SelectAll_InTransaction(self, pModel, session):

                try:
                    lst =  session.query(pModel).all()
                    return lst
                except Exception as e:
                    raise Exception('Type Error In SelectAll :'+ str(e))

        def SelectOne(self, pModel, pID):
            try:
                   Session = sessionmaker(bind=connect.ConnectorMySql())
                   ses = Session()
                   our_model =  ses.query(pModel).filter_by(ID=pID).first()
                   ses.close()
                   return our_model

            except Exception as e:
                   raise Exception('Type Error In SelectOne :'+ str(e))

        def SelectOne_InTransaction(self, pModel, pID, session):
            try:
                   our_model =  session.query(pModel).filter_by(id=pID).first()
                   return our_model
            except Exception as e:

                   raise Exception('Type Error In SelectOne :'+ str(e))

        def Transaction(self,pModel):

            Session = sessionmaker(bind=connect.ConnectorMySql(),autocommit=True)
            sessiondb = Session()
            trans = sessiondb.begin()
            try:
                 ed_user   =  pModel(name="ramin",fullname="fara",password=1234345)
                 sessiondb.add(ed_user)
                 df = pModel(name="love",fullname=" sdfdfertgerg",password=1234345)
                 sessiondb.add(df)
                 trans.commit()

            except:
                trans.rollback()
                raise

