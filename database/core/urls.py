from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from core import views

urlpatterns = patterns('',
    
    url(r'^$', login_required( views.IndexView.as_view() ), name = 'index' ),
    url(r'^(?P<pk>\d+)/entries',login_required( views.ActivityEntriesView.as_view() ), name='activity_entries'),
    url(r'^(?P<pk>\d+)',login_required( views.ActivityView.as_view() ), name='activity'),
    url(r'^create/$',login_required( views.ActivityCreate.as_view() ), name='activity_create' ),
    url(r'^activity_entry_create/(?P<pk>\d+)/$', login_required( views.ActivityEntryCreate.as_view() ),
        name = 'activity_entry_create' ),
    url(r'^activity_entry_update/(?P<pk>\d+)/$', login_required( views.ActivityEntryUpdate.as_view() ),
        name = 'activity_entry_update' ),
    url(r'^activity_entry_delete/(?P<pk>\d+)/$', login_required( views.ActivityEntryDelete.as_view() ),
        name = 'activity_entry_delete' ),
    url(r'^activity_update/(?P<pk>\d+)/$', login_required( views.ActivityUpdate.as_view() ), name = 'activity_update' ),
    url(r'^activity_delete/(?P<pk>\d+)/$', login_required( views.ActivityDelete.as_view() ), name = 'activity_delete' ),
)
