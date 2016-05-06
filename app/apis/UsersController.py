# -*- coding: utf-8 -*-
from app.models.UsersModel import Users
from app.models.businesslogic.UsersBL import UserBL
from django.shortcuts import HttpResponse
from serialization.UsersSerializer import UsersSchema , LogsSchema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(['GET'])
def UserModel_SelectAll(request):

    try:

        if request.method == 'GET':
            usermodel_object = UserBL().SelectAll_Users()
            if usermodel_object:
                users_schema = UsersSchema(many=True)
                if users_schema:
                    to_json = users_schema.dump(usermodel_object,many=True).data
                    return Response(to_json,status=status.HTTP_201_CREATED)

            return HttpResponse('Try Again')
        return HttpResponse('Invalid Method')

    except Exception as e:
        raise


@api_view(['POST'])
def UserModel_Insert(request):

    try:

        if request.method == 'POST':
            usermodel = request.POST
            from serialization.UsersSerializer import Session
            users_schema = UsersSchema()
            json_dict = users_schema.load(usermodel,session=Session).data
            usermodel_object = UserBL().Insert_Users(json_dict)
            if usermodel_object:
                result = {'status':'True'}
                return Response(json.dumps(result))

    except Exception as e:
        raise


@api_view(['DELETE'])
def UserModel_Delete(request,pk):
    try:

        usermodel_object = UserBL().Delete_Users(pk)
        if usermodel_object:
            result = json.dumps({'status':'True'})
            return Response(result)

    except Exception as e:
        raise

@api_view(['PUT'])
def UserMOdel_Update(request,pk):

    try:

        usermodel_selectone = UserBL().SelectOne_Users(pk)
        if usermodel_selectone:
            if request.method == 'PUT':
                usermodel_update = request.POST
                from serialization.UsersSerializer import Session
                users_schema = UsersSchema()
                usermodel_selectone = users_schema.load(usermodel_update,session=Session).data
                update = UserBL().Update_Users(usermodel_selectone)
                if update:
                    result = json.dumps({'status':'True'})
                    return Response(result)

    except Exception as e:

        raise