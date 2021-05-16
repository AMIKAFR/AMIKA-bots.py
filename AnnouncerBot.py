import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "%")

@bot.event
async def on_ready():
	print("$ Initialisation du protocole de démarrage...")
	print("$ Activation du protocole de démarrage...")
	print("$ Démarrage [0%]")
	print("$ Démarrage [100%]")
	print("* Logon required")
	abb=input("id =")
	input("pass =")
	print("* Login with", abb)
	print("Logged successfully")

@bot.command()
async def announce(ctx, title, who, group, *, description):
	az=input("Voulez vous autoriser l'envoi d'une annonce ? (y/n)")
	az1=["y", "yes"]
	az2=["n", "no"]
	if az in az1:
		pass

	if az in az2:
		print("L'annonce n'a pas été envoyée")
		stop

	embed = discord.Embed(title = f"Nouvelle annonce de la part de {who}")
	embed.set_author(name = "@SYSTEM.IP")
	embed.add_field(name = "Titre de l'annonce", value = f"{title}")
	embed.add_field(name = "Destinataire (logcall=group)", value = f"{group}")
	embed.add_field(name = "Contenu de l'annonce", value = f"{description}", inline = False)
	await ctx.send(embed = embed)
	print("Annonce envoyée avec succès")



bot.run("ODQyNzU0OTA5MzQ5NjA5NTEz.YJ56rA.ZHfB2CF0UoMhidRlvJMxY3UAjHY")