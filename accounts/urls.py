from django.conf.urls import url
from django.contrib.auth.views import login, logout


from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', login, name='login',
        kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, name='logout',
        kwargs={'template_name': 'accounts/logout.html'}),
]