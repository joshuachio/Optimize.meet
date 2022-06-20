import asyncio
from flask import Flask, render_template, redirect, url_for, request
import asyncio
import os
import json

activesessions = {}
timeout = 600
app = Flask(__name__)

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

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
            return redirect(url_for('calendar'))
    return render_template('login.html', error=error)