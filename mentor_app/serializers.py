from rest_framework import serializers
from rest_framework import generics
from rest_framework.validators import UniqueValidator
from . import models
from django.contrib.auth.password_validation import validate_password


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class RegistrationSerializer(generics.CreateAPIView):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=models.User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_retry = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'password_retry', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

        def validate(self, attrs):
            if attrs['password'] != attrs['password_retry']:
                raise serializers.ValidationError({'password': "Password fields didn't match"})
            return attrs

        def create(self, validated_data):
            user = models.User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()

            return user
