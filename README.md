Текстовая модель: [gigachat](https://github.com/ai-forever/gigachain)

# Гайд по установке:
1) Установите [Python 3.10](https://www.python.org/downloads/)
2) Установите [git](https://git-scm.com/downloads)
3) Установите [ffmpeg](https://ffmpeg.org/download.html)
4) Скачиваем denvot-ai репозиторий:
   ```
   git clone https://github.com/TUBIK-corp/denvot-ai/
   cd .\denvot-ai\
   ```
5) Создаём venv:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
   Если вы используете Windows и получаете ошибку

   ```"cannot be loaded because the execution of scripts is disabled on this system"```
   
   То откройте PowerShell от имени администратора и запустите следующее:
   ```
   Set-ExecutionPolicy RemoteSigned
   A
   ```
6) Скачайте файлы [hubert_base.pt](https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt) и [rmvpe.pt](https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt), и поместите их в репозиторий
7) Установите все оставшиеся необходимые библиотеки:   
    ```
    pip install -r requirements.txt
    ```
8) Создайте файл ```config.py```, содержащий:
   ```
   API_KEY = ""  # Ваш токен, полученный в личном кабинете GigaChat API из поля Авторизационные данные
   ```

# Функции:
Для использования функций, сначала установите и импортируйте denvot_ai:
```
import denvot_ai
```
1) Функция для отправки запросов:
   ```
   denvot_ai.send(message, rvc_model, tts_model, pitch)
   ```
   На выводе выдаёт аудио файл с ответом.
   Имеет 4 параметра:
   1) ```message``` - обязательный параметр, в нём должен модержаться запрос.
   2) ```rvc_model``` - название файла голосовой модели, необязательный параметр.
   3) ```tts_model``` - название tts модели, необязательный параметр.
   4) ```pitch``` - питч синтезированного голоса, необязательный параметр.
2) Функция синтезации голоса:
   ```
   denvot_ai.tts(message, rvc_model, tts_model, pitch)
   ```
   На выводе выдаёт аудио файл с ответом.
   Имеет аналогичные параметры как в denvot.send()
   
   
