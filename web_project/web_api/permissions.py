from rest_framework import permissions


class UpdateProfile(permissions.IsAdminUser):
    """Allow superusers to edit profiles"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_superuser)
