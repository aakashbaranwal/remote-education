from django.urls import path, re_path
from . import views as report_views
from django.conf.urls import url
app_name = 'report'


urlpatterns = [
    path('', report_views.sheet, name='sheet'),
    
]