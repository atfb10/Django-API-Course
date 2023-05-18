from rest_framework import pagination

class AFOREAPIPagination( pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 20