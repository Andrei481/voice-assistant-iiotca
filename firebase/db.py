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
db = firebase.database()


def send_status(status):
    data = {
        "status": status
    }
    results = db.child("statuss").push(data)
    db.update(data)
    print("Sent to Firebase")

def send_to_firebase(song, artist, album):
    # try:
    data = {
        "topic": "Spotify",
        "title": "Spotify playing...",
        "message": "Song: " + song + "\nArtist: " + artist + "\nAlbum: " + album,
        "song": song,
        "artist": artist,
        "album": album
    }
    results = db.child("notificationRequests").push(data)
    db.update(data)
    print("Sent to Firebase")
    # except RuntimeError as error:
    #     print(error.args[0])

