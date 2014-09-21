from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from core.models import Activity
from core.models import ActivityEntry

class IndexView( generic.ListView ):
    template_name = 'core/index.html'
    context_object_name = 'latest_activities'

    def get_queryset(self):
        
        self.activities =  Activity.objects.filter( creation_date__lte=timezone.now()
                                        ).order_by('-creation_date')[:5]
        return self.activities

class ActivityEntriesView( generic.ListView ):
    template_name = 'core/activity_entries.html'
    model = ActivityEntry

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(ActivityEntriesView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ActivityEntriesView, self).get_context_data(**kwargs)
        activity_pk = self.kwargs['pk']
        activity = get_object_or_404( Activity, pk = activity_pk )
        context['activity_name'] = activity.name
        entries = ActivityEntry.objects.filter( activity = activity )
        context['entries'] = entries
        context['activity_pk'] = activity_pk
        return context

class ActivityView( generic.DetailView ):
    template_name = 'core/activity.html'
    model = Activity

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(ActivityView, self).dispatch(request, *args, **kwargs)

class ActivityCreate( CreateView ):
    template_name = "core/activity_form.html"
    model = Activity
    success_url = reverse_lazy('core:index')
    fields = ['name','description']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(ActivityCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_owner = self.request.user
        form.instance.creation_date = timezone.now()
        return super(ActivityCreate, self).form_valid(form)
 
class ActivityEntryCreate( CreateView ):
    template_name = "core/activity_entry_form.html"
    model = ActivityEntry
    success_url = reverse_lazy('core:index')
    fields = ['activity','score']

    def form_valid(self, form ):
        
        form.instance.entry_date = timezone.now()
        form.instance.user = self.request.user

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(ActivityEntryCreate, self).dispatch(request, *args, **kwargs)



