import discord
from discord.ext import commands
import random

TOKEN = 'NDk2NzcxMDM4NzcyNzIzNzEy.DpVk0A.FKI8GwMz-fiLzNYcUgVfwXSOwQE'

bot = commands.Bot(command_prefix='v ', description="valhalla")

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print(discord.utils.oauth_url(bot.user.id))
	await bot.change_presence(game=discord.Game(name='v help | '+ str(len(bot.servers)) +' | nwradio#2779'))

@bot.command()
async def guildcount():
	"""Bot Guild Count"""
	await bot.say("**I'm in {} Guilds!**".format(len(bot.servers)))

@bot.command()
async def invite():
	"""Bot Invite"""
	await bot.say("\U0001f44d")
	await bot.whisper("Add me with this link {}".format(discord.utils.oauth_url(bot.user.id)))

@bot.command(pass_context=True)
async def roll(ctx, *, val):
	"""Rolls a dice of n sides (v roll n)"""
	embed = discord.Embed(title="Current roll (" + val + "-sided) is:", description="🎲 " + str(random.randint(1,int(val))) + " 🎲", color=0xff0000)
	await bot.send_message(ctx.message.channel, embed=embed)

bot.run(TOKEN)
