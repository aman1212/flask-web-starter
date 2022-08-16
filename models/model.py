from db import mysql
import json
# user Class
class User:
    id = ''
    email = ''
    fullname = ''
    password = ''
    stat = ''
    type = ''

    def __init__(self, user_id=None):
        if user_id is None:
         self.new_user = True
        else:
          self.new_user = False
          self.id = user_id
          #fetch all records from db about user_id
          self._populateUser() 

    def commit(self):
        if self.new_user:
            #Do INSERTs
            pass
        else:
            #Do UPDATEs
            pass
    def delete(self):
        if self.new_user == False:
            return False
        #Delete user code here
    def _populate(self):
        #Query self.user_id from database and
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM user WHERE id = %s', (self.id))
        # Fetch one record and return result
        account = cursor.fetchone()
        self.email = account[5]
        self.fullname = account[1]
        self.password = account[2]
        self.stat = account[3]
        self.type = account[4]
    def getFullName(self):
        return self.name
    def aut(self):
        # Check if account exists using MySQL
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (self.email, self.password))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            self.id = account[0]
            self._populate()
            return True
        else:
            # Account doesnt exist or username/password incorrect
            return False
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# user user class end
    
    