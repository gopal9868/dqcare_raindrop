"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from .router import router
from raindrop.views.create_file import create_file1
from raindrop.views.get_tc_details import get_conn_dtl
from raindrop.views.external.generate_schedule_script import gen_schedule_script
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/create_file/<int:id>', create_file1),
    path('api/execute_tc/<int:id>', get_conn_dtl),
    path('api/generate_schedule/', gen_schedule_script),
]
