from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    path('', include('books.urls')),
]
