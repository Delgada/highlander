from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from registration.signals import user_registered

# Create your models here.
class Activity( models.Model ):
    name = models.CharField(max_length = 255, unique = True )
    creation_date = models.DateTimeField('date created')
    user_owner = models.ForeignKey(User)
    description = models.CharField(max_length = 2000 )

    class Meta:
        verbose_name_plural = "Activities"

    def __unicode__(self):
        return self.name


class ActivityEntry( models.Model ):
    activity = models.ForeignKey( Activity )
    user = models.ForeignKey( User )
    entry_date = models.DateTimeField('entry date' )
    score = models.DecimalField( name = 'score', max_digits = 15, decimal_places = 8, default = 0 )

    def __unicode__(self):
        return 'Activity Entry %s' % self.activity.name

#user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    bio = models.TextField(null=True)

    def __unicode__(self):
        return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)

#class UserProfile(models.Model):
#    user = models.OneToOneField( User )
#    url = models.URLField()
 
#    def __unicode__(self):
#        return self.user
 
#def user_registered_callback(sender, user, request, **kwargs):
#    profile = UserProfile(user = user)
#    profile.url = request.POST["url"]
#    profile.save()
 
#user_registered.connect(user_registered_callback)