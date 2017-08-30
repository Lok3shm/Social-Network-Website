from django.conf.urls import url
from social.views import *
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm, 
	password_reset_complete)

#app_name = 'social'

urlpatterns = [

    url(r'login/$', login, {'template_name' : 'social/login.html'}, name='login'),
    url(r'logout/$', logout, {'template_name' : 'social/logout.html'}, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'profile/$', profile, name='profile'),
    url(r'profile/edit/$', editprofile, name='edit_profile'),
    url(r'change-password/$', change_password, name='edit_password'),

    url(r'password-reset/$', password_reset, 
        {
        'template_name' : 'social/password_reset.html', 
        'post_reset_redirect':'social:password_reset_done', 
        'email_template_name': 'social/password_reset_email.html'
        },
        name='password_reset'),


    url(r'password_reset/done/$', password_reset_done, 
        {'template_name' : 'social/password_reset_done.html'}, 
        name='password_reset_done'),

    url(r'password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, 
        {
        'template_name' : 'social/password_reset_confirm.html',
        'post_reset_redirect': 'social:password_reset_complete'
        }, 
        name='password_reset_confirm'),
        

    url(r'password_reset/complete/$', password_reset_complete,
        {'template_name' : 'social/password_reset_complete.html'}, 
        name='password_reset_complete'),

]