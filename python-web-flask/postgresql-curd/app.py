from flask import Flask
# from models import db
from flask import Flask, render_template
from flask import request
from flask import jsonify
from data_process import PostgreDbProcess
import json

app = Flask(__name__)
app.config['DEBUG'] = True

# index page
@app.route('/')
def index():
    return render_template('index.html')

# register
@app.route('/', methods=["POST"])
def register_user():
    # request from form
    data = {
        "table":"users",
        "columns": "id, name, email, birthday, register_time",
        "name":request.form.get('name'),
        "email":request.form.get('email'),
        "phone":request.form.get('phone'),
        "birthday":request.form.get('birthday'),
        "table": "users",
    }
    insert_data = PostgreDbProcess(data)
    insert_data.insert()
    return 'insert ok!'

@app.route('/delete/id/<user_id>', methods=["GET"])
def delete_user(user_id):
    if len(user_id) == 0:
        return 'you need to add user id!'
    data = {
        "table":"users",
        "columns": "id, name, email, birthday, register_time",
        "id":user_id
    }    
    del_data = PostgreDbProcess(data)
    del_data.delete_user()
    return 'delete ok' 

@app.route('/show/users/', methods=["GET"])
def show_users():
    users_rows = PostgreDbProcess.show_all_users()
    print(type(users_rows))
    return json.dumps(users_rows)

if __name__ == '__main__':
    app.run()