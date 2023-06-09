print("Importing time...")
import time
#from pydub import AudioSegment
#from pydub.playback import play
print("Importing VoiceRecognizer...")
from lib.voice_recognition.speech_recognition_module import VoiceRecognizer, Commands
from lib.voice_recognition.phrases import *
print("Importing SpotifyClient...")
from api.spotify_client import SpotifyClient
#from gtts import gTTS
print("Importing Firebase...")
from firebase.db import send_to_firebase
from firebase.db import send_status
print("Importing OS...")
import os


def main():
    print("Initializing VoiceRecognizer...")
    voice = VoiceRecognizer()
    print("Initializing SpotifyClient...")
    spotify = SpotifyClient()
    while True:
        voice.command = ""
        print("Listening...")
        voice.recognize_speech()
        send_status(voice.text)
        if voice.command == Commands.EXIT:
            break
        elif voice.command == Commands.PLAY:
            song = str(voice.text).split(play_phrase[0])[1]
            song_uri = spotify.get_track_uri(song)
            spotify.play(song_uri)
            current_track_info = spotify.get_current_track_info()
            send_to_firebase(current_track_info['song'], current_track_info['artist'], current_track_info['album'])
        elif voice.command == Commands.PLAY_PLAYLIST_0:
            playlist = str(voice.text).split(play_playlist_phrase[0])[1].strip()
            print(f"Playing playlist: {playlist}")
            playlist_id = spotify.get_playlist_id(playlist)
            spotify.play_playlist(playlist_id)
            current_track_info = spotify.get_current_track_info()
            send_to_firebase(current_track_info['song'], current_track_info['artist'], current_track_info['album'])
        elif voice.command == Commands.PLAY_PLAYLIST_1:
            playlist = str(voice.text).split(play_playlist_phrase[1])[1].strip()
            print(f"Playing playlist: {playlist}")
            playlist_id = spotify.get_playlist_id(playlist)
            spotify.play_playlist(playlist_id)
            current_track_info = spotify.get_current_track_info()
            send_to_firebase(current_track_info['song'], current_track_info['artist'], current_track_info['album'])
        elif voice.command == Commands.PLAY_PLAYLIST_2:
            playlist = str(voice.text).split(play_playlist_phrase[2])[1].strip()
            print(f"Playing playlist: {playlist}")
            playlist_id = spotify.get_playlist_id(playlist)
            spotify.play_playlist(playlist_id)
            current_track_info = spotify.get_current_track_info()
            send_to_firebase(current_track_info['song'], current_track_info['artist'], current_track_info['album'])
        elif voice.command == Commands.PAUSE:
            spotify.pause()
        elif voice.command == Commands.RESUME:
            spotify.resume_playing()
        elif voice.command == Commands.PREVIOUS:
            spotify.previous_song()
            current_track_info = spotify.get_current_track_info()
            send_to_firebase(current_track_info['song'], current_track_info['artist'], current_track_info['album'])
        elif voice.command == Commands.NEXT:
            spotify.skip_song()
            current_track_info = spotify.get_current_track_info()
            send_to_firebase(current_track_info['song'], current_track_info['artist'], current_track_info['album'])
        elif voice.command == Commands.VOLUME_INCREASE:  # DOESN'T WORK ON MOBILE
            spotify.set_volume(True)
        elif voice.command == Commands.VOLUME_DECREASE:  # DOESN'T WORK ON MOBILE
            spotify.set_volume(False)
        #elif voice.command == Commands.UNKNOWN:
            #play(AudioSegment.from_mp3("hello.mp3"))
        

if __name__ == "__main__":
    main()
