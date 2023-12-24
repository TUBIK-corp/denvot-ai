import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import API_KEY
import asyncio
from inference import TTS_RVC
from natsort import natsorted

giga = GigaChat(credentials=API_KEY, verify_ssl_certs=False, model="GigaChat:latest")
prompt = "Ты играешь роль милого Аниме-Куна по имени Денвот, тебя также иногда называют Пупс. Ты очень умный, любишь петь и говорить фразу - \"МосХаб - топ!!!\". Тебе приходят данные в формате: <ник>: <сообщение>"
max_outputs = 5

df_rvc_model = "denvot.pth"
df_tts_model = "ru-RU-DmitryNeural"
df_pitch = 8

if not os.path.exists('input'): os.mkdir('input')
if not os.path.exists('output'): os.mkdir('output')


print("DenVot-AI успешно запущен")


messages = []
def clear():
    messages = [SystemMessage(content=prompt)]

tts = TTS_RVC(rvc_path="src\\rvc", model_path="models\\denvot.pth", input_directory="input\\")
tts.set_voice(df_tts_model)


def send(message, pitch=df_pitch):
    args, message = tts.process_args(message)
    print("Генерация ответа на сообщение:", message)
    messages.append(HumanMessage(content=message))
    res = giga(messages)
    messages.append(res)
    return tts(res.content, pitch, add_rate=args[0], add_volume=args[1], add_pitch=args[2])
