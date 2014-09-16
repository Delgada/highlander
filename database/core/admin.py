from django.contrib import admin
from core.models import Activity
from django.contrib.auth.models import User
# Register your models here.


#class UserInline( admin.TabularInline ):
#    model = User
#    extra = 3

class ActivityAdmin( admin.ModelAdmin ):
    fieldsets = [
                 (None, {'fields':['name','url','user_owner']}),
                 ('Date Information', {'fields':['creation_date']}),
                 ]
    list_display = ('name', 'user_owner', 'creation_date' )
    list_filter = ['creation_date']
    search_fields = ['name']
    #inlines = [UserInline]

admin.site.register( Activity, ActivityAdmin )


