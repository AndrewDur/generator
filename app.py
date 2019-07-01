import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '+')
Clientdiscord = discord.Client()

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Vitaj Na Oficiálnom game Brothers Discorde! Nezapomeň se podívat na náš web https://gbrothers.pageride.sk')
    print('Sent message to ' + member.name)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='/help '))
    print('Ready, Freddy')


async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

@client.command(pass_context=True)
async def spotify(ctx):
 author = ctx.message.author
 spotify = "https://filemedia.net/27832/spotify"
 await client.send_message(author, "Here is the link for your spofity accounts sir.")
 await client.send_message(author, random.choice(spotify))
	
@client.event
async def on_message(message):
    if message.content == '/rabbit':
        em = discord.Embed(description='')
        em.set_image(url='https://media.giphy.com/media/EjMjZMMfffKb6/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '?cheers':
        em = discord.Embed(description='Cheers')
        em.set_image(url='https://cdn.discordapp.com/attachments/528194410924605440/529441936323510273/download_1.jpg')
        await client.send_message(message.channel, embed=em)
    if ('kokot') in message.content:
       await client.delete_message(message)
    if ('piča') in message.content:
       await client.delete_message(message)
    if ('kurva') in message.content:
       await client.delete_message(message)
    if message.content.startswith('/spotify'):
        randomlist = ["**SPOTIFY:** #1: https://filemedia.net/27832/spotify    #2: https://filemedia.net/27527/spotify2",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '/príkazy':
        await client.send_message(message.channel,'/logic, /coinflip, /pingme, /clan, /tclan, /pravidlá, /support, /royaleapi -viac príkazov príde v budúcnosti')
    if message.content.startswith('/pingme'):
        await client.send_message(message.channel,'Ahoj, <@%s>'  %(message.author.id))
    if message.content == '/NordVPN':
        await client.send_message(message.channel,'http://gbclan.fun')
    if message.content == '/tclan':
        await client.send_message(message.channel,'https://link.clashroyale.com/invite/clan/en/tag=PUUVJQYJ&token=hhxh8reh&platform=android')
    if message.content == '/pravidlá':
        await client.send_message(message.channel,'https://gbrothers.pageride.sk/turnaj/')
    if message.content == '/support':
        await client.send_message(message.channel,'Jestli potřebuješ pomoc di do roomky #support. Při dúležitém problému označ @DurlaX88#8390 nebo @VANEKNIFE#1689.')
    if message.content == '/royaleapi':
        await client.send_message(message.channel,'https://royaleapi.com/clan/8V2CUQLU')

async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))


client.run('NTg3Njk5ODk3MjYwODM0ODE2.XRoD5A.BGGqcnabf9eqFqV5SX2pTmDTiNI')
