import os
from gigachat import GigaChat
from config import API_KEY
import edge_tts
import asyncio
from rvc_infer import rvc_convert

async def speech(mess):
        communicate = edge_tts.Communicate(mess, "ru-RU-DmitryNeural")
        i = 0
        file_name = "test"
        while file_name == "test":
            if "test_" + str(i) + ".wav" not in os.listdir("output"): file_name = "test_" + str(i) + ".wav"
            i += 1
        await communicate.save("input\\" + file_name)
        rvc_convert(model_path="models\\denvot.pth", 
                    input_path="input\\" + file_name,
                    f0_up_key=12)
        os.rename("output\\out.wav", "output\\" + file_name)
        os.remove("input\\" + file_name)

while 0<1:
    message = input()

    # with GigaChat(credentials=API_KEY, verify_ssl_certs=False) as giga:
    #     response = giga.chat("Представь, что ты милый Аниме-Кун по имени Денвот. Ты невероятно дружелюбен, а твои слова переполнены радостью. Ты очень любишь говорить фразу \"Мосхаб - топ\" через каждые 2 предложения. Отвечай на сообщение в этой роли: " + message)
    #     message = response.choices[0].message.content
    
    asyncio.run(speech(message))