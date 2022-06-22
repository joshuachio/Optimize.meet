from tracemalloc import start
from flask import Flask, render_template, redirect, url_for, request
import asyncio
import os
import json
from datetime import datetime

# from Source import be_calendar, be_events, be_recurring, user_creation

activesessions = {}
timeout = 600
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/home/<username>", methods=["GET", "POST"])
def home(username):
    # if request.method == "POST":
    #     #Try to login with the email and password
    #     email = request.form["email"]
    #     password = request.form["password"]

    #     #If not valid, return to login page

    #     #If valid, display their daily page
    #     return render_template("daily.html")
    print(username)
    return render_template("error.html")

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
            recurring = be_recurring.Recurring(frequency, stopRepeat, 1, [])
        else:
            recurring = None

        #Creates the event object
        newEvent = be_events.Event(startTime, endTime, eventName, location, description, recurring)

        #Need to add the event to the user calendar


        return redirect(url_for('home'))
    return render_template("event.html")


@app.route('/user/', methods=['POST'])
def profile():
    if request.method == 'POST':
        #Needs to get the current logged in user session
        currUser = sesh.user
        return render_template("profile.html", username=currUser.username, email=currUser.email, phone=currUser.phoneNumber)
    return render_template("error.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        #Tries to create a login session with the username and password provided
        sesh = user_creation.Session(request.form['username'], request.form['password'])

        #If that account is not valid, then error
        if not sesh:
            errorstate = 1
            return

        #Active session with the login
        else:
            sesh.active = True
            activesessions[sesh] = sesh.userID
            return redirect(url_for('home'))
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
            calendar = be_calendar.Calendar()

            # #Create a new user object and add them to firebase storage
            newUser = user_creation.User(username, email, password, calendar, telephone)
            newUser.addToStorage()
            
            #Redirect to the login page
            return redirect(url_for('login'))
        except:
            #Some error occurred, return to register page again
            error = 'Invalid'
            return render_template('register.html', error)

    return render_template('register.html')