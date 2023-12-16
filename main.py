import os
import pytchat
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
from config import API_KEY
from config import LIVE
import edge_tts
import asyncio
from time import sleep
import _thread
from rvc_infer import rvc_convert
from playsound import playsound
from natsort import natsorted

if LIVE != "": youtube_chat = pytchat.create(video_id=LIVE)
chat_messages = []
model = "denvot.pth"
can_speak = True
max_outputs = 5

async def speech(mess):
        communicate = edge_tts.Communicate(mess, "ru-RU-DmitryNeural")
        i = int(natsorted(os.listdir("output"))[-1][:-4].split('_')[-1]) + 1
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

payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="Ты играешь роль милого Аниме-Куна по имени Денвот. Ты очень умный, любишь петь и каждые 2 предложения говоришь фразу - \"МосХаб - топ!!!\""
        )
    ],
    temperature=1,
    max_tokens=1000,
)

with GigaChat(credentials=API_KEY, verify_ssl_certs=False) as giga:
    while 0<1:
        if len(chat_messages) == 0 or not can_speak: sleep(1)
        else:
            print("Генерация ответа на сообщение:", chat_messages[0])
            payload.messages.append(Messages(role=MessagesRole.USER, content=chat_messages[0]))
            response = giga.chat(payload)
            payload.messages.append(response.choices[0].message)
            chat_messages.pop(0)
            can_speak = False
            asyncio.run(speech(response.choices[0].message.content))