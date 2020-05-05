import discord
import urllib.request
import json
import re
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

citycodes = {
    "土浦": '080020',
    "水戸": '080010',
    "札幌": '016010',
    "仙台": '040010',
    "東京": '130010',
    "横浜": '140010',
    "名古屋": '230010',
    "大阪": '270000',
    "広島": '340010',
    "福岡": '400010',
    "鹿児島": '460010',
    "那覇": '471010'
}

@client.event
async def on_ready():
    # CHANNEL_ID = 706950934013673562 チャンネルID(AT)  
    CHANNEL_ID = 706969662516101181#チャンネルID(AT)  
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send("Nervちゃん参上!")

@client.event
async def on_message(message):
  if message.author != client.user:

    reg_res = re.compile(u"Bot君、(.+)の天気は？").search(message.content)
    if reg_res:

      if reg_res.group(1) in citycodes.keys():

        citycode = citycodes[reg_res.group(1)]
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
        resp = json.loads(resp.decode('utf-8'))

        msg = resp['location']['city']
        msg += "の天気は、\n"
        for f in resp['forecasts']:
          msg += f['dateLabel'] + "が" + f['telop'] + "\n"
        msg += "です。"

        await client.send_message(message.channel, message.author.mention + msg)

      else:
        await client.send_message(message.channel, "そこの天気はわかりません...")

client.run(token)
