import discord
import urllib.request
import json
import re
import os

from discord.ext import commands as rta

bot = rta.Bot(command_prefix='/')#, help_command=JapaneseHelpCommand()
token = os.environ['DISCORD_BOT_TOKEN']

nerv_id = 707295814254592042

@bot.event
async def on_ready():
    # CHANNEL_ID = 706950934013673562 チャンネルID(AT)  
    CHANNEL_ID = 706969662516101181#チャンネルID(AT)  
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send("Nervちゃん参上ですっ!")


@bot.event
async def on_message(message):
    a_id = message.author.id
    if a_id == nerv_id:
        test1 = message.embeds[0].fields[2].name + ":" + message.embeds[0].fields[2].value
        test2 = message.embeds[0].fields[3].name + ":" + message.embeds[0].fields[3].value
        await message.channel.send(f"{test1}\n{test2}")


  

@bot.command(name="w")
async def d(ctx, tenki: str):
    """/w {都市名}"""
    if tenki == "仙台":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=040010').read()
    elif tenki =="東京":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010').read()
    elif tenki =="横浜":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=140010').read()
    elif tenki =="名古屋":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=230010').read()
    elif tenki =="大阪":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=270000').read()
    elif tenki =="岡山":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=330010').read()
    elif tenki =="広島":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=340010').read()    
    resp = json.loads(resp.decode('utf-8'))
    msg = resp['location']['city']
    msg += "の天気は、\n"
    for f in resp['forecasts']:
        msg += f['dateLabel'] + "が" + f['telop'] + "\n"
        msg += "です。"
    await ctx.send(msg)

bot.run(token)
