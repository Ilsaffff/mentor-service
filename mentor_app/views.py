from rest_framework import viewsets, permissions
from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializers
