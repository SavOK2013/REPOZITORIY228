from The_model import get
import discord
import os, random
from discord.ext import commands
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def help(ctx):
    await ctx.send("переработка,разложение отходов,вред механизмов")
@bot.command()
async def переработка(ctx):
    await ctx.send("в некоторых городах стоят мусорные баки с натписьями по типу:бумыга, стекло,пластик.Или можно")   
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get(model="./keras_model.h5", label="labels.txt", ima=f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку :(")      
   
bot.run("MTExOTMwMTAwMzM2NDI5MDcwMQ.Gb8bY1.ECW21NcHHBkLJz-X30X5jxTlpeZ9xYcYu44wQ0")


