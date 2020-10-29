from rest_framework import permissions

from .utils import get_auth0_user_id_from_request


class IsCreator(permissions.BasePermission):
    message = 'You must be the creator of this object.'

    def has_object_permission(self, request, view, obj):
        auth0_user_id = get_auth0_user_id_from_request(request)
        return obj.created_by == auth0_user_id