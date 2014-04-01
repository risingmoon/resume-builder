from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns(
    'outline.views',
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
    url(
        r'^profile/$',
        'stub_view',
        name='profile',
        ),
    url(
        r'^edit/$',
        'stub_view',
        name='edit',
        ),
)
