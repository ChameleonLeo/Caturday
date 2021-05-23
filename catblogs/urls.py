from django.urls import path, include
from . import views

app_name = 'catblogs'

urlpatterns = [
    path('', views.PostListView.as_view(), name='catpost_list'),
    path('catpost/', include([
        path('new/', views.catpost_new, name='catpost_new'),
        path('my_posts/', views.MyPostListView.as_view(), name='catpost_my_posts'),
        path('recent/', views.RecentPostListView.as_view(), name='catpost_recent'),
        path('archive/', views.ArchivePostListView.as_view(), name='catpost_archive'),
        path('short_stories/', views.ShortPostListView.as_view(), name='catpost_short'),
        path('articles/', views.ArticlePostListView.as_view(), name='catpost_article'),
        path('<int:pk>/', views.catpost_detail, name='catpost_detail'),
        path('<int:pk>/edit/', views.catpost_edit, name='catpost_edit'),
    ])),
]
