import asyncio
from tracemalloc import start
from flask import Flask, render_template, redirect, url_for, request
import asyncio
import os
import json
from datetime import datetime
from ..backend import be_events

activesessions = {}
timeout = 600
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("daily.html")

@app.route("/event", methods=['POST', 'GET'])
def event():
    if request.method == 'POST':
        eventName = request.form['name']
        startTime = datetime.strptime(request.form['start-time'], "%Y-%m-%dT%H:%M")
        endTime = datetime.strptime(request.form['end-time'], "%Y-%m-%dT%H:%M")
        location = request.form['location']
        description = request.form['description']
        newEvent = be_events.Event(startTime, endTime, eventName, location, description)
        print(newEvent)
        frequency = request.form['recurring']
        if request.form['stop-time']:
            stopRepeat = datetime.strptime(request.form['stop-time'], "%Y-%m-%dT%H:%M")


        print(request.form['name'])
        return redirect(url_for('home'))
    return render_template("event.html")


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid'
        else:
            sesh = user_creation.Session(request.form['username'], request.form['password'])
            if not sesh:
                errorstate = 1
                return
            else:
                sesh.active = True
                activesessions[sesh] = sesh.userID
                return redirect(url_for('calendar'))
    return render_template('login.html', error=error)