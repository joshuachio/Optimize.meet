from tracemalloc import start
from flask import Flask, render_template, redirect, url_for, request, session, g
import asyncio
import os
import json
from datetime import datetime
# import sys
# sys.path.append('../Calendar')
from ..Source.be_calendar import Calendar
from ..Source.be_events import Event
from ..Source.be_recurring import Recurring
from ..Source.be_tasks import Task
from ..Source.user_creation import User, Session

activesessions = {}
timeout = 600
app = Flask(__name__)

app.secret_key = 'super secret key'

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = Session(session['user_id'][0], session['user_id'][1])
        g.user = user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=["GET"])
def home():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('homepage.html')

@app.route("/event", methods=['POST', 'GET'])
def event():
    if request.method == 'POST':
        #Gets data from the submitted form
        eventName = request.form['name']
        startTime = datetime.strptime(request.form['start-time'], "%Y-%m-%dT%H:%M")
        endTime = datetime.strptime(request.form['end-time'], "%Y-%m-%dT%H:%M")
        location = request.form['location']
        description = request.form['description']

        #Creates a recurring object if needed
        if request.form['recurring'] and request.form['stop-time']:
            frequency = request.form['recurring']
            stopRepeat = datetime.strptime(request.form['stop-time'], "%Y-%m-%dT%H:%M")
            recurring = Recurring(frequency, stopRepeat, 1, [])
        else:
            recurring = None

        #Creates the event object
        newEvent = Event(startTime, endTime, eventName, location, description, recurring)
        print(newEvent.event_name)
        #Need to add the event to the user calendar
        g.user.user.calendar.addEvent(newEvent)
        print("success")

        return redirect(url_for('home'))
    return render_template("event.html")
    
@app.route("/task", methods=['POST', 'GET'])
def task():
    if request.method == 'POST':
        #Gets data from the submitted form
        taskName = request.form['name']
        dueDate = datetime.strptime(request.form['due-date'], "%Y-%m-%dT%H:%M")
        description = request.form['description']

        #Creates the task object
        newTask = Task(taskName, dueDate, description)

        #Need to add the task to the user calendar
        g.user.user.calendar.addTask(newTask)
        print("success")

        return redirect(url_for('home'))
    return render_template("task.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        session.pop('user_id', None)
        # Tries to create a login session with the username and password provided
        try:
            sesh = Session(request.form['email'], request.form['password'])
            print(request.form['email'])

            activesessions[sesh] = sesh.userID
            if sesh.active:
                session['user_id'] = (sesh.user.email, sesh.user.password)
                return redirect(url_for('home'))

        # If that account is not valid, then error
        except:
            errorstate = 1
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    return render_template('login.html', error=error)

@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        try:
            #Get email and password from the form
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            telephone = request.form['phone']

            # Create empty calendar
            calendar = Calendar()

            # #Create a new user object and add them to firebase storage
            newUser = User(username, email, password, calendar, telephone)
            newUser.addToStorage()
            
            #Redirect to the login page
            return redirect(url_for('login'))
        except:
            #Some error occurred, return to register page again
            error = 'Invalid Credentials'
            return render_template('register.html', error=error)

    return render_template('register.html')