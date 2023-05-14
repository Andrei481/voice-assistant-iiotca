import time

from lib.voice_recognition.speech_recognition_module import VoiceRecognizer, Commands
from lib.voice_recognition.phrases import *
from api.spotify_client import SpotifyClient
from gtts import gTTS
from firebase.db import send_to_firebase
import os


def main():
    print("Listening...")
    voice = VoiceRecognizer()
    spotify = SpotifyClient()
    voice_text = "Nuamînțeles, vărog repetați"
    language = 'ro'
    speech = gTTS(text=voice_text, lang=language, slow=False)
    speech.save("hello.mp3")
    # spotify.print_devices()
    while True:
        voice.command = ""
        voice.recognize_speech()
        if voice.command == Commands.EXIT:
            break
        elif voice.command == Commands.PLAY:
            song = str(voice.text).split(play_phrase)[1]
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
        elif voice.command == Commands.UNKNOWN:
            os.system("vlc hello.mp3")


if __name__ == "__main__":
    main()
