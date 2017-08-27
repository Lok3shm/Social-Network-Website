from django.conf.urls import url
from social.views import *
from django.contrib.auth.views import login, logout

app_name = 'social'

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'login/$', login, {'template_name' : 'social/login.html'}, name='login'),
    url(r'logout/$', logout, {'template_name' : 'social/logout.html'}, name='logout'),

]