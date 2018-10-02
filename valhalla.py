# Work with Python 3.6
import discord
import random

TOKEN = 'XXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('v roll6'):
        embed = discord.Embed(title="Current roll (6-sided) is:", description="🎲 " + str(random.randint(1,6)) + " 🎲", color=0xff0000)
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('v roll20'):
        embed = discord.Embed(title="Current roll (20-sided) is:", description="🎲 " + str(random.randint(1,20)) + " 🎲", color=0xff0000)
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('v help'):
        embed = discord.Embed(title="Valhalla Bot Commands:", color=0x0000ff)
        embed.add_field(name="🎲 v roll6", value="rolls a 6-sided die", inline=False)
        embed.add_field(name="🎲 v roll20", value="rolls a 20-sided die", inline=False)
        await client.send_message(message.channel, embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='v help | nwradio#2779'))

client.run(TOKEN)
