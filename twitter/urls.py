from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^twitter/$', 'twitter.views.hello', name='hello'),
    url(r'^twitter/login/$', 'twitter.views.login', name='post'),
    url(r'^twitter/hello/$', 'twitter.views.newhello', name='helloagain'),
     url(r'^twitter/post/$', 'twitter.views.post', name='post'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
