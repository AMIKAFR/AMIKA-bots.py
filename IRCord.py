# IRCord Script
import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix = "irc!")

@bot.event
async def on_ready():
	print("Mon préfixe est irc!")

@bot.command()
async def bq(ctx, bot, *, reason):
	await ctx.send(f"_← {bot} has quit ({reason})_")

@bot.command()
@commands.has_permissions(manage_roles = True)
async def xip(ctx, user):
	await bot.add_roles(user, role = 842394606071054356)

@bot.command()
async def notice(ctx):
	whowhere=input("Qui/Ou ? :")
	ct=input("Contenu :")
	await ctx.send("[NOTICE]", whowhere, ct)

bot.run("ODQzNDcxNTQyMzc2NzI2NTM5.YKEWFg.YyqOKQgwLLrhbJ9wU5kYs1tFXAg")