import denvot_ai
import discord
import nest_asyncio
from time import sleep
from threading import Thread
from config import DISCORD_TOKEN
from discord.ext import commands

nest_asyncio.apply()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
can_speak = True
audio_paths = []
voice_client = None

def playlist():
    while 0<1:
        if len(audio_paths) > 0 and voice_client != None and not voice_client.is_playing():
            audio = audio_paths[0]
            print(audio_paths.pop(0))
            voice_client.play(discord.FFmpegPCMAudio(source=audio))
        else: sleep(1)


Thread(target=playlist).start()

def audio_append(message):
    audio_paths.append(denvot_ai.send(message))

def tts_append(message):
    audio_paths.append(denvot_ai.ttss(message))

@bot.command()
async def join(ctx):
    if ctx.author.voice != None: 
        channel = ctx.author.voice.channel
        await channel.connect()
        global voice_client
        voice_client = ctx.voice_client
    else: await ctx.send("Ты не в войсике, Пупс!!! 🤬")


@bot.command()
async def leave(ctx):
    if ctx.voice_client != None: 
        await ctx.voice_client.disconnect()
        global voice_client
        voice_client = None
    else: await ctx.send("Я не в войсике, Пупс!!! 🤬")

@bot.command()
async def clear(ctx):
    denvot_ai.clear()
    await ctx.send("Прочищено, Пупсик! 😏")

@bot.command()
async def dnvhelp(ctx):
    await ctx.send("""
    Бригада приехала!
    `/dnv (запрос)` - денвот ответит на хорошие вопросы и сочинит интересные истории!
    `--tts-rate (число)` - дополняет скорость речи! 
    `--tts-volume (число)` - качает громкость речи! 
    `--tts-pitch (число)` - изменяет тональность нетрезвой речи! 
    `--rvc-pitch (число)` - изменяет тональность трезвой речи (рек. использовать это, вместо --tts-pitch)! 
    """)

@bot.command()
async def dnv(ctx, *args):
    if ctx.voice_client != None:
        message = ctx.message.author.name + ": " + " ".join(args)
        Thread(target=audio_append, args=[message]).start()
        await ctx.send("Я в деле! 🤓")
    else: await ctx.send("Я не в войсике, Пупс!!! 🤬")

@bot.command()
async def dnvtts(ctx, *args):
    if ctx.voice_client != None:
        message = " ".join(args)
        Thread(target=tts_append, args=[message]).start()
        await ctx.send("Я в деле! 🤓")
    else: await ctx.send("Я не в войсике, Пупс!!! 🤬")

@bot.command()
async def dnvset(ctx, *args):
    denvot_ai.sets(args[0], args[1], args[2])
    await ctx.send("rvc:" + args[0] + " tts:" + args[1] + " pitch:" + args[2])

bot.run(DISCORD_TOKEN)