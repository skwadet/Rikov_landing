"""untitled URL Configuration

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
from Rikov import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('upload_video/', views.PageCreate.as_view(), name='create_url'),
                  path('video/<str:slug>/', views.DetailView.as_view(), name='pages_url'),
                  path('tag/<str:slug>/', views.DetailTag.as_view(), name='tag_url'),
                  path('photos/', views.photo, name='photos'),
                  path('upload_photo/', views.create_page, name='upload_photo'),
                  path('control/', views.control, name='control')
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.pagenotfound