# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login , logout
from app.models.businesslogic.UsersBL import UserBL
from rest_framework.decorators import api_view
from django.http import JsonResponse


api_view(['GET'])
def SignIn(request):

    try:

        if request.method == 'GET':

            user_data = request.GET.dict()
            if user_data:
                usermodel_object = UserBL().FindUsername(user_data['Username'])
                if usermodel_object:
                    user = authenticate(username=user_data['Username'].encode("UTF-8"), password=user_data['Password'].encode("UTF-8"))
                    if user:
                        login(request, user)
                        #logout(request)

                        return JsonResponse({'status':'True'})

                    return JsonResponse({'status':'Not Found Account on Auth Users'})

                return JsonResponse({'status':'Not Found Account'})

            return JsonResponse({'status':'Empty Parameter Request'})

        return JsonResponse({'status':'Invalid Requset Method'})

    except Exception as e:
        raise