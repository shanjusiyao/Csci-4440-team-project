from flask import Flask, render_template, redirect, request, Response, jsonify, abort
from models import *
from functools import wraps
import json



app = Flask(__name__, static_folder='static', static_url_path="")
create_table()

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

loginState = False
user = ""

def login_required(func):
    @wraps(func)
    def function(*args, **kwargs):
        global loginState
        if not loginState:
            return redirect('/login')
        return func(*args, **kwargs)
    return function

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        try:
            passwd = get_user_password(username)
            print(password)
            print(passwd)
            if (passwd != password):
                return abort(401)
        except Exception:
             return Response("You fail")
        global loginState
        global user
        loginState = True
        user = username
        return redirect('/')

@app.route('/addteam', methods=['POST'])
def addteam():
    teamData = json.loads(request.data)
    insert_new_team(teamData['name'], teamData['public'], teamData['tags'])
    return jsonify(
        {
            "result": "200 OK"
        }
    )


@app.route('/deleteTeam', methods=['POST'])
def deleteT():
    teamName = json.loads(request.data)['name']
    delete_team(teamName)
    return jsonify(
        {
            "result": "200 OK"
        }
    )

@app.route('/addTeam', methods=['POST'])
def addT():
    teamid = json.loads(request.data)['teamid']
    add_team(teamid, user)
    return jsonify(
        {
            "result": "200 OK"
        }
    )

@app.route('/ms', methods=['POST'])
def ms():
    teamid, tags = json.loads(request.data)['teamid'], json.loads(request.data)['tags']
    modify_student(teamid, tags)
    return jsonify(
        {
            "result": "200 OK"
        }
    )
@app.route('/mt', methods=['POST'])
def mt():
    teamid, tags = json.loads(request.data)['teamid'], json.loads(request.data)['tags']
    modify_team(teamid, tags)
    return jsonify(
        {
            "result": "200 OK"
        }
    )

@app.route('/leaveTeam', methods=['POST'])
def leaveT():
    leave_team(user)
    return jsonify(
        {
            "result": "200 OK"
        }
    )

@app.route('/getStudentTeam', methods=['GET'])
def getStudentTeam():
    data = select_all_team_students()
    roleMap = {}
    teamMap = {}
    for obj in data:
        roleMap[obj[3]] = obj[1]
    print(roleMap)
    students = select_all_user()
    for stu in students:
        if not roleMap.get(stu[0], None):
            teamMap[stu[0]] = ""
        else:
            teamMap[stu[0]] = roleMap[stu[0]]
    print(teamMap)
    return jsonify(
        teamMap
    )

@app.route('/getTeam', methods=['GET', 'POST'])
def getTeam():
    if request.data == b'':
        print("allteam")
        teamData = select_all_team()
        return jsonify(teamData)
    elif json.loads(request.data).get('me', None):
        teamData = filter_by_me(user)
        return jsonify(teamData)
    elif json.loads(request.data).get('search', None):
        teamData = filter_name(json.loads(request.data)['val'])
        return jsonify(teamData)
    else:
        teamData = filter_tag(json.loads(request.data)['tag'])
        return jsonify(teamData)

# @app.route('/add_team_tag', methods=['POST'])
# def change_team_tag():
#     pass

@app.route('/', methods=['GET'])
@login_required
def homepage():
    return render_template('index.html')    


@app.route('/team', methods=['GET'])
@login_required
def team():
    return render_template('team.html')

@app.route('/assignment', methods=['GET'])
@login_required
def assignment():
    return "Not Implemented"

@app.route('/course', methods=['GET'])
@login_required
def course():
    return "Not Implemented"

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    global loginState
    global user
    loginState = False
    user = ""
    return redirect('/login')

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
