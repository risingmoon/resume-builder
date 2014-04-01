from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns(
    'resume_storage.views',
    url(
        r'^$',
        'front_view',
        name='index',
        ),
    url(
        r'^home/$',
        'home_view',
        name='home',
        ),
    url(
        r'^login/$',
        login,
        name='login',
        ),
    url(
        r'^logout/$',
        logout,
        name='logout',
        ),
    url(r'^resume/(\d+)/',
        'stub_view',
        name='resume'
        ),
)
