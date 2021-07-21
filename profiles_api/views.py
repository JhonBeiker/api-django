from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers, models, permissions


# Create your views here.

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiView = [
            'Usamos metodo http (get, post, delete, put, patch)'
        ]

        return Response({'message': 'hello', 'data': an_apiView})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewSet = [
            'Usamos metodo http (list, create, retrivie, update, partial_update)',
            'Mapea automaticamente las URLs por medio del router'
        ]

        return Response({'message': 'hello', 'data': a_viewSet})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        return Response({'message': 'GET'})

    def update(self, request, pk=None):
        return Response({'message': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'message': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Crear y actualizar perfiles"""
    serializer_class = serializers.ProfileUserSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOneProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Crea tokens de autenticacion"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
