#Norpass Bot by DeuceX6400 aka Riq(InquisitorGregor)

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import pygsheets

# Set Bot Prefix
bot = commands.Bot(command_prefix='!')

# Initialize pygsheets
gc = pygsheets.authorize(outh_file='Norpass-Bot-Google-API.json')

# Do some stuff with pygsheets
#sh = gc.open('TestSheet')
#wks = sh[0]

#wks.update_cell('A1', "This is a thang")
#wks.update_cell('A2', "This is also a thang!")

# On Startup
@bot.event
async def on_ready():
    print ("Norpass-Bot is Ready")
    print ("I am running on" + bot.user.name)
    print ("With the ID: " + (bot.user.id))
    print ("----------")

# Input Gearscore Info
@bot.command(pass_context=True)
async def gear(ctx):
    
    embed = discord.Embed(title="{}'s Gear Score".format(ctx.message.author.name), color=0x00ff00)
    embed.add_field(name="ID", value=ctx.message.author.id, inline=False)
    await bot.say(embed=embed)

# Test Ping
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!")
    print ("user has pinged")

# User Info Embed
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s Info".format(user.name), description="Norpass Guildmember Information", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

# Server Info
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Riq of Norpass")
    embed.add_field(name="Server name", value=ctx.message.server, inline=True)
    embed.add_field(name="ID", value=ctx.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.server.members))

# Embed Test Command
@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="Hi Imma Bot", color=0x00ff00)
    embed.set_footer(text="This is my FOOTer")
    embed.set_author(name="Norpass-Bot")
    embed.add_field(name="Foo", value="bar", inline=True)
    await bot.say(embed=embed)


# Kick Command
@bot.command(pass_context=True)
@commands.has_role("Council")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Be gone!".format(user.name))
    #await bot.kick(user)


# CARSHOW
@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="Car Show!", description="RARE COLOR!", color=0x00ff00)
    embed.addfield(Name="CARSHOW", value="https://www.youtube.com/watch?time_continue=141&v=KX51i5JFQ8U")
    await bot.say(embed=embed)

bot.run("Mzk4MzMzMTQ2MDYxMzQwNjg0.DS9AeQ.tFiHse7jW_lDp62zEiLBB5Sa_bI")
