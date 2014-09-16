##a script for quickly populating some data
import os
from datetime import datetime

def populate():
    
    def add_user( user, email, password ):
        u = User.objects.get_or_create( username = user, email = email, password = password )
        u[0].save()
        return u[0]

    def add_activity( name, creation_date, user_owner ):
       return   Activity.objects.get_or_create( name = name, 
                                          creation_date = creation_date,
                                          user_owner = user_owner)
    def add_activity_entry( user, entry_date, score, activity ):
        return  ActivityEntry.objects.get_or_create( user = user,
                                                     entry_date = entry_date,
                                                     score = score, 
                                                     activity = activity )
                   
    bart = add_user( 'bart', 'bart@simpsons.com', 'bart' )  
    a1 = add_activity('Catapulting', datetime.today().date(), bart )[0]

    lisa = add_user( 'lisa', 'lisa@simpsons.com', 'lisa' )
    a2 = add_activity( 'Speed Mathematics', datetime.today().date(), lisa )[0]

    homer = add_user( 'homer', 'homer@simpsons.com', 'homer' )
    a3 = add_activity( 'Yard of Ale', datetime.today().date(), homer )[0]

    today = datetime.today().date()
    activity_entries = [ ( bart, today, 10.0, a1 ),
                          ( bart, today, 10.0, a2 ),
                          ( bart, today, 10.0, a3 ),
                          ( lisa, today, 11.0, a1 ),
                          ( lisa, today, 11.0, a2 ),
                          ( lisa, today, 11.0, a3 ),
                          ( homer, today, 1.0, a1 ),
                          ( homer, today, 1.0, a2 ),
                          ( homer, today, 100.0, a3 )
                          ]
    for ae in activity_entries:
        add_activity_entry( ae[0], ae[1], ae[2], ae[3] )
  

# Start execution here!
if __name__ == '__main__':
    print "Starting Highlander population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'highlander.settings')
    #imports must go after environment variable has been set
    import django    
    django.setup()

    from core.models import Activity, ActivityEntry
    from django.contrib.auth.models import User
    
    populate()