from django.urls import path, include   
from . import views
from .feeds import LatestPostsFeed


app_name = 'blog'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/share/', views.post_share, name='post_share'),
    path('<int:id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
