from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Activity( models.Model ):
    name = models.CharField(max_length = 255, unique = True )
    creation_date = models.DateTimeField('date created')
    user_owner = models.ForeignKey(User)
    

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


    
