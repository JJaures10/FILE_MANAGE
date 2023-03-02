from rest_framework import permissions

class IsOfficeUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.type == 'OFFICE' or request.user.is_superuser

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'ADMIN' or request.user.is_staff