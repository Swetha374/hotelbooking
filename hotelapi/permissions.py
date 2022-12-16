from rest_framework.permissions import BasePermission


class IsHotelCreateAccess(BasePermission):
    message="you dont have permission to create a hotel"
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if  request.user.usertype == "Hotel":
                return True
        return False








