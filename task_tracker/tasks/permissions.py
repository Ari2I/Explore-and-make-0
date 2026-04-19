from rest_framework.permissions import BasePermission

class TaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        user = request.user

        if obj.project.owner == user:
            return True

        if obj.author == user:
            return True

        if obj.performer == user and request.method in ['PATCH', 'PUT']:
            return True

        return False

