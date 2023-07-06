from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("test/data", views.data()),
    path("test/list", views.list())
]