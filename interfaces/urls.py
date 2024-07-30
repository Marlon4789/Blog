from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_posts/', views.show_posts, name='show_posts'),
    path('detail/<int:quillpost_id>/', views.quillpost_detail, name='detail'),
]