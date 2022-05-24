from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Give read-only access if user is not owner of object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
