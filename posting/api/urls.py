from django.urls import path, include
from .views import BlogPostRudView, BlogPostApiView

urlpatterns = [
    path('', BlogPostApiView.as_view(), name='post-api'),
    path('<pk>/', BlogPostRudView.as_view(), name='post-rude')
]
