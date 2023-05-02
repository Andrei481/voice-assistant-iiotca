import time


from lib.voice_recognition.speech_recognition_module import VoiceRecognizer, Commands
from lib.voice_recognition.phrases import *
from api.spotify_client import SpotifyClient


def main():
    print("Andrei")
    voice = VoiceRecognizer()
    spotify = SpotifyClient()
    while True:
        voice.command = ""
        voice.recognize_speech()
        if voice.command == Commands.STOP:
            break
        elif voice.command == Commands.PLAY:
            song = str(voice.text).split(play_phrase)[1]
            song_uri = spotify.get_track_uri(song)
            spotify.play(song_uri)
        elif voice.command == Commands.PLAY_PLAYLIST:
            playlist = str(voice.text).split(play_playlist_phrase)[1].strip()
            print(f"|{playlist}|")
            playlist_id = spotify.get_playlist_id(playlist)
            # print(playlist_id)
            spotify.play_playlist(playlist_id)
        elif voice.command == Commands.PAUSE:
            spotify.pause()
        elif voice.command == Commands.RESUME:  # FIX THIS
            spotify.resume_playing()
        elif voice.command == Commands.PREVIOUS:
            spotify.previous_song()
        elif voice.command == Commands.NEXT:
            spotify.skip_song()
        elif voice.command == Commands.VOLUME_INCREASE:
            spotify.set_volume(True)
        elif voice.command == Commands.VOLUME_DECREASE:
            spotify.set_volume(False)


if __name__ == "__main__":
    main()
