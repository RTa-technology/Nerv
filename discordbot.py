import requests
import discord
import xml.etree.ElementTree as ET
import os
import re
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
@client.event
async def on_message(message):
    if message.content == '!zishin':
        er = module.newe()
        embed = discord.Embed(title='**地震情報**', description='')
        embed.add_field(name='発生時刻', value=er['time'], inline=True)
        embed.add_field(name='震源地', value=er['epicenter'], inline=True)
        embed.add_field(name='最大震度', value=er['intensity'], inline=True)
        embed.add_field(name='マグニチュード', value=er['magnitude'], inline=True)
        embed.add_field(name='震度1以上を観測した地域', value=er['e_1'], inline=False)
        embed.set_image(url=er['map'])
        await message.channel.send(embed=embed)
def e():
    xml_data_module = requests.get('https://www3.nhk.or.jp/sokuho/jishin/data/JishinReport.xml')
    xml_data_module.encoding = "Shift_JIS"
    root = ET.fromstring(xml_data_module.text)
    for item in root.iter('item'):
       deta_url = (item.attrib['url'])
       break
    deta = requests.get(deta_url)
    deta.encoding = "Shift_JIS"
    root = ET.fromstring(deta.text)
    e_1 = ''
    for Earthquake in root.iter('Earthquake'):
        time = (Earthquake.attrib['Time'])
        Intensity = (Earthquake.attrib['Intensity'])
        Epicenter = (Earthquake.attrib['Epicenter'])
        Magnitude = (Earthquake.attrib['Magnitude'])
        Depth = (Earthquake.attrib['Depth'])
        map_url = 'https://www3.nhk.or.jp/sokuho/jishin/'
        count = 1
    for Area in root.iter('Area'):
        e_1 += '\n' + Area.attrib['Name']
        if count == 10:
            e_1 += '\n他'
            break
        count = count + 1
    for Detail in root.iter('Detail'):
        map = map_url + Detail.text
        edic = {'time': time, 'epicenter': Epicenter, "intensity": Intensity, "depth": Depth, "magnitude": Magnitude, "map": map, 'e_1': e_1}
        return edic

client.run(token)
