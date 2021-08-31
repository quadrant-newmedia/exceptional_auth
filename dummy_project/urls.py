"""dummy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

import exceptional_auth

def login_required(request):
    raise exceptional_auth.LoginRequired()
def permission_denied(request):
    raise exceptional_auth.PermissionDenied()
def not_currently_allowed(request):
    raise exceptional_auth.NotCurrentlyAllowed('test message')

urlpatterns = [
    path('login_required/', login_required),
    path('permission_denied/', permission_denied),
    path('not_currently_allowed/', not_currently_allowed),
]
