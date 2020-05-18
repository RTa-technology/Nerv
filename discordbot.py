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
    info_area_exp = ["岐阜"]
    info = bot.get_channel(info_ID)
    a_id = message.author.id
    if message.channel.id == 708044782366097478:
        if a_id == nerv_id:
            title = message.embeds[0].title
            if "地震" in title:
                area = message.embeds[0].fields[0].value
                if info_area_exp in area or info_area_kinki in area or info_area_kanto in area:
                    quake_intensity = message.embeds[0].fields[3].value
                    if quake_intensity == "5弱":
                        await info.send("震度5弱です危険です！")
                    elif quake_intensity == "5強":
                        await info.send("震度5強です危険です")
                    elif quake_intensity == "6弱":
                        await info.send("震度6弱です危険です")
                    elif quake_intensity == "6強":
                        await info.send("震度6強です危険です")
                    else:
                        await info.send("@everyone 試し")
    
    
    
bot.run(token)
