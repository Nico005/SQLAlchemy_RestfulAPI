# -*- coding: utf-8 -*-
from app.models.businesslogic.helper.repository import Repository
from app.models.UsersModel import Users


class UserBL():

    def Insert_Users(self,pModel):
        rep = Repository()
        return rep.Insert(pModel)

    def Update_Users(self,pModel):
        rep = Repository()
        return rep.Update(pModel)

    def SelectOne_Users(self,pID):
        rep = Repository()
        return rep.SelectOne(Users,pID)

    def SelectAll_Users(self):
        rep = Repository()
        return rep.SelectAll(Users)

    def Delete_Users(self,pID):
        rep = Repository()
        return rep.Delete(Users,pID)

    def Find_Users(self,pID):
        rep = Repository()
        return rep.Find(Users,pID)

    def FindUsername(self,username):
        rep = Repository()
        return rep.Search_Username(Users,username)


