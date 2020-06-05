
from django.urls import path, re_path
from . import views as chat_views
from django.conf.urls import url
app_name = 'chat'


urlpatterns = [
    path('', chat_views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', chat_views.room, name='room'),
]
