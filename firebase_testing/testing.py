from Pyrebase4 import pyrebase

config = {
    "apiKey": "AIzaSyAz5bLpUWAOBouA8Q9_WeloGYDdI1Q9s5g",
    "authDomain": "calendar-be058.firebaseapp.com",
    "databaseURL": "https://calendar-be058-default-rtdb.firebaseio.com",
    "projectId": "calendar-be058",
    "storageBucket": "calendar-be058.appspot.com",
    "messagingSenderId": "765432044481",
    "appId": "1:765432044481:web:7dceaf5af57e8374572d40",
    "measurementId": "G-9Q457P91BV"
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = "email@gamil.com"
password = "password"

user = auth.create_user_with_email_and_password(email, password)
print("User created")