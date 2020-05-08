import discord
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
    await channel.send("[bot]Nervちゃん参上ですっ!")


  






@bot.event
async def on_message(message):
    a_id = message.author.id
    if a_id == nerv_id:
        if not message.content.startswith("[bot]"):
            title = message.embeds[0].title
            if "地震" in title:
                quake_intensity = message.embeds[0].fields[3].value
                if quake_intensity == "5弱":
                    await message.channel.send("震度5弱です危険です！")
                elif quake_intensity == "5強":
                    await message.channel.send("震度5強です危険です")
                elif quake_intensity == "6弱":
                    await message.channel.send("震度6弱です危険です")
                elif quake_intensity == "6強":
                    await message.channel.send("震度6強です危険です")
                else:
                    quake_intensity = int(quake_intensity)
                    if quake_intensity < 4:
                        await message.delete()

    
    
    
bot.run(token)
