from django.contrib import admin
from django.urls import path
from perfis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('perfil/<int:perfil_id>',
    				views.exibir, name='exibir'),
    path('perfil/<int:perfil_id>/convidar',
    				views.convidar, name='convidar'),
]
