from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


# usuário tem permissao para acessar um recurso.
# apenas usuários autenticados com permissao de staff podem realizar operaçoes de escrita ('GET', 'HEAD', 'OPTIONS').
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and (
            request.user.is_staff or request.method in permissions.SAFE_METHODS
        )


# verificar se o usuário autenticado pode acessar ou modifica
# funcionário pode acessar e modificar qualquer objeto de usuário.
class IsAuthenticatedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User) -> bool:
        return obj.email == request.user.email or request.user.is_employee
