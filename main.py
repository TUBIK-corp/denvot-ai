import os
import pytchat
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import API_KEY
from config import LIVE
import edge_tts
import asyncio
from time import sleep
import _thread
from rvc_infer import rvc_convert
from playsound import playsound
from natsort import natsorted

giga = GigaChat(credentials=API_KEY, verify_ssl_certs=False, model="GigaChat-Pro")
if LIVE != "": youtube_chat = pytchat.create(video_id=LIVE)
chat_messages = []
can_speak = True

model = "denvot.pth"
prompt = "Ты играешь роль милого Аниме-Куна по имени Денвот, тебя также иногда называют Пупс. Ты очень умный, любишь петь и говорить фразу - \"МосХаб - топ!!!\""
max_outputs = 5

if not os.path.exists('input'): os.mkdir('input')
if not os.path.exists('output'): os.mkdir('output')

async def speech(mess):
        communicate = edge_tts.Communicate(mess, "ru-RU-DmitryNeural")
        if len(os.listdir("output")) == 0: i = 0
        else: i = int(natsorted(os.listdir("output"))[-1][:-4].split('_')[-1]) + 1
        file_name = "test_" + str(i) + ".wav"
        if len(os.listdir("output")) >= max_outputs: os.remove("output\\" + natsorted(os.listdir("output"))[0])
        await communicate.save("input\\" + file_name)
        rvc_convert(model_path="models\\" + model, 
                    input_path="input\\" + file_name,
                    f0_up_key=8)
        os.rename("output\\out.wav", "output\\" + file_name)
        os.remove("input\\" + file_name)
        print("DenVot: " + file_name)
        playsound(os.getcwd().replace('\\', '/') + '/output/' + file_name)
        global can_speak
        can_speak = True
        
def chat():
    if LIVE != "":
        while youtube_chat.is_alive():
            sleep(1)
            for c in chat.get().sync_items():
                chat_messages.append(f"{c.author.name}: {c.message}")
                print("Новые сообщения:", chat_messages)
    else: 
        while 0<1: chat_messages.append(input())
_thread.start_new_thread(chat, ())

print("DenVot-AI успешно запущен")

messages = [SystemMessage(content=prompt)]

while 0<1:
    if len(chat_messages) == 0 or not can_speak: sleep(1)
    else:
        print("Генерация ответа на сообщение:", chat_messages[0])
        messages.append(HumanMessage(content=chat_messages.pop(0)))
        res = giga(messages)
        messages.append(res)
        can_speak = False
        asyncio.run(speech(res.content))
