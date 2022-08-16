from flask import session,redirect
from datetime import datetime,timezone,timedelta

def timecheck():
    if 'login' in session:
       if session['login']:
          if(session['time'].replace(tzinfo=timezone.utc) < datetime.now().replace(tzinfo=timezone.utc)):
            return False
          else:
           session['time'] = datetime.now() + timedelta(hours=1)
           return True
       else:
        return False
    else:
     return False