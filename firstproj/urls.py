"""
URL configuration for firstproj project.

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
from home.views import *
from vege.views import *

urlpatterns = [
    path("", home, name="home"),
    path("recipes/", recipes, name="recipes"),
    path("delete_recipe/<id>/", delete_recipe, name="delete_recipe"),
    path("login/", login_page, name="login_page"),
    path("register/", register_page, name="register_page"),
    path("update-recipe/<id>/", update_recipe, name="update_recipe"),
    path("aboutus/", aboutus, name="about"),
    path("contact/", contact, name="contact"),
    path("admin/", admin.site.urls),
]