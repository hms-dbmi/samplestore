from rest_framework import permissions
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)

class IsAssociatedUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
