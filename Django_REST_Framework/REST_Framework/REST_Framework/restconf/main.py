# Set up having default permission_classes & default authentication classes
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    # 'rest_framework.authentication.BasicAuthentication',
    'rest_framwork_jwt.authentication.JSONWebTokenAuthentication',
    'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated'
    )
}

# NOTE: Super cool! Now, if I want the default authentication or permission classes above, I do not have to define them in the API views!