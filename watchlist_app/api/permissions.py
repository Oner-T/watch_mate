from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        # admin_permission = bool(request.user and request.user.is_staff) # This is same as below
        admin_permission = super().has_permission(request, view)
    
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return admin_permission
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user # checks the review objects user equals to the login user
    