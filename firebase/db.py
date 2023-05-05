import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "storageBucket": os.getenv("STORAGE_BUCKET")
}

firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
#user = auth.sign_in_with_email_and_password(os.getenv("FIREBASE_EMAIL"), os.getenv("FIREBASE_PWD"))
db = firebase.database()

test_song = "fresh"
test_artist = "domnul puya"
numerical_data = 6.9
try:
    data = {
        "topic": "Spotify",
        "title": test_song,
        "message": test_artist,
        "id": numerical_data
    }
    results = db.child("notificationRequests").push(data)
    db.update(data)
    print("Sent to Firebase")
except RuntimeError as error:
    print(error.args[0])