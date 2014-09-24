from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic.simple import direct_to_template
#from core.forms import UserProfileForm
from registration.backends.simple.views import RegistrationView
from core.views import UserProfileDetailView
from django.contrib.auth.decorators import login_required as auth
from core.views import UserProfileEditView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'highlander.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','core.views.home', name = 'home' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activities/',include('core.urls', namespace = 'core')),
    #url(r'accounts/register/$', 
    #    RegistrationView.as_view(form_class = UserProfileForm), 
    #    name = 'registration_register'),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    #url(r'^$', direct_to_template, 
    #        { 'template': 'index.html' }, 'index'),
)
        