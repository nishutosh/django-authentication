from django.conf.urls import url
from authprocess.views import *

urlpatterns=[
    url(r'^$',homepage,name="home"),
    url(r'^login/$',login,name="login"),
    url(r'^register',register,name="register"),
    url(r'logout/$',logout,name="logout")
    
]