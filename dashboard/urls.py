from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('hood/new/', views.add_hood, name='create-hood'),
    path('hood/<int:id>/', views.hood_detail, name='hood-detail'),
    path('post/new/<int:hood_id>/', views.post, name='new-post'),
    path('posts/<int:id>/', views.hood_posts, name='hood-posts'),
]