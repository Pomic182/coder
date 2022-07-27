from django.contrib import admin
from django.urls import path
from integrantes.views import create_member, list_member

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_member/', create_member, name='create_member'),
    path('list_member/', list_member, name='list_member')
]
