from . import views
from django.urls import path
from .feeds import LatestPostsFeed
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    
    path('upload/',image_upload_view , name='upload'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
