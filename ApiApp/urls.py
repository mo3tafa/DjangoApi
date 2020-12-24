from django.urls import path
from .views import Post

app_name = 'ApiApp'
urlpatterns = [
    path('', Post.as_view(), name='list'),
]