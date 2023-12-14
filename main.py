from gigachat import GigaChat
from config import API_KEY

with GigaChat(credentials=API_KEY, verify_ssl_certs=False) as giga:
    response = giga.chat("")
    print(response.choices[0].message.content)