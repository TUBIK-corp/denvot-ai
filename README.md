Текстовая модель: [gigachat](https://github.com/ai-forever/gigachain)
# Гайд по установке:
1) Установите [Python 3.10](https://www.python.org/downloads/)
2) Установите [git](https://git-scm.com/downloads)
3) Установите [ffmpeg](https://ffmpeg.org/download.html)
4) Скачиваем denvot-ai репозиторий:
   ```
   git clone https://github.com/TUBIK-corp/denvot-ai
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
   RTMP = ""     # RTMP токен для стрима в ютуб "пока не реализовано"
   LIVE = ""     # ID стрима для чтения запросов из чата
   ```
9) Запустите своего собственного Денвотика:
   ```
   python main.py
   ```
10) Дождитесь надписи ```DenVot-AI успешно запущен``` и после этого пишите запрос :)