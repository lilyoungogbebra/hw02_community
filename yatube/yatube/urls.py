from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='page')),
    path('admin/', admin.site.urls),
]
