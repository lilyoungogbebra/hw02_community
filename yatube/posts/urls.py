from django.urls import path

from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='home_page'),
    path('group/<slug:slug>/', views.group_posts, name='group_page'),
]
