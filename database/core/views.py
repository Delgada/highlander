from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.forms.models import modelform_factory
from django.http import HttpResponseRedirect

from core.models import Activity
from core.models import ActivityEntry
from core.models import UserProfile
from core.forms import UserProfileForm

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect( reverse('core:index' ) )
    else:
        return HttpResponseRedirect( reverse('auth_login' ) ) 

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

class ActivityCreate( CreateView ):
    template_name = "core/activity_form.html"
    model = Activity
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user_owner = self.request.user
        form.instance.creation_date = timezone.now()
        return super(ActivityCreate, self).form_valid(form)

class ActivityUpdate( UpdateView ):
    template_name = "core/activity_form.html"
    model = Activity
    success_url = reverse_lazy('core:index')

class ActivityDelete( DeleteView ):
    model = Activity
    success_url = reverse_lazy('core:index')

class ActivityEntryCreate( CreateView ):
    template_name = "core/activity_entry_form.html"
    model = ActivityEntry
    success_url = reverse_lazy('core:index')
    fields = ['activity','score']

    def form_valid(self, form ):
        
        form.instance.entry_date = timezone.now()
        form.instance.user = self.request.user
        return super(ActivityEntryCreate, self ).form_valid(form)

class ActivityEntryUpdate( UpdateView ):
    template_name = "core/activity_entry_form.html"
    model = ActivityEntry
    success_url = reverse_lazy('core:index')
    fields = ['activity','score']

class ActivityEntryDelete( DeleteView ):
    model = ActivityEntry
    success_url = reverse_lazy('core:index')

class UserProfileDetailView( generic.DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

from core.forms import UserProfileEditForm

class UserProfileEditView(UpdateView):
    form_class = UserProfileEditForm
    template_name = "edit_profile.html"

    def get_initial( self ):
        initial = super(UserProfileEditView, self).get_initial()
        initial["bio"] = self.get_object().bio
        initial["first_name"] = self.get_object().first_name
        initial["last_name"] = self.get_object().last_name
        initial["url"] = self.get_object().url
        initial["location"] = self.get_object().location
        return initial

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug': self.request.user})
