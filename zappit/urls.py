"""
URL configuration for zappit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="zappit API",
        default_version="1.0.0",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="CnJrQ@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    #Swagger
    path("swagger",schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-schema"),
    # Login
     path('api-auth/', include('rest_framework.urls')),
]
