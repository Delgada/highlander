from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'highlander.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name = 'index' ),
    url(r'^(?P<pk>\d+)/entries',views.ActivityEntriesView.as_view(), name='activity_entries'),
    url(r'^(?P<pk>\d+)',views.ActivityView.as_view(), name='activity'),
    url(r'^create',views.ActivityCreate.as_view(), name='activity_create' ),
    url(r'^activity_entry_create/(?P<pk>\d+)', views.ActivityEntryCreate.as_view(), name = 'activity_entry_create' ),
)
