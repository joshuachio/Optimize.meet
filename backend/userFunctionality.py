import smtplib
import requests
import pandas as pd
import datetime
import os
from twilio.rest import Client
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import oauth

#GSheets Boilerplate
def googlesheets():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = ('key.json')
    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    spreadsheetURL = 'URL'
    service = build('sheets', 'v4', credentials=creds)

#Twilio Script
def SMS(to):
    tw_sid = "AC72bd84375c2d0655f5378c4b8248bede"
    tw_auth = "22dd717dd96b2ae80d4a6123705383e4"
    twclient = Client(tw_sid,tw_auth)

    message = twclient.messages.create(
        to=to,
        from_="+13257328702",
        body ="Hello father")

    print(message.sid)

#login api :)
def login(query):
    users = []
    passwords = []
    loggedin = []
    query = query.split(" ")
    action = query[1]
    username = query[2]
    password = query[3]

    if action == "register":
        if username in users:
            return 2
        else:
            users.append(username)
            passwords.append(passwords)
            return 0
    if action == "login":
        if username in users:
            if password in passwords:
                if username not in loggedin:
                    loggedin.append(username)
                else:
                    return 1
            else:
                return 3
        else:
            return 4
    if action == "logout":
        if (username in loggedin & password in passwords):
            loggedin.remove(username)
            return 0
        elif (username in loggedin):
            return 3
        else:
            return 5
    return 6

def email(recipient):
    pass