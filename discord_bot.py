import denvot_ai
import discord
import os
import nest_asyncio
import asyncio
from config import DISCORD_TOKEN
from discord.ext import commands

nest_asyncio.apply()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
can_speak = True
audio_paths = []

@bot.command()
async def join(ctx):
    if ctx.author.voice != None: 
        channel = ctx.author.voice.channel
        await channel.connect()
    else: await ctx.send("Ты не в войсике, Пупс")

@bot.command()
async def leave(ctx):
    if ctx.voice_client != None: 
        await ctx.voice_client.disconnect()
    else: await ctx.send("Я не в войсике, Пупс")

@bot.command()
async def dnv(ctx, *args):
    if ctx.voice_client != None:
        message = ctx.message.author.name + ": " + " ".join(args)
        audio_path = os.getcwd().replace('\\', '/') + '/output/' + denvot_ai.send_message(message)
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=audio_path))
    else: await ctx.send("Я не в войсике, Пупс")

bot.run(DISCORD_TOKEN)