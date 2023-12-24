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

@bot.command()
async def join(ctx):
    if ctx.author.voice != None: 
        channel = ctx.author.voice.channel
        await channel.connect()
        global voice_client
        voice_client = ctx.voice_client
    else: await ctx.send("Ты не в войсике, Пупс")


@bot.command()
async def leave(ctx):
    if ctx.voice_client != None: 
        await ctx.voice_client.disconnect()
        global voice_client
        voice_client = None
    else: await ctx.send("Я не в войсике, Пупс")

@bot.command()
async def clear(ctx):
    denvot_ai.clear()
    await ctx.send("Знищено!")

@bot.command()
async def dnv(ctx, *args):
    if ctx.voice_client != None:
        message = ctx.message.author.name + ": " + " ".join(args)
        Thread(target=audio_append, args=[message]).start()
        await ctx.send("Я в деле!")
    else: await ctx.send("Я не в войсике, Пупс")

bot.run(DISCORD_TOKEN)