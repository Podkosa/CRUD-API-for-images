"""ImagiON_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT
from django.views.generic.base import TemplateView
from rest_framework.schemas import get_schema_view

# from django.http import HttpRequest
# from images.views import logger
urlpatterns = [
    path('img/', include('images.urls')),
    path('', TemplateView.as_view(template_name='homepage.html')),
    
    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
        title="Images for ImagiON",
        description="Open API generation",
        version="1.0.0"
    ), name='openapi-schema'),
]
urlpatterns += static (MEDIA_URL, document_root=MEDIA_ROOT)
