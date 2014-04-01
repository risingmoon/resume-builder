from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns(
    'outline.views',
    url(
        r'^$',
        'stub_view',
        name='front',
        ),
    url(
        r'^home/$',
        'stub_view',
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
    url(
        r'^profile/$',
        'stub_view',
        name='profile',
        ),
    url(
        r'^new_section/$',
        'stub_view',
        name='new_section',
        ),
    url(
        r'^(\d+)/new_entry/$',
        'stub_view',
        name='new_entry',
        ),
    url(
        r'^(\d+)/new_data/$',
        'stub_view',
        name='new_data',
        ),
)
