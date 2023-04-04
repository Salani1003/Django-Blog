from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # print(request.data)
        # print(request.query_params)
        # print(request.content_type)
        # print(request.method)
        if request.method == 'GET':
            print(request.user)              
            return True
        else:
            return request.user.is_staff