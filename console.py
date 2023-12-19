import denvot_ai
import librosa
import _thread
from time import sleep
from playsound import playsound

audio_paths = []

def playlist():
    while 0<1:
        if len(audio_paths) > 0:
            audio = audio_paths[0]
            print(audio_paths.pop(0), librosa.get_duration(filename=audio))
            playsound(audio)
            sleep(librosa.get_duration(filename=audio))
        else: sleep(1)
_thread.start_new_thread(playlist, ())

while 0<1: 
    audio_paths.append(denvot_ai.send(input()))