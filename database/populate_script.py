##a script for quickly populating some data
import os
from datetime import datetime

def populate():
    from django.utils import timezone

    def add_user( user, email, password ):
        u = User.objects.get_or_create( username = user,
                                       defaults={'email':email, 'password': password } )
        up = UserProfile.objects.get_or_create( user = u[0] )
        return u[0]

    def add_activity( name, creation_date, user_owner ):
        a =  Activity.objects.get_or_create( name = name,
                                             defaults = { 'creation_date':creation_date, 'user_owner': user_owner} )
        return a

    def add_activity_entry( user, entry_date, score, activity ):
        ActivityEntry.objects.get_or_create( user = user,
                                             entry_date = entry_date,
                                             score = score, 
                                             activity = activity )
    filename = './100m_data.csv'
    creator = add_user( 'create','creator@gmail.com','creator' )
    activity = add_activity( '100m', timezone.now(), creator )[0]

    def read_csv( filename ):
        import csv, re
        numeric_const_pattern = "(?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )"
        rx = re.compile( numeric_const_pattern, re.VERBOSE )
        with open( filename, 'rb' ) as f:
            fcsv = csv.reader( f ) 
            fcsv.next() ## header
            for line in fcsv:
                first_name = line[2].split(' ')[0]
                last_name = line[2].split(' ')[-1]
                username = first_name + last_name
                runner = add_user( username, username + '@gmail.com', 'password' )
                entry_date =  timezone.make_aware( datetime( int( line[0] ),1,1 ), timezone.get_current_timezone())
                x = rx.findall( line[-1] )
                time = float(x[0] )
                #time = float( line[-1].split(' ')[0] )
                add_activity_entry( runner, entry_date, time, activity )
    print "Reading file %s" % filename
    read_csv( filename )

    filename = 'longjump_data.csv' 
    activity = add_activity( 'longjump', timezone.now(), creator )[0]
    print "Reading file %s" % filename
    read_csv( filename )


  

# Start execution here!
if __name__ == '__main__':
    print "Starting Highlander population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'highlander.settings')
    #imports must go after environment variable has been set
    import django    
    django.setup()

    from core.models import Activity, ActivityEntry
    from core.models import User, UserProfile
    
    populate()