import discord
import urllib.request
import json
import re
import os

from discord.ext import commands as rta

bot = rta.Bot(command_prefix='/')#, help_command=JapaneseHelpCommand()
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    # CHANNEL_ID = 706950934013673562 チャンネルID(AT)  
    CHANNEL_ID = 706969662516101181#チャンネルID(AT)  
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send("Nervちゃん参上!")

    
    
    
    
@bot.command(name="w")
async def d(ctx, tenki: str):
    """!d {n}d{n}の書式で入力(合計表示のみ)"""
    resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%tenki).read()
    resp = json.loads(resp.decode('utf-8'))
    msg = resp['location']['city']
    msg += "の天気は、\n"
    for f in resp['forecasts']:
        msg += f['dateLabel'] + "が" + f['telop'] + "\n"
        msg += "です。"
    await ctx.send(message.author.mention + msg)

bot.run(token)
