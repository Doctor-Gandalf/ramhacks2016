from django.conf.urls import url

from . import views

app_name = 'adventure'
urlpatterns = [
    url(r'^login/?$', views.login, name="login")
]