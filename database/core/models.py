from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Activity( models.Model ):
    name = models.CharField(max_length = 255, unique = True )
    creation_date = models.DateTimeField('date created')
    user_owner = models.ForeignKey(User)
    url = models.CharField(max_length = 255 )

    class Meta:
        verbose_name_plural = "Activities"

    def __unicode__(self):
        return self.name

    
