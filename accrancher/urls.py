from django.conf.urls import url
from . import views

from django.contrib.auth.views import auth_login, auth_logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, auth_login
app_name = 'accrancher'

urlpatterns = [

    url(r'^$', views.scrap, name='index'),
    #url(r'^login/$', views.login, {'template_name':'login.html'}),
    #url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #url(r'^login/$',LoginView.as_view(template_name='login.html')),
    url(r'^login/$',views.loginPage,name='login'),
    url(r'^logout/$',views.logutuser,name='logout'),
    url(r'^signup/$',views.register,name='register'),
    #url(r'^(?P<slug>[-\w]+)/$',views.profile,name='profile'),
    url(r'^(?P<slug>[-\w]+)/change_password$', views.change_password, name='change_password'),
    url(r'^(?P<slug>[-\w]+)/edit$',views.edit_profile,name='edit_profile'),
    url(r'^allusers/$', views.stack_detail, name='name'),
]















