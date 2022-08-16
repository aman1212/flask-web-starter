from flask import Flask
from db import mysql
from views.main_blueprint import main_blueprint

app = Flask(__name__)

#connect to the database
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

mysql.init_app(app)

app.register_blueprint(main_blueprint)
if(__name__ == "__main__"):
    app.run(debug=True)