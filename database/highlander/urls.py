from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from core.views import UserProfileDetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from core.views import UserProfileEditView
from core.models import UserProfile
from core.forms import UserProfileForm
from core import views

urlpatterns = patterns('',
    url(r'^$','core.views.home', name = 'home' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activities/',include('core.urls', namespace = 'core')),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
    url(r'^edit_profile/$', login_required(UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class = UserProfileForm ) , name = 'registration_register'),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'registration/logout.html', 'next_page':'home'}, name='auth_logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
        