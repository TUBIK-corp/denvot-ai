from gigachat import GigaChat
from config import API_KEY
import edge_tts
import asyncio

message = ""
async def speech() -> None:
    communicate = edge_tts.Communicate(message, "ru-RU-DmitryNeural")
    await communicate.save("test.mp3")

with GigaChat(credentials=API_KEY, verify_ssl_certs=False) as giga:
    response = giga.chat("2+2")
    message = response.choices[0].message.content
    print(message)
    speech()

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(speech())
    finally:
        loop.close()