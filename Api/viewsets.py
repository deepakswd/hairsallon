from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse 
from hairsaloon.mixins import CustomMixins

# User = get_user_model()

class UserViewSet(CustomMixins, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # pagination_class = None

    def get_queryset(self):
        if self.request.query_params.get("username"):
            return User.objects.filter(username__icontains=self.request.query_params.get("username")).exclude(id=self.request.user.id)
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        # confirm_password = request.data.get('confirm_password', None)
        image = request.FILES.get("image", None)
        if username and email and password:
            get_user = User.objects.filter(email=username)
            if get_user:
                return Response({'message': 'Email already exists', 'status': 0})
            # if password != confirm_password:
            #     return Response({'message': 'Password and confirm password doesnot match    ', 'status': 0})
            user = User.objects.create(
                email=email, username=username, password=password)
            if name:
                user.first_name = name
            user.set_password(user.password)

            if image:
                user.image = image

            user.save()
        # other_user = User.objects.get(id=1)
        # Follow.objects.add_follower(request.user, other_user)

            return Response({"message": "User Created Successfully", 'status': 1},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Email, Password and Username is required', 'status': 0})

    @action(detail=True, methods=["post"], url_path="update")
    def edit_user(self, request, *args, **kwargs):
        user = self.get_object()
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        confirm_password = request.data.get("confirm_password", None)
        name = request.data.get("name", None)
        image = request.FILES.get("image")
        if email and name:
            get_user = User.objects.filter(email=email).exclude(id=user.id)
            if get_user:
                return Response({"message": "Email Already Exist", "status": 0})
            user.email = email

            if password != "undefined":
                if password == confirm_password:
                    user.set_password(password)
                else:
                    return Response({"message": "Password and confirm Password does not match", "status": 0})
            if name:
                user.first_name = name
            else:
                user.first_name = ""
            if image:

                user.image = image
            else:
                user.image = ""
            user.save()
            data = {
                # "image": user.image,
                "email": user.email,
                "name": user.first_name,
            }
            return Response({"data": data, "message": "User Updated Successfully", "status": 1})

        else:
            return Response({'message': 'Email and Name is required', 'status': 0})


class ServiceViewSet(CustomMixins, viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    permission_classes = (AllowAny,)
    # pagination_class = None

    def get_queryset(self):
        # if self.request.query_params.get("username"):
        #     return Services.objects.filter(username__icontains=self.request.query_params.get("username")).exclude(id=self.request.user.id)
        return Services.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        description = request.data.get('description', None)
        price = request.data.get('price', None)
        if name and price:
            service = Services.objects.create(
                name=name,description=description,price=price)
            service.save()

            return Response({"message": "Service Created Successfully", 'status': 1},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Name and price is required', 'status': 0})

    @action(detail=True, methods=["post"], url_path="update")
    def edit_service(self, request, *args, **kwargs):
        service = self.get_object()
        name = request.data.get('name')
        description = request.data.get('description', None)
        price = request.data.get('price', None)
        if name and price:
            service.name=name
            service.price=price
            if description:
                service.description=description
            service.save()
            return Response({'message': 'Service Updated Successfully', 'status': 1})
        else:
            return Response({'message': 'Name and price is required', 'status': 0})

class ListServicesViewSet(CustomMixins, viewsets.ModelViewSet):
    serializer_class = listServiceSerializer
    permission_classes = (IsAuthenticated,)
    # pagination_class = None

    def get_queryset(self):
        return listService.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name:
            listservice = listService.objects.create(
                name=name)
            # ids = 
            ids=request.data.get("id",None)
            if ids:
                for id in ids:
                    service = Services.objects.filter(id=int(id)).first()
                    listservice.service.add(service)
                    listservice.save()

            return Response({"message": "List Service Created Successfully", 'status': 1},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Name is required', 'status': 0})

    @action(detail=True, methods=["post"], url_path="update")
    def edit_service(self, request, *args, **kwargs):
        listservice = self.get_object()
        name = request.data.get('name')
        if name:
            listservice.name=name
            id=request.data.get("id")
            if id:
                for id in ids:
                    service = service.object.filter(id=int(id)).first()
                    listservice.service.add(service)
                    listservice.save()

            return Response({"message": "List Service Created Successfully", 'status': 1},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Name is required', 'status': 0})