# -*- coding: utf-8 -*-
from app.models.businesslogic.helper.repository import Repository
from app.models.LogsModel import Logs


class LogsBL():

    def Insert_UsersLogs(self,pModel):
        rep = Repository()
        return rep.Insert(pModel)

    def Update_UsersLogs(self,pModel):
        rep = Repository()
        return rep.Update(pModel)

    def SelectOne_UsersLogs(self,pID):
        rep = Repository()
        return rep.SelectOne(Logs,pID)

    def SelectAll_UsersLogs(self):
        rep = Repository()
        return rep.SelectAll(Logs)

    def Delete_UsersLogs(self,pID):
        rep = Repository()
        return rep.Delete(Logs,pID)



