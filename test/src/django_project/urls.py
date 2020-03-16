"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import urls as ur
from django_project import views
from accounts import views as vi
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from .views import Home
app_mname='django_project'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index.html'),
    url(r'^about/$',views.about,name='about.html'),
    url(r'^courses/$',views.courses,name='courses.html'),
    url(r'^teacher/$',views.teacher,name='teacher.html'),
    url(r'^blog/$',views.blog,name='blog.html'),
    url(r'^contact/$',views.contact,name='contact.html'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', vi.RegisterView.as_view(), name='register'),

    #path('', Home.as_view(), name='home'),
    path('about/', TemplateView.as_view(
        template_name='about_us.html'
    ), name='about_us'),

    path('personality/', include('personality.urls')),
    path('', include('accounts.urls')),
]
