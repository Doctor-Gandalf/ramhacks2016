from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import UserCreationForm


from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', login, name='login',
        kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, name='logout',
        kwargs={'template_name': 'accounts/logout.html'}),
    url('^register/', CreateView.as_view(
        template_name='accounts/register.html',
        form_class=UserCreationForm,
        success_url='/adventure/home'),
        name='register'),
]