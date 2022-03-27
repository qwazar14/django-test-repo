from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('wiki/', include('micro_wiki.urls')),
    path('books/', include('books.urls')),
]
