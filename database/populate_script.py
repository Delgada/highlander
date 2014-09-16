##a script for quickly populating some data
import os
from datetime import datetime

def populate():
    
    def add_user( user, email, password ):
        u = User.objects.get_or_create( username = user, email = email, password = password )
        u[0].save()
        return u[0]

    def add_activity( name, creation_date, user_owner ):
        a = Activity.objects.get_or_create( name = name, 
                                          creation_date = creation_date,
                                          user_owner = user_owner)

    bart = add_user( 'bart', 'bart@simpsons.com', 'bart' )  
    add_activity('Catapulting', datetime.today().date(), bart )

    lisa = add_user( 'lisa', 'lisa@simpsons.com', 'lisa' )
    add_activity( 'Speed Mathematics', datetime.today().date(), lisa )

    homer = add_user( 'homer', 'homer@simpsons.com', 'homer' )
    add_activity( 'Yard of Ale', datetime.today().date(), homer )
  

# Start execution here!
if __name__ == '__main__':
    print "Starting Highlander population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'highlander.settings')
    #imports must go after environment variable has been set
    import django    
    django.setup()

    from core.models import Activity
    from django.contrib.auth.models import User
    
    populate()