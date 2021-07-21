from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializador para campo nombre de prebas"""
    name = serializers.CharField(max_length=10)


class ProfileUserSerializer(serializers.ModelSerializer):
    """Serializador para perfilies de usuarios"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

        def crete(self, validate_data):
            """Crear y retornar nuevo usuario"""
            user = models.UserProfile.object.create_user(
                email=validate_data['email'],
                name=validate_data['name'],
                password=validate_data['password']
            )

            return user

        def update(self, instance, validate_data):
            """Actualiza cuenta de usuario"""
            if 'password' in validate_data:
                password = validate_data.pop('password')
                instance.set_password(password)

            return super().update(instance, validate_data)

