from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializers
    permission_classes = (IsAuthenticated,)
