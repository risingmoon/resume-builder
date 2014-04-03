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
        'profile',
        name='profile',
        ),
    url(
        r'^section/(\d+)/$',
        'section',
        name='section',
        ),
    url(
        r'^edit/$',
        'stub_view',
        name='edit',
        ),
)
