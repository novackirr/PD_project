from rest_framework.permissions import BasePermission

class IsEmailVerifedAndUserAuth(BasePermission):
    message = "Email не подтверждён!"

    def has_permission(self, request, view):
        user = request.user
        if request.auth is None:
            return False
        if user.email_verified:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True

class IsTeacher(IsEmailVerifedAndUserAuth):
    message = "Вы не являетесь учителем!"

    def has_permission(self, request, view):
        groups = []
        for a in request.user.groups.values_list('name'):
            groups += [a[0]]
        if 'Преподаватель' in groups:
            return True
        return False