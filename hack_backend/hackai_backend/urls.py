"""
URL configuration for hackai_backend project.

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
from Map.views import MatList, MatViewSet
from Cam.views import Cam, CamViewSet
from Tests.views import Tests, TestsListViewSet
from Test.views import Test, TestListViewSet
from django.http import HttpResponse
from rest_framework import routers
urlpatterns = [
    # ... other paths ...
    path('mat/', MatList.as_view()),
    path('cam/', Cam),
    path('tests/', Tests),
    path('test/', Test),
]

from django.shortcuts import render
from django.http import HttpResponse

router = routers.DefaultRouter()
router.register(r'Map', MatViewSet, basename='Map')
router.register(r'Test', TestListViewSet, basename='Test')
router.register(r'Cam', CamViewSet, basename='Cam')
router.register(r'Tests', TestsListViewSet, basename='Tests')

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('mat/', MatList.as_view()),
    path('cam/', Cam),
    path('tests/', Tests),
    path('test/', Test),
    path('', home_view),
]
