from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'highlander.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^activities/',include('core.urls', namespace = 'core')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^$', direct_to_template, 
    #        { 'template': 'index.html' }, 'index'),
)
