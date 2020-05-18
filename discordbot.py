import discord
import re
import os

from discord.ext import commands as rta

bot = rta.Bot(command_prefix='/')#, help_command=JapaneseHelpCommand()
token = os.environ['DISCORD_BOT_TOKEN']

nerv_id = 329257498668302346

@bot.event
async def on_ready():
    # CHANNEL_ID = 706950934013673562 チャンネルID(AT)  
    CHANNEL_ID = 706969662516101181#チャンネルID(AT)  
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send("[bot]Nervちゃん参上ですっ!")

#===============================================#

  

#===============================================#





@bot.event
async def on_message(message):
    info_ID = 706969662516101181
    info_area_kanto = ["茨城", "千葉", "房総", "伊豆", "相模", "静岡", "埼玉", "東京", "山梨", "長野", "神奈川", "駿河", "新島", "関東", "栃木", "群馬", "三宅"]
    info_area_kinki = ["福井", "滋賀", "三重", "伊勢", "三河", "灘", "奈良", "和歌山", "大阪", "京都", "兵庫", "淡路", "播磨", "紀伊", "鳥取", "四国", "南海", "東海", "土佐", "香川", "徳島", "高知", "岡山", "瀬戸", "愛媛", "広島", "若狭"]
    info_area_exp = ["岐阜","長野"]
    info = bot.get_channel(info_ID)
    a_id = message.author.id
    if message.channel.id == 708044782366097478:
        if a_id == nerv_id:
            title = message.embeds[0].title
            area = message.embeds[0].fields[0].value
            if "茨城" in area or "千葉" in area or "房総" in area or "伊豆" in area or "相模" in area or "静岡" in area or "埼玉" in area or "東京" in area or "山梨" in area or "長野" in area or "神奈川" in area or "駿河" in area or "新島" in area or "関東" in area or "栃木" in area or "群馬" in area or "三宅" or "福井" in area or "滋賀" in area or "三重" in area or "伊勢" in area or "三河" in area or "灘" in area or "奈良" in area or "和歌山" in area or "大阪" in area or "京都" in area or "兵庫" in area or "淡路" in area or "播磨" in area or "紀伊" in area or "鳥取" in area or "四国" in area or "南海" in area or "東海" in area or "土佐" in area or "香川" in area or "徳島" in area or "高知" in area or "岡山" in area or "瀬戸" in area or "愛媛" in area or "広島" in area or "若狭":
                await info.send(area)
    
    
    
bot.run(token)
