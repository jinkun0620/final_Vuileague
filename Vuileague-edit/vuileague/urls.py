"""vuileague URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from league import views

# 새로운 내용
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('make_team/', views.make_team, name="make_team"),
    path('detail_team/<int:profile_pk>/', views.detail_team, name="detail_team"),
    path('make_match/', views.make_match, name="make_match"),
    path('detail_match/<int:match_pk>/', views.detail_match, name="detail_match"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
