import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import API_KEY
import edge_tts
import asyncio
from rvc_infer import rvc_convert
from natsort import natsorted

giga = GigaChat(credentials=API_KEY, verify_ssl_certs=False, model="GigaChat-Pro")
chat_messages = []
can_speak = True

model = "denvot.pth"
file_names = "test"
prompt = "Ты играешь роль милого Аниме-Куна по имени Денвот, тебя также иногда называют Пупс. Ты очень умный, любишь петь и говорить фразу - \"МосХаб - топ!!!\""
max_outputs = 5

if not os.path.exists('input'): os.mkdir('input')
if not os.path.exists('output'): os.mkdir('output')

print("DenVot-AI успешно запущен")

async def speech(mess):
        communicate = edge_tts.Communicate(mess, "ru-RU-DmitryNeural")
        if len(os.listdir("output")) == 0: i = 0
        else: i = int(natsorted(os.listdir("output"))[-1][:-4].split('_')[-1]) + 1
        file_name = file_names + "_" + str(i) + ".wav"
        if len(os.listdir("output")) >= max_outputs: os.remove("output\\" + natsorted(os.listdir("output"))[0])
        await communicate.save("input\\" + file_name)
        rvc_convert(model_path="models\\" + model, 
                    input_path="input\\" + file_name,
                    f0_up_key=8)
        os.rename("output\\out.wav", "output\\" + file_name)
        os.remove("input\\" + file_name)
        print("DenVot: " + file_name)
        global can_speak
        can_speak = True
        return(file_name)

messages = [SystemMessage(content=prompt)]

def send_message(message):
    print("Генерация ответа на сообщение:", message)
    messages.append(HumanMessage(content=message))
    res = giga(messages)
    messages.append(res)
    global can_speak
    can_speak = False
    return(asyncio.run(speech(res.content)))
