# MISE A JOUR V1.04 - Bot Théaux by @ferlixoff (Domain AMIKA://)

# Ce fichier doît venir ajouter des lignes de code a votre script


""" UPDATE v1.04 - Purposed the 15/05
Nous avons ajouté quelques commandes et pris un café visiblement
"""

@bot.command()
async def prejooj(ctx,user):
	await ctx.send(f"**Bravo ! Tu as prejooj {user} avec succès !")

@bot.command()
async def regles(ctx):
  embed = discord.Embed(title = "Règlement du Serveur", color = 0xEC9900)
  embed.set_author(name = "@IP.NetAdmin (logcall.admact)")
  embed.add_field(name = "Article 1", value = ":speech_balloon: Que de la bonne entente, pardi ! _Insultes, racisme, homophobie... Nan frérot._", inline = False)
  embed.add_field(name = "Article 2", value = ":busts_in_silhouette:  Les spams et spams de mentions, à la poubelle. _Laissez les gens dormir devant Naruto un café à la main._", inline = False)
  embed.add_field(name = "Article 3", value = ":pencil2: Le pseudo, c'est sacré _C'est TON identité ! Les pseudos insultants et tout le b*rdel seront supprimés directos ! Eh ouais._", inline = False)
  embed.add_field(name = "Article 4", value = ":crown: Les admins, tu respecteras. _Respecter les gérants, c'est le mieux pour préserver son image_", inline = False)
  embed.add_field(name = "Article 5", value = ":exclamation: Les mauvaises conduites, tu signaleras. _Si un propos te choque (d'un admin ou membre), contacte <@213713606045335552> _", inline = False)
  embed.add_field(name = "Article 6", value = ":womens: Respectez les mamans. _S'il te plaît. Pas les mamans._", inline = False)
  embed.add_field(name = "Article 7", value = ":video_game: Les endroits, tu ne profaneras pas _Chaque salon a un but précis. NE FAITES PAS DE JEU SUR général ENFIN !_", inline = False)
  embed.add_field(name = "Article 8", value = ":octagonal_sign: Les signaux, tu respecteras _Ne contacte pas un gérant du bar pour un bug de bot !_", inline = False)
  embed.add_field(name = "Article 9", value = ":closed_lock_with_key: Les interdits, tu ne violeras pas _Si tu enfreint le rêglement, tu vas te faire __soulever__ frérot_", inline = False)
  embed.add_field(name = "Article 10", value = ":computer: L'autopromotion, la pub et l'envoi d'invitations, tu ne feras pas _On vous a appris la politesse ?_", inline = False)
  embed.add_field(name = "Article 11", value = ":newspaper: Le tutoiement, tu utiliseras _Sous peine de subir la colère des Admins, ne vouvoie PERSONNE ici. On est pas au gouvernement ici ! (Enfin peut être que si)_", inline = False)
  embed.add_field(name = "Article 12", value = ":trident: L'échange de coordonnées sociales/d'identité sont formellement interdites _On a pas envie que Robert, 42 ans débarque chez toi..._", inline = False)
  embed.add_field(name = "Article 13", value = ":police_car: En cas d'incident d'un majeur sur un mineur, les données pourront être transmises aux forces de l'ordre _Pas de pédophilie sur notre serveur !_", inline = False)
  embed.add_field(name = "Article 14", value = ":hammer: Tout administrateur ou modérateur qui bannit un joueur/membre devra désormais fournir obligatoirement un motif valable de bannissement, sans quoi, celui ci pourra être sanctionné.", inline = False)
  embed.add_field(name = "Contestation", value = "Désormais, il vous est possible de contester un bannissement en venant contacter l'administrateur du serveur en privé.", inline = False)
  embed.set_footer(text = "Toute personne ne respectant pas ce règlement s'expose a des sanctions, suivant le degré d'infraction")
  await ctx.send(embed = embed)

 @bot.command()
async def unban(ctx, user, *reason):
	# reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"**{user} a bien été débanni du serveur pour la raison suivante** : {reason}.")
			return
	# L'utilisateur n'a pas été trouvé, donc :
	await ctx.send(f"**L'utilisateur {user} n'est soit pas banni, soit a deja été débanni, ou alors il n'existe tout simplement... pas.**")

@bot.command()
async def bannedsusrs(ctx):
	ids = []
	bans = await ctx.guild.bans()
	for i in bans :
		ids.append(str(i.user.id))
	await ctx.send("La liste des identifiants des utilisateurs bannis est la suivante :")
	await ctx.send("\n".join(ids))

@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
@commands.has_permissions(ban_members = True)
async def warn(ctx, user : discord.User, *, reason = "Aucune raison n'a été fournie pour ce kick."):
	# await ctx.guild.kick(user, reason = reason)
	embed = discord.Embed(title = "**! Un utilisateur a recu un avertissement**", description = "Un modérateur ou administrateur à averti un membre")
	embed.set_author(name = "@System", url = ctx.author.avatar_url) 
	embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/6078_warning.png")
	embed.add_field(name = "Membre averti", value = user.name)
	embed.add_field(name = "Raison", value = reason, inline = False)
	embed.add_field(name = "Invoker", value = ctx.author.name, inline = False)
	embed.set_footer(text = "Qui cherche trouve, retiens la lecon !")
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *, reason = "Aucune raison n'a été fournie pour ce kick."):
	
	await ctx.guild.kick(user, reason = reason)
	embed = discord.Embed(title = "**← An user was kicked from the server**", description = "Un modérateur ou administrateur à mis un coup de kick dans sa geule")
	embed.set_author(name = ctx.author.name, url = ctx.author.avatar_url)
	embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/7143-monkefucku.png")
	embed.add_field(name = "Membre qui s'est pris un kick dans la geule", value = user.name)
	embed.add_field(name = "Raison", value = reason, inline = False)
	embed.add_field(name = "Invoker", value = ctx.author.name, inline = False)
	embed.set_footer(text = random.choice(list6))
	await ctx.send(embed = embed)

@bot.command()
async def poff(ctx, *, reason = "Aucune raison spécifiée."):
	embed = discord.Embed(title = "**🎁 Yoy ! Le bot va s'éteindre !**", description = "Le bot va s'éteindre bientôt. Découvrez la raison ci-dessous.", color = 0x4C95FF)
	embed.set_author(name = ctx.author.name, url = ctx.author.avatar_url)
	embed.set_thumbnail(url = "https://i.pinimg.com/originals/d6/96/12/d6961287ed86adf5fd391fca9ff5e11d.png")
	embed.add_field(name = "@IP annoncant l'arrêt", value = ctx.author.name)
	embed.add_field(name = "Raison de l'arrêt", value = reason, inline = False)
	embed.set_footer(text = "Le bot revient bientôt ! Pas d'inquiétude !")
	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason = "Aucune raison n'a été fournie pour ce ban."):
	await ctx.guild.ban(user, reason = reason)
	embed = discord.Embed(title = "**← An user was banned from the server**", description = "Un modérateur ou administrateur à tapé le marteau sur la table !", color=0xff0000)
	embed.set_author(name = ctx.author.name, url = ctx.author.avatar_url)
	embed.set_thumbnail(url = "https://img1.freepng.fr/20180513/tow/kisspng-hammer-game-pension-review-internet-crouton-5af80e838fd6c6.5099974915262060835892.jpg")
	embed.add_field(name = "Membre qui s'est pris le marteau en pleine tronche", value = user.name)
	embed.add_field(name = "Raison", value = reason, inline = False)
	embed.add_field(name = "Invoker", value = ctx.author.name)
	embed.set_footer(text = random.choice(list6))
	await ctx.send(embed = embed)