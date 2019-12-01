from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='criar'),
    path('post/<int:pk>/', views.post_detail, name='detail'),

]
