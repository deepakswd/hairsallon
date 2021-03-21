from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = "__all__"

class listServiceSerializer(serializers.ModelSerializer):
    service=ServicesSerializer(allow_null=True, required=False, many=True)
    class Meta:
        model = listService
        fields = "__all__"