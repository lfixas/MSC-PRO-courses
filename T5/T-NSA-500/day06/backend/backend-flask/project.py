from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("backend")

# Configuration of the database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<user>:<password>@<hostname>/<db_name>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

#for create table
'''with app.app_context():
    db.create_all()'''

@app.route("/")
def hello_nsapoold06():
    return "<p>Welcome to nsapoold06</p>"

@app.route("/api/user")
def status_api():
    users = User.query.all()
    list_users = []
    for user in users:
        user_dict = {
            'id': user.id,
            'name': user.name,
        }
        list_users.append(user_dict)
    return jsonify({'users': list_users})