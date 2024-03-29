"""
URL configuration for first_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('first/', include('first.urls')),
    path('second/', include('second.urls')),
    path('third/', include('third.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('myapp/', include('myapp.urls')),
    path('rq/', include('rq_test.urls')),
]

urlpatterns += [
    path('django-rq/', include('django_rq.urls'))
]


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# jwt 토큰 생성 endpoint
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# api docs
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path

schema_view = get_schema_view(
openapi.Info(
        title="Swagger Study API",
        default_version="v1",
        description="Swagger Study를 위한 API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="jyyoon", email="jyyoon0615@naver.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
