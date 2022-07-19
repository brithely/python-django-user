from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_app.urls.api'))
]

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    schema_view = get_schema_view( 
    openapi.Info( 
        title="Django User API", 
        default_version="v1", 
        description="Django User API", 
        contact=openapi.Contact(name="정승룡", email="bing9013@naver.com"), 
    ), 
    public=True
    )

    urlpatterns += [
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]
