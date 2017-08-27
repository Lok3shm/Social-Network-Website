from django.conf.urls import url
from social.views import *
from django.contrib.auth.views import login, logout

app_name = 'social'

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'login/$', login, {'template_name' : 'social/login.html'}, name='login'),
    url(r'logout/$', logout, {'template_name' : 'social/logout.html'}, name='logout'),
    url(r'register/$', register, name='register'),
    url(r'profile/$', profile, name='profile'),
    url(r'profile/edit/$', editprofile, name='edit_profile'),
    url(r'edit-password/$', change_password, name='edit_password'),

]