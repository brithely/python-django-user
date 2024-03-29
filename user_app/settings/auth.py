from datetime import timedelta

from user_app.settings.core import SECRET_KEY

AUTH_USER_MODEL = 'users.User'
REST_USE_JWT = True
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=60),

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'AUTH_HEADER_TYPES': 'JWT',

    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': "none",
    'OPERATIONS_SORTER': "alpha",
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
}
