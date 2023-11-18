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
from django.urls import path
from Map import views as Map
from Cam import views as Cam
from Tests import views as Tests
from Test import views as Test
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the HackAI Backend!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mat/', Map.MatList.as_view()),
    path('cam/', Cam.CamList.as_view()),
    path('tests/', Tests.TestsList.as_view()),
    path('test/', Test.TestList.as_view()),
    path('', home_view),
]
