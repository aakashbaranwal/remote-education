"""onlineclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 
from user import views as user_views
from user.views import user, students, teachers
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',user.profile,name="profile"),
    path('search/',user.search,name="search"),
    path('chat/', include('chat.urls', namespace ='chat')),
    path('report/', include('report.urls', namespace ='report')),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('accounts/',include('allauth.urls')),
    path('home/', user.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup')
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
