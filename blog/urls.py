from django.urls import path
from .views import about, PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('about/', about, name='blog-about'),
]
