from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id



class OwnerUpdate(permissions.BasePermission):
    """Allow users to update their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author.id == request.user.id