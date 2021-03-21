from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, views, permissions
from django.utils.translation import gettext as _
import random
# from .models import *
# from .serializers import *

class UserLoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    pagination_class = None

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        admin = request.data.get('admin', None)
        if admin:
            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    return Response({"message": "Email or Password is Incorrect", 'status': 0})
                if not user.is_superuser:
                    return Response({"message": "You are not an Admin", 'status': 0},
                                    )
                try:
                    token = Token.objects.get(user=user)
                except:
                    token = Token.objects.create(user=user)
                first_name = ""
                if user.first_name:
                    first_name = user.first_name
                data = {
                    "name": first_name,
                    "id": user.id,
                    "username": user.username,
                    "token": token.key,
                }
                return Response({"data": data, "message": "Login Successful", 'status': 1},
                                status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Email and Password is required', 'status': 0})

        return Response({"message": "You are not an Admin", 'status': 0})