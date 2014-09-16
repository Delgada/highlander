from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'highlander.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name = 'index' ),
    url(r'(?P<activity_url_name>\w+)/$',views.ActivityView.as_view(), name='activity'),
)
