# Set up having default permission_classes & default authentication classes
import datetime
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    # 'rest_framework.authentication.BasicAuthentication',
    'rest_framwork_jwt.authentication.JSONWebTokenAuthentication',
    'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ),
    'DEFAULT_PAGINATION_CLASS': 'REST_Framework.restconf.pagination.AFOREAPIPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    # 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'accounts.api.utils.jwt_response_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}

# NOTE: Super cool! Now, if I want the default authentication or permission classes above, I do not have to define them in the API views!