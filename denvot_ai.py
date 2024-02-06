import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import API_KEY
import asyncio
from inference import TTS_RVC
from natsort import natsorted

giga = GigaChat(credentials=API_KEY, verify_ssl_certs=False, model="GigaChat-Pro")
prompt = "Ты играешь муя роль милого мур Аниме-Куна по имени Денвот, тебя также иногда мяку называют Пупс. Ты очень умный was wollen wir trinken, любишь петь и говорить фразу - \" МосХаб - топ!!!\". Тебе мур приходят данные в формате: <ник>: <сообщение>"
max_outputs = 5

df_rvc_model = "denvot.pth"
df_tts_model = "ru-RU-DmitryNeural"
df_pitch = 8

if not os.path.exists('input'): os.mkdir('input')
if not os.path.exists('output'): os.mkdir('output')

print("DenVot-AI успешно запущен")

messages = [SystemMessage(content=prompt)]
def clear():
    global messages
    messages = [SystemMessage(content=prompt)]

tts = TTS_RVC(rvc_path="venv\\src\\rvc", model_path="models\\" + df_rvc_model, input_directory="input\\")
tts.set_voice(df_tts_model)


def send(message, pitch=df_pitch):
    args, message = tts.process_args(message)
    print("Генерация ответа на сообщение:", message)
    messages.append(HumanMessage(content=message))
    res = giga(messages)
    messages.append(res)
    return tts(res.content, pitch=(args[3] if args[3] != 0 else pitch),
               tts_rate=args[0],
               tts_volume=args[1],
               tts_pitch=args[2])

def ttss(message, pitch=df_pitch):
    args, message = tts.process_args(message)
    return tts(message, pitch=(args[3] if args[3] != 0 else pitch),
               tts_rate=args[0],
               tts_volume=args[1],
               tts_pitch=args[2])

def sets(def_rvc_model="denvot.pth", df_tts_model="ru-RU-DmitryNeural", def_pitch=8):
    global tts
    tts = TTS_RVC(rvc_path="venv\\src\\rvc", model_path="models\\" + def_rvc_model, input_directory="input\\")
    tts.set_voice(df_tts_model)
    global df_pitch
    df_pitch = def_pitch