"""
URL configuration for ERP project.

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
from django.urls import path, include

# COMMON HEADER TEMPLATE URL FOR STATIC FILES AND MEDIA - STARTS 
from ERP import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static 
# COMMON HEADER TEMPLATE URL FOR STATIC FILES AND MEDIA - ENDS 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]

# COMMON URL BODY TEMPLATE FOR STATIC FILES AND MEDIA - STARTS 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
 
urlpatterns += staticfiles_urlpatterns() 
# COMMON URL BODY TEMPLATE FOR STATIC FILES AND MEDIA - ENDS