from django.conf.urls import url

from . import views

app_name = 'adventure'
urlpatterns = [
    url(r'^login/?$', views.login, name="login"),
    url(r'^do_login/?$', views.do_login, name="do_login"),
]