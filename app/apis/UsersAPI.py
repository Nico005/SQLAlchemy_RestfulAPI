# -*- coding: utf-8 -*-
from app.models.UsersModel import Users
from app.models.LogsModel import Logs
from app.models.businesslogic.UsersBL import UserBL
from app.models.businesslogic.LogsBL import LogsBL
from django.http import JsonResponse
from serialization.UsersSerializer import UsersSchema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serialization.UsersSerializer import Session
import json


@api_view(['GET'])
def UserModel_SelectAll(request):

    try:

            if request.method == 'GET':
                if request.user.is_authenticated():
                    usermodel_object = UserBL().SelectAll_Users()
                    if usermodel_object:
                        users_schema = UsersSchema(many=True)
                        if users_schema:
                            to_json = users_schema.dump(usermodel_object,many=True).data
                            return Response(to_json,status=status.HTTP_201_CREATED)
                    return Response(json.dumps({'status':'Try Again'}))

                return Response(json.dumps({'status':'Invalid authenticated'}))
            return Response(json.dumps({'status':'Invalid Request Method'}))

    except Exception as e:
        return Response(json.dumps({'status':e}))

@api_view(['POST'])
def UserModel_Insert(request):

    try:

        if request.method == 'POST':
            usermodel = request.POST
            users_schema = UsersSchema()
            if users_schema:
                json_dict = users_schema.load(usermodel,session=Session).data
                usermodel_object = UserBL().Insert_Users(json_dict)
                if usermodel_object:
                    logmodel = Logs(user_id=usermodel_object,UserLog="Hello Ramin This is a test ")
                    logmodel_object = LogsBL().Insert_UsersLogs(logmodel)
                    if logmodel_object:
                        return Response(json.dumps({'status':'True'}))
                return Response(json.dumps({'status':'Error in Insert Model'}))

        return JsonResponse({'status':'Invalid Request Method'})

    except Exception as e:
        return Response(json.dumps({'status':e}))

@api_view(['DELETE'])
def UserModel_Delete(request,pk):

    try:

        if request.method == 'DELETE':
            usermodel_object = UserBL().Delete_Users(pk)
            if usermodel_object:
                    return Response(json.dumps({'status':'True'}))

            return Response(json.dumps({'status':'Not Found Account'}))
        return JsonResponse({'status':'Invalid Request Method'})

    except Exception as e:
       return Response(json.dumps({'status':e}))


@api_view(['PUT'])
def UserMOdel_Update(request,pk):

    try:
        if request.method == 'PUT':
            usermodel_selectone = UserBL().SelectOne_Users(pk)
            if usermodel_selectone:

                    usermodel_update = request.POST
                    users_schema = UsersSchema()
                    if users_schema:
                        usermodel_update = users_schema.load(usermodel_update,session=Session).data
                        usermodel_update.ID = usermodel_selectone.ID
                        update = UserBL().Update_Users(usermodel_update)
                        ## If you need update log model here if you need else empty to update model log
                        if update:
                            return Response(json.dumps({'status':'True'}))

            return Response(json.dumps({'status':'Not Found Account'}))

        return Response(json.dumps({'status':'Invalid Request Method'}))

    except Exception as e:

        return Response(json.dumps({'status':e}))


@api_view(['GET'])
def UserModel_Search(request,pk):

    try:
        if request.method == "GET":
            usermodel_object = UserBL().Find_Users(pk)
            if usermodel_object:
                users_schema = UsersSchema(many=True)
                if users_schema:
                    to_json = users_schema.dump(usermodel_object,many=True).data
                    return Response(to_json,status=status.HTTP_201_CREATED)

            return Response(json.dumps({'status':'Not Found Account'}))

        return Response(json.dumps({'status':'Invalid Request Method'}))

    except Exception as e:

        return Response(json.dumps({'status':e}))


@api_view(['GET'])
def UserModel_SearchUsername(request,username):

    try:
        if request.method == 'GET':

            usermodel_object = UserBL().FindUsername(username)
            if usermodel_object:

                users_schema = UsersSchema(many=True)
                if users_schema:
                    to_json = users_schema.dump(usermodel_object,many=True).data
                    return Response(to_json,status=status.HTTP_201_CREATED)

            return Response(json.dumps({'status':'Not Found Account'}))
        return Response(json.dumps({'status':'Invalid Request Method'}))

    except Exception as e:
        return Response(json.dumps({'status':e}))
