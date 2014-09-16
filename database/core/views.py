from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404

from core.models import Activity
from core.models import ActivityEntry

# Create your views here.
def decode_url(category_name_url):
    return category_name_url.replace('_', ' ')

def encode_url(category_name):
    return category_name.replace(' ', '_' )

class IndexView( generic.ListView ):
    template_name = 'core/index.html'
    context_object_name = 'latest_activities'

    def get_queryset(self):
        
        self.activities =  Activity.objects.filter( creation_date__lte=timezone.now()
                                        ).order_by('-creation_date')[:5]

        for activity in self.activities:
            activity.url = encode_url(activity.name)
        return self.activities

class ActivityEntriesView( generic.ListView ):
    template_name = 'core/activity_entries.html'
    model = ActivityEntry

    def get_context_data(self, **kwargs):
        context = super(ActivityEntriesView, self).get_context_data(**kwargs)
        activity_url_name = self.kwargs['activity_url_name']
        activity_name = decode_url( activity_url_name )
        context['activity_name'] = activity_name
        activity = get_object_or_404( Activity, name = activity_name )
        entries = ActivityEntry.objects.filter( activity = activity )
        context['entries'] = entries
        context['activity_url_name'] = activity_url_name
        return context
    #    self.activities = ActivityEntry.objects.filter( 



class ActivityView( generic.DetailView ):
    template_name = 'core/activity.html'
    model = Activity

    def get_object(self):
        name = decode_url(self.kwargs['activity_url_name'])
        return get_object_or_404(Activity, name = name )
    #slug_field = 'name'
    #slug_url_kwarg = 'activity_url_name'

    #def get_context_data(self, **kwargs):
    #    name = decode_url(self.kwargs['activity_url_name'])
    #    activity = get_object_or_404( Activity, name = name )
    #    context = super(ActivityView, self).get_context_data(**kwargs)
    #    context['name'] = name
    #    context['user_owner'] = activity.user_owner
    #    context['creation_date'] = activity.creation_date
    #    return context
        




