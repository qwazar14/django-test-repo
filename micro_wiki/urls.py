from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='wiki-home'),
    path('  about', views.index, name='wiki-about'),
    # path('create', views.create, name='create'),
]
