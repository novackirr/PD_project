from rest_framework.permissions import BasePermission

class IsEmailVerifed(BasePermission):
    message = "Email не подтверждён!"

    def has_permission(self, request, view):
        user = request.user
        if user.email_verified:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True