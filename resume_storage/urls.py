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
    url(r'^resume/new/$',
        'create_resume',
        name='create_resume',
        ),
    url(r'^resume/(\d+)/$',
        'resume_view',
        name='resume_view',
        ),
    url(r'^resume/(\d+)/delete/$',
        'delete_resume',
        name='delete_resume',
        ),
    url(r'^resume/(\d+)/delete/real/$',
        'real_delete',
        name='real_delete',
        ),
)
