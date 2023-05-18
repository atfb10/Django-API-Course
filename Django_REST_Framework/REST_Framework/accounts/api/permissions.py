from rest_framework import permissions

class BlackListPermission(permissions.BasePermission):
    '''
    global permission check for blacklisted IPs
    '''
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted
    
class AnonymousPermission(permissions.BasePermission):
    '''
    global permission check for anonymous IPs (non authenticated users)
    '''
    def has_permission(self, request, view):
        return not request.user.is_authenticated

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    object-level permission to only allow owners of an object to edit it
    Assumes model instance has an owner attribute
    '''
    message = 'You must be the owner to update or delete'
    def has_object_permission(self, request, view, obj):
        '''
        read permissions are allowed to any request
        so we will always allow GET, HEAD or OPTIONS requests
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Instance must have an attribute named owner
        return obj.owner == request.user