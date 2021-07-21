from rest_framework import permissions


class UpdateOneProfile(permissions.BasePermission):
    """Permite usuario editar su perfil"""
    def has_object_permission(self, request, view, obj):
        """Verificar si usuario intenta editar su perfil"""
        if request.metho in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id