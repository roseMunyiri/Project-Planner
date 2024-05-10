from rest_framework import permissions

class isAdminorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):   
        return request.user.is_authenticated or request.user.is_superuser
    

