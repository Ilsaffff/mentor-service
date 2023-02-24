from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from . import models
from . import serializers
from rest_framework import generics


class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)


class RegistrationView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.RegistrationSerializer
    permission_classes = (AllowAny,)


class OnboardingView(generics.ListAPIView):
    queryset = models.Module.objects.all()
    serializer_class = serializers.OnboardingSerializer
    permission_classes = (IsAuthenticated,)
