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
import ffmpeg

chat = pytchat.create(video_id=LIVE)
chat_messages = []
model = "denvot.pth"
can_speak = True

async def speech(mess):
        communicate = edge_tts.Communicate(mess, "ru-RU-DmitryNeural")
        i = 0
        file_name = "test"
        while file_name == "test":
            if "test_" + str(i) + ".wav" not in os.listdir("output"): file_name = "test_" + str(i) + ".wav"
            i += 1
        await communicate.save("input\\" + file_name)
        output_path = rvc_convert(model_path="models\\" + model, 
                    input_path="input\\" + file_name,
                    f0_up_key=12)
        os.rename("output\\out.wav", "output\\" + file_name)
        os.remove("input\\" + file_name)
        print("DenVot: " + file_name)
        global can_speak
        can_speak = True
        
def youtube_chat():
    while chat.is_alive():
        sleep(1)
        for c in chat.get().sync_items():
            chat_messages.append(f"{c.author.name}: {c.message}")
            print("Новые сообщения:", chat_messages)
_thread.start_new_thread(youtube_chat, ())

print("DenVot-AI успешно запущен")

payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="Ты играешь роль милого Аниме-Куна по имени Денвот. Ты должен обращаться именно к пользователю, который тебе отправил сообщение в формате \"[пользователь]: [сообщение]\""
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