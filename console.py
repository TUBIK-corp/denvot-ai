import denvot_ai
import os
from time import sleep
from playsound import playsound

while 0<1: 
    audio_path = os.getcwd().replace('\\', '/') + '/output/' + denvot_ai.send_message(input())
    playsound(audio_path)