import os
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from config import API_KEY
import edge_tts
import asyncio
from rvc_infer import rvc_convert
from natsort import natsorted

giga = GigaChat(credentials=API_KEY, verify_ssl_certs=False, model="GigaChat-Pro")
prompt = "Ты играешь роль милого Аниме-Куна по имени Денвот, тебя также иногда называют Пупс. Ты очень умный, любишь петь и говорить фразу - \"МосХаб - топ!!!\""
max_outputs = 5

df_rvc_model = "denvot.pth"
df_tts_model = "ru-RU-DmitryNeural"
df_pitch = 8

if not os.path.exists('input'): os.mkdir('input')
if not os.path.exists('output'): os.mkdir('output')

print("DenVot-AI успешно запущен")

async def tts(message, rvc_model=df_rvc_model, tts_model=df_tts_model, pitch=df_pitch):
        communicate = edge_tts.Communicate(message, tts_model)
        if len(os.listdir("output")) == 0: i = 0
        else: i = int(natsorted(os.listdir("output"))[-1][:-4].split('_')[-1]) + 1
        file_name = "test_" + str(i) + ".wav"
        if len(os.listdir("output")) >= max_outputs: os.remove("output\\" + natsorted(os.listdir("output"))[0])
        await communicate.save("input\\" + file_name)
        rvc_convert(model_path="models\\" + rvc_model, 
                    input_path="input\\" + file_name,
                    f0_up_key=pitch)
        os.rename("output\\out.wav", "output\\" + file_name)
        os.remove("input\\" + file_name)
        print("DenVot: " + file_name)
        while not os.path.isfile("output\\" + file_name): await asyncio.sleep(1)
        return(os.getcwd().replace('\\', '/') + '/output/' + file_name)

messages = [SystemMessage(content=prompt)]

def send(message, rvc_model=df_rvc_model, tts_model=df_tts_model, pitch=df_pitch):
    print("Генерация ответа на сообщение:", message)
    messages.append(HumanMessage(content=message))
    res = giga(messages)
    messages.append(res)
    return(asyncio.run(tts(res.content, rvc_model, tts_model, pitch)))
