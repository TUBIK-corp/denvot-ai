import denvot_ai
import os
from time import sleep
from playsound import playsound

while 0<1: 
    if denvot_ai.can_speak:
        audio_path = os.getcwd().replace('\\', '/') + '/output/' + denvot_ai.send_message(input())
        while not os.path.exists(audio_path): sleep(1)
        playsound(audio_path)