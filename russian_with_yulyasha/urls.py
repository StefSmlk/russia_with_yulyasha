"""russian_with_yulyasha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from learning.views import learning_view_video, learning_view_photo, photo_comment_view, video_comment_view, \
    video_delete_comment_view, photo_delete_comment_view
from russian_with_yulyasha import settings
from russian_with_yulyasha.views import home_view

urlpatterns = [
    path('home', home_view, name='home'),
    path('learning/video', learning_view_video, name='video'),
    path('learning/photo', learning_view_photo, name='photo'),
    path('learning/photo/<int:image_id>', photo_comment_view, name='photo_comments'),
    path('learning/video/<int:video_id>', video_comment_view, name='video_comments'),
    path('learning/video/delete/<int:comment_id>', video_delete_comment_view, name='video_comments_delete'),
    path('learning/photo/delete/<int:comment_id>', photo_delete_comment_view, name='photo_comments_delete'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
