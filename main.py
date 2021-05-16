### AlexIA Discord bot Python File ###
### DO NOT EDIT, DELETE, COPY THIS FILE WITHOUT THE CREATOR'S APPROBATION ###
import discord
from discord.ext import commands, tasks
import random
import time

status = ["$alexhelp",
		"Résous les problèmes dans la boîte aux lettres du staff",
		"Attrape les admins avec $catchadmin",
		"Lance des $couille sur #chatbox"]

bot = commands.Bot(command_prefix = "!", description = "Official bot from Solaris Server and his creator Asura")
list6= ["Pourquoi tu lis ca, ca sert a rien en fait !", "Qu'est ce qui est jaune et qui attend ?",
			"Tu te fais tellement chier que ca que tu lis ca mec ?",
			"Qui cherche la guerre finit par l'avoir. C'est logique non ?",
			"Qui cherche trouve (fin ca dépend des fois)",
			"Respecte les modos et les admins, c'est dans la liste bg !",
			"Arrête de lire ca et continue ta vie...",
			"Donc si je résume tas vraiment que ca a faire de ta vie",
			"Oh et merde j'abandonne."]

# MISE A JOUR V9 :


@bot.command()
async def session(ctx):
	await ctx.send("**&Natsuu est connecté sous l'AmID suivant : natsuu@theohxx.py")

# EVENTS :
@bot.event
async def on_ready():
	print('Natsuu bot (DO NOT EDIT THIS SCRIPT ! @theohxx)')
	print("* Connecting to server")
	print("* Looking for host")
	print("* Logging in servers")
	print("* Bot activation...")
	print("[-] VERIFYING TOKEN")
	print("[V] TOKEN OK")
	statusnpd.start()

"""@bot.event
async def on_message(message):
	if message.content == "Bonjour":
		await message.channel.send("Bonjour à toi :3")
	else:
		pass

@bot.event
async def on_message(message):
	if message.content == "Enculé":
		await message.channel.send(":O Les gros mots ici la !")
	else:
		pass

@bot.event
async def on_message(message):
	if message.content == "natsuu est le meilleur bot que j'ai fait, je l'aime ^^":
		await message.channel.send("Je t'aime aussi <3")
	else:
		pass

"""

# COMMANDES ------------------------------------------
@bot.command()
async def s(ctx):
	ssay=input("&Natsuu: Qu'est-ce que je dois dire ? ")
	print("&Natsuu: C'est carré!")
	await ctx.send(ssay)

@bot.command()
async def invite(ctx):
	await ctx.send("**L'invitation pour inviter tes potes est https://discord.gg/KBeY9jgQSm**")

@bot.command()
async def pldg(ctx, user):
	await ctx.send(f"**Picture loading... (from {user}**")

@bot.command()
async def appel(ctx, user, *, ou):
	await ctx.send(f"__**{user} tu es demandé dans {ou} !! Immédiatement !**__")


@bot.command()
async def snake(ctx):
	await ctx.send("...")
	await ctx.send("Je suis désolé, mon moteur rencontre un petit problème actuellement...")
	await ctx.send("```[E] Unknown error```")


@bot.command()
async def prejooj(ctx, user):
	await ctx.send(f"Bravo, tu as **prejooj** {user} avec élégance")

@bot.event
async def on_member_join(member):
	channel = member.guild

@bot.command()
async def bisou(ctx, user):
	await ctx.send(f"**Natsuu s'approche de {user} et lui fait un gros 'smack'**")

#TASKS HERE
@tasks.loop(seconds = 5)
async def statusnpd():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.dnd, activity = game)

# Commandes relatives au status : (voir avec #TASKS HERE)
@bot.command()
async def interval_state(ctx, secondes = 40):
	statusnpd.change_interval(seconds = secondes)

# OTHER
@bot.command()
async def lovewith(ctx):
  await ctx.send("**Le seul que j'aime est mon createur,** <@213713606045335552>  :3")

@bot.command()
async def lovestory(ctx, user1, user2):
  await ctx.send(f"**C'est le debut d'une belle et douce histoire de _love_ entre {user1} et {user2}...**")
  
@bot.command()
async def sacrifice(ctx, user):
  await ctx.send(f"**Natsuu kidnappe {user} et le place dans sa voiture [00.29]**")
  await ctx.send(f"**Natsuu endort {user} et l'attache sur l'hotel [01.31]**")
  await ctx.send("__Natsuu sort son couteau et le desinfecte__ [01.49]")
  await ctx.send(f"**Natsuu sacrifie {user} au dieu createur <@213713606045335552> sur la place publique.**")
  
@bot.command()
async def taab(ctx, user):
  await ctx.send(f"**Natsuu sort son couteau auparavant desinfecté et poignarde {user}**")

@bot.command()
async def staff(ctx):
  await ctx.send("❗ **Un <@714458539866980392> est demande dans ce salon d'urgence.** _(logcall:emergency-report)_") 
  
@bot.command()
async def sos(ctx):
  await ctx.send("❗ **<@213713606045335552>, tu es demande ici !**")
  
@bot.command()
async def requestcmd(ctx, title, *,reason):
	await ctx.send(f"La commande **{title}** avec la description **{reason}** a bien été ajoutée à la liste d'attente (<@213713606045335552>)")

@bot.command()
async def report(ctx, user, *, reason):
  await ctx.send(f"✅ **Le report pour {user} a bien ete enregistre. Description :**")
  await ctx.send(f"_{reason}_")
  await ctx.send("** Un <@714458539866980392> pour traiter cette demande s'il vous plait.** _(logcall:user-report_")

@bot.command()
async def oof(ctx, user):
	await ctx.send(f"**Oof** {user} s'en prend plein la geule")

@bot.command()
async def shell(ctx, *, content):
	await ctx.send("**</> - N:/System/shell**")
	await ctx.send("```Shell opened successfully```")
	await ctx.send(f"```$ {content}```")

@bot.command()
async def approved(ctx, ids):
	await ctx.send("**</> MESSAGE SYSTEME**")
	await ctx.send(f"```* La commande ayant pour numéro {ids} a bien été approuvée par <@admin>```")

@bot.command()
async def cmdready(ctx, title):
	await ctx.send("**</> MESSAGE SYSTEME**")
	await ctx.send(f"```* La commande ayant pour nom {title} a été ajoutée à la liste de commandes```")

@bot.command()
async def shlogout(ctx, user, passwd, argument):
	await ctx.send("**</> - N:/System/shell - Logout.command**")
	await ctx.send(f"```$ logout {user} {passwd} {argument}```")
	await ctx.send("```* Logout success. [OK]```")

@bot.command()
async def stop(ctx, user):
	await ctx.send(f"**STOP ! On arrête ici {user} ! Sinon ca va mal se passer...**")

@bot.command()
async def addlibrary(ctx, *, title):
	await ctx.send(f"```@+SYSTEM - The command named {title} has been added to bot library.```")

@bot.command()
async def shellauth(ctx, user, passwd):
	await ctx.send("**</> - N:/System/shell - Auth.command**")
	await ctx.send(f"```$ authentification {user}...```")
	await ctx.send("```* Authentification denied```")
	await ctx.send("~~BAHAHAHA DANS TON ***~~")

@bot.command()
async def pot(ctx, user):
	await ctx.send(f"**Natsuu voit le pot de fleurs (?) arriver en plein dans la tronche à {user}**")

@bot.command()
async def cours_saphir(ctx):
  await ctx.send("Le cours actuel du Saphir est de **109 Cr**")

@bot.command()
async def cours_pomme(ctx):
  await ctx.send("Le cours actuel de la pomme est de **1.9 Cr la piece**")

@bot.command()
async def divorce(ctx, user1, user2, *, reason):
	await ctx.send(f"**__Malheureusement, nous célébrons (?)  le divorce de {user1} et {user2} pour la raison suivante :__** _{reason}_")

@bot.command()
async def pecho(ctx, user):
	await ctx.send(f"**HEYYY ! Quelqu'un veut pas pécho {user} la !")

@bot.command()
async def bzc(ctx):
	await ctx.send("Ah non ! Il n'y a que moi qui peux aller sous le lit avec <@213713606045335552>")

@bot.command()
async def jvocal(ctx, user, *, name):
	await ctx.send(f"**{user} a rejoint le vocal {name}. Le laissez pas tout seul, allez le rejoindre !**")

# Commandes d'animation - Killing et shot :
@bot.command()
async def killorto(ctx):
	await ctx.send("**← l'orthographe has quit** ($self_quit : _AIDEZ MOI ! Je suis dans un serveur de fou ! Bannez moi ces gens qui ne respectent pas l'orthographeeee ! Mais. C'est une blague ! Je n'existe plus !_)")

@bot.command()
async def addquote(ctx, user, *,text):
	await ctx.send(f"La quote pour {user} a été ajoutée avec succès :")
	await ctx.send(f"{user} : {text}")
	await ctx.send("**__Veuillez cliquer sur 'épingler le message' pour garder la quote en mémoire__**")

@bot.command()
async def theapaa(ctx, user):
	await ctx.send(f"{user} est morte sous les pizza à l'ananas...")

@bot.command()
async def killto(ctx, user : discord.User, *, reason, montant = "Aucun montant fourni", color = 0x4C95FF):
	embed = discord.Embed(title = "Contrat d'assassinat effectué !", description = "Après tant d'efforts... Nous y sommes arrivés...", color = 0x4C95FF)
	embed.set_author(name = "@IP.System")
	embed.add_field(name = "Membre enfin tué", value = user)
	embed.add_field(name = "Raison", value = reason)
	embed.add_field(name = "Invoker", value = ctx.author.name, inline = False)
	embed.add_field(name = "Montant de la prime", value = montant)
	embed.set_footer(text = "Contrat rempli avec succès.")
	await ctx.send(embed = embed)

@bot.command()
async def contrekill(ctx, user : discord.User,):
	embed = discord.Embed(title = "$Contrekill ! Tu n'as pas réussi à le tuer...", color = 0x4C95FF)
	embed.set_author(name = "@KillSystem")
	embed.add_field(name = "Membre ayant utilisé $kill", value = user)
	embed.add_field(name = "Membre non tué", value = ctx.author.name)
	await ctx.send(embed = embed)


#############################################################################################################################
# Commandes d'administration (ban, kick, warn, unban, bannedusrs)

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
async def fd4e(ctx, user):
	await ctx.send("**__La famille des 4 enculés est désormais réunie__**")
	await ctx.send("**Un triomphe d'applaudissement pour les quatres enculés**")

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

@bot.command()
async def updaterecap(ctx, date, version, sub, *, detail):
  embed = discord.Embed(title = f"Mise à jour du serveur réussie vers {version}", color = 0x00DB00)
  embed.set_author(name = f"{date}")
  embed.add_field(name = "DETAIL :", value = f"{detail}", inline = False)
  embed.set_footer(text = f"{sub}")
  await ctx.send(embed = embed)

@bot.command()
async def current_profile(ctx):
	print("==================================================")
	print("La liste des profils pour Natsuu est :")
	print("Maintenance, Travail, Non défini, Par défaut, Natsu_Online, Natsu_Busy")
	prfch=input("Quel profil est lié à Natsu ? :")
	prfdb=["Maintenance","Travai","Par défaut","Natsu_online","Natsu_Busy"]
	if prfch in prfdb:
		await ctx.send("**Natsuu est connecté sous le profil**", prfch)
	else:
		await ctx.send("**Natsuu est connecté sous un profil inconnu, non défini ou une erreur temporaire est survenue.")

@bot.command()
async def helpcmd(ctx):
	embed = discord.Embed(title = "Commandes disponibles", color = 0x00ECFF)
	embed.set_author(name = "@com.NAPTT.FamilyUpgrade - @!")
	embed.add_field(name = "Préfixe du bot @Natsuu :", value = "Prefix = _$_", inline = False)
	embed.add_field(name= "Préfixe du bot @Théaux :", value = "Prefix = _._", inline = False)
	embed.add_field(name = "Préfixe du bot @Pingbot:", value = "Prefix = _&_", inline = False)
	embed.add_field(name = "Préfixe du bot @AnnouncerBot", value = "Prefix = _%_", inline = False)
	embed.add_field(name = "Préfixe du bot @Teenradio", value = "Prefix = _t/_", inline = False)
	await ctx.send(embed = embed)

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
async def pon(ctx, *, commentaire):
  embed = discord.Embed(title = "Le bot est maintenant en ligne !", color = 0xEC9900)
  embed.set_author(name = "@Natsuu.IP/NetAdmin+  -  logcall = (natsuu.pwron)")
  embed.add_field(name = "DETAIL :", value = f"{commentaire}")
  embed.set_footer(text = "(c) 2021 - Natsuu bot by matteo from AMIKA Dev - Do not copy, edit, remove code.")
  await ctx.send(embed = embed)

def isOwner(ctx):
	return ctx.message.author.id == 213713606045335552

@bot.command()
async def anniv(ctx, user):
	await ctx.send(f"**Souhaitons à tous un bon anniversaire à** {user}")

@bot.command()
async def jeudutir(ctx):
	await ctx.send("**__Je déclare le Jeu du tir ouvert ! A vos marques, prêts, tirez !__**")

@bot.command()
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre).flatten()
	for message in messages:
		await message.delete()


@bot.command()
async def fellation(ctx, user):
	await ctx.send(f"**Natsuu s'approche de {user} et lui fait une grosse fellation**")

@bot.command()
async def banspam(ctx):
	await ctx.send("**← An user was banned** : $BAN ___On t'a prévenu plusieurs fois, le spam/flood n'est pas longtemps toléré !___ (Ban 1h00)")

@bot.command()
async def banhomophobie(ctx):
	await ctx.send("**← An user was banned** : $BAN ___Les homophobes ne sont pas les bienvenus sur notre réseau, reviens quand tu auras mûri.___ (Ban 8h00)")

@bot.command()
async def banpdeum(ctx, user):
	await ctx.send(f"**← {user} was banned** : $BAN ___Propos déplacés envers un utilisateur mineur, suivant le degré de gravité, les captures d'écrans pourront être fournies aux forces de l'ordre___ (Ban 24h00)")

@bot.command()
async def bannm(ctx, user, texte):
	await ctx.send(f"_{user} a banni {texte}_")

@bot.command()
async def banmenaces(ctx):
	await ctx.send("**← An user was banned** : $BAN ___Les menaces pour l'IRL ne sont absolument pas tolérées sur notre serveur___ (Ban 6h00)")

@bot.command()
async def banmoqph(ctx):
	await ctx.send("**← An user was banned** : $BAN ___Les utilisateurs faisant preuve de harcélement ou de moqueries sur le physique sont sévèrement sanctionnés___ (Ban 24h00)")

@bot.command()
async def bz(ctx, user1, user2):
	await ctx.send(f":o **C'est parti ! Natsuu pousse {user1} et {user2} sous la couverture et hop ! Ca batifole !**")

@bot.command()
async def kick_vc(ctx, message):
	await ctx.send(f"**← An user was kicked from voice channel** $KICK ___Utilisateur ejecté du salon vocal par {message.author} ___")

@bot.command()
async def kickpsd(ctx):
	await ctx.send("**←An user was kicked from server** : $KICK ___ Pseudo innaproprié après plusieurs avertissements et a plusieurs reprises. ___")

@bot.command()
async def bantchsrv(ctx, user):
	await ctx.send(f"**←An user was banned from server** ({user}) : $BAN ___ Interdiction totale de toucher aux paramètres du serveur sans autorisation. Tu as voulu jouer, tu as perdu.___ (Ban 72h00)")

@bot.command()
async def rglminvite(ctx):
	await ctx.send("**RAPPEL !** L'envoi d'invitations, l'autopromotion et la pub sont strictement interdits sur notre serveur")

@bot.command()
async def infonudes(ctx):
	await ctx.send("**RAPPEL !** L'échange de **nudes** (photos dénudées) est FORMELLEMENT INTERDIT sur notre serveur ! La prochaine fois, c'est kick ! Puis $ban.")

@bot.command()
async def rglmrespect(ctx):
	await ctx.send("**RAPPEL !** : Tout le monde doit être ici. TU dois respecter et tu dois être respecté.")

@bot.command()
async def banporno(ctx):
	await ctx.send("**← An user was banned** : $BAN ___L'échange de vidéos/photos ou liens porno est formellement interdit et sanctionné. (Ban 5h00)___")

@bot.command()
async def giveop(ctx, user : discord.User, *, reason = "Aucun motif donné (Facultatif)"):
	reason = " ".join(reason)
	embed = discord.Embed(title = "**(+) An user was given the -+OP- role** _(logcall : OP_add_role.action)")

@bot.command()
async def couille(ctx):
	await ctx.send("Une **couille** sauvage apparaît !")

@bot.command()
async def catchcouille(ctx):
	await ctx.send("Tu as attrapé les couilles !")

@bot.command()
@commands.check(isOwner)
async def private(ctx):
	await ctx.send("Cette commande ne peut être activée que par le propriétaire du serveur.")


@bot.command()
async def actvty(ctx, user, *,reason):
	await ctx.send(f"{user} _à mis a jour son activité :_ **{reason}**")

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

#####################################################################################################################################

# Commandes d'animation :
  
@bot.command()
async def bouquet(ctx, user):
  await ctx.send(f"{user} envoie son bouquet de fleurs sur cette room ! **$catchflwrs** pour l'attraper en vol")
  
@bot.command()
async def catchflwrs(ctx, user):
  await ctx.send(f"**Bravo !** Tu as réussi à attraper le bouquet de fleurs de {user}")

@bot.command()
async def catch(ctx):
  await ctx.send("**Whoops! y'a rien en vol pour l'instant, dommage**")
  
@bot.command()
async def mpoubelle(ctx):
  await ctx.send("🎵 **Qui est l'enc<3le qui a renverse ma poubelle wooh oh ooh !**")

@bot.command()
async def observe(ctx):
  await ctx.send("_J'observe la scene, un paquet de pop corn a la main..._ Mmmh interessant...")
  
@bot.command()
async def cold(ctx):
  await ctx.send("❄ **Brrr! Il fait froid !**")
  
@bot.command()
async def slc(ctx):
  await ctx.send("**_Salut les chakals !_**")

@bot.command()
async def sohot(ctx):
  await ctx.send(" 😏 _Ca commence a devenir hot par ici!_")
  
@bot.command()
async def alrtmrdr(ctx, user):
  await ctx.send(f"‼ PIN PON ! **_ ALERTE EMMERDEUR !_** __Vite ! {user} est arrivé @here __")

@bot.command()
async def bonjour(ctx):
	await ctx.send("Bonjour à tous !")

@bot.command()
async def payer(ctx):
	await ctx.send("**__Pour payer quelqu'un,__** (marketplace ou autre), tape -commande en cours de chargement- et vire la monnaie (virtuelle) de ton compte a celui de l'autre.")

@bot.command()
async def wod(ctx):
	await ctx.send("**__World Of Darknet__** est un jeu gratuit (pour l'instant :P ). En développement par les administrateurs et des volontaires. Pour rejoindre la version minimaliste de WoD, rends toi dans le salon #🔔-annonces et clique sur l'invitation. Pour devenir volontaire de développement, rends toi dans les PV du propriétaire.")

# - COMMANDES D'AIDE
@bot.command()
async def alexhelp(ctx):
	await ctx.send("Pour retrouver l'aide complète, **rendez vous sur le site de Solaris**")
	await ctx.send("Ou contactez le développeur du bot _Adresse mail indisponible pour le moment_")


@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
async def chinese(ctx, *text):
	chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
			chineseText.append(" ")
			await ctx.send("".join(chineseText))

@bot.command()
async def jeu(ctx):
	await ctx.send("Vous pouvez jouer à un jeu ici ! Par exemple, testez le nouveau jeu Roulette ! En tapant **$roulette** ! D'autres jeux sont en cours d'ajout, on vous le fera savoir bientôt !")

@bot.command()
async def roulette(ctx):
	await ctx.send("ATTENTION ATTENTION ! Vous avez démarré le jeu Roulette !")
	await ctx.send("Le jeu de la Roulette va commencer dans 15.0 secondes. Tenez vous prêts !")

	players = []
	def check(message):
		return message.channel == ctx.message.channel and message.author not in players and message

	try:
		while True:
			participation = await bot.wait_for('message', timeout = 15, check = check)
			players.append(participation.author)
			print("Nouveau player dans le jeu $Roulette !")
			print(participation)
			await ctx.send("**{participation.author.name}** participe au tirage de la roulette ! Le tirage va commencer... Envoie \"moi\" dans cette room pour participer !")
	except: #Timeout
		print("Protocole de tirage en démarrage...")
	gagner = ("ban", "kick", "role personnel", "mute", "gage")

	await ctx.send("Le tirage va commencer dans 3 (countdown lol !)")
	await asyncio.sleep(1)
	await ctx.send("2...")
	await asyncio.sleep(1)
	await ctx.send("1...")
	await asyncio.sleep(1)
	loser = random.choice(players)
	price = random.choice(gagner)
	await ctx.send(f"La personne qui a gagné ce jeu et un {price} est...")
	await asyncio.sleep(1)
	await ctx.send("**" + loser.name + "**" + " !")


@bot.command()
async def trivia(ctx):
	await ctx.send("Activer/Desactiver les **Services en ligne Trivia** pour votre compte WoD")
	message = await ctx.send("Pour activer Trivia, faites ✅ . Pour désactiver Trivia, faites : ❌")
	await message.add_reaction("✅")
	await message.add_reaction("❌")

	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

	reaction, user = await bot.wait_for("reaction_add", timeout = 15, check = checkEmoji)
	if reaction.emoji == "✅":
		await ctx.send("✅ **Tes services en ligne Trivia ont été activés avec succès**")
	else:
		await ctx.send("❌ **Tes services en ligne Trivia ont bien été désactivés, conformément à ta demande.**")

@bot.command()
async def catchadmin(ctx, user):
	await ctx.send(f"Natsuu attrape {user} et le donne en sacrifice au dieu des miaou")

@bot.command()
async def mariage(ctx, user, user2):
	await ctx.send(f"_Célébrons tous le mariage de {user} avec {user2} Allez ! On jette des fleurs_")

@bot.command()
async def trimariage(ctx, user, user2, user3, user4, user5):
	await ctx.send(f"Célébrons le mariage de {user}, {user2}, {user3}, {user4}, {user5}")

@bot.command()
async def gn(ctx):
	await ctx.send(f"@here , _", ctx.author.name," vous souhaite une bonne nuit :)_")

@bot.command()
async def vodka(ctx, user):
	await ctx.send(f"**Natsuu** sert un verre de vodka bien frais à {user}")

@bot.command()
async def pizzaananas(ctx, user):
	await ctx.send(f"**Ding dong ! La pizza à l'ananas pour {user} est arrivée !**")

@bot.command()
async def pizza(ctx):
	await ctx.send("**Ding dong !** _Quelqu'un a commandé une pizza ?_")

@bot.command()
async def matchready(ctx):
	await ctx.send(f"_**{message.author} est prêt pourle matchmaking ! Invitez le !**_")

@bot.command()
async def away(ctx, user):
	await ctx.send(f"_{user} est désormais défini comme absent._")

@bot.command()
async def oqp(ctx, user):
	await ctx.send(f"_{user} est désormais défini comme occupé._ (DO NOT DISTURB !)")

@bot.command()
async def sell(ctx, user, prix, *, description):
	await ctx.send(f"{user} a bien été vendu(e) sur le **Market place** pour {prix}, sa description : {description}")

@bot.command()
async def buy(ctx, user, prix):
	await ctx.send(f"{user} a été acheté(e) pour {prix} auhjourd'hui.")

@bot.command()
async def temps(ctx):
	await ctx.send("Je suis actuellement à **37,4°c**")

@bot.command()
async def celm(ctx):
	await ctx.send("Je suis **love** de mon créateur <@213713606045335552> ^^")

@bot.command()
async def imback(ctx, user):
	await ctx.send(f"_{user} est désormais de retour parmi nous !_")

@bot.command()
async def statut(ctx):
	await ctx.send("_Désolé ! Cette commande est actuellement en développement..._")

@bot.command()
async def capote(ctx, user):
	await ctx.send(f"**Alex** offre une capote à {user}")

@bot.command()
async def tpn(ctx, user):
	await ctx.send(f"**T'ES PAS NET BAPTISTE !({user})**")

@bot.command()
async def dtc(ctx):
	await ctx.send("Boum boum, dans ton cul !")

#######################################################################################################

# FAIRY TAIL FAMILY UPDATE COMMANDS (Erased : 25/12/2021 15:00 (GMT+01)) :

@bot.command()
async def happy(ctx):
	await ctx.send("**Happy** : _Ouais ?!_")

@bot.command()
async def lucy(ctx):
	await ctx.send("**Lucy** : _Lucy, la meilleure constellationniste du monde pour vous servir !_")
	await ctx.send("**Happy** : (discrètement) _Elle fricote avec loki, hu hu hu..._")
	await ctx.send("**Lucy** : _Tu vas la fermer saleté de chat !!_")

@bot.command()
async def erza(ctx):
	await ctx.send("**Erza** : _Je suis la gardienne de la paix dans ce bas-monde !_")
	await ctx.send("**Natsu** : _J'vais te cramer ta sale tronche !_")
	await ctx.send("**Grey** : _Essaie un peu gros naze !_")
	await ctx.send("**Erza** : 💢 _LA FEERMMEEEEEE !_ (jette un livre en métal sur les deux cons)")
	await ctx.Send("**Grey&Natsu** : _C'est nous les deux cons...?_ (tristes)")

@bot.command()
async def grey(ctx):
	await ctx.send("**Grey** : _Salut._")
	await ctx.send("**Erza&Lucy** : _RHABILLE TOI TOUT DE SUITE !_")
	await ctx.send("**Grey** : _WAAAAH !_")

@bot.command()
async def natsu(ctx):
	await ctx.send("**Natsu** : _T'es qui, toi ?_")
	await ctx.send("**Happy** : _La délicatesse..._")

@bot.command()
async def fthelp(ctx):
	await ctx.send("**__ PANEL DES COMMANDES Update Fairy Tail :__**")
	await ctx.send("**Suppression des commandes le 28 décembre 2021 à 15h00 (GMT+01)**")
	await ctx.Send("__Présentation__ : $natsu $grey $lucy $erza $happy")
	await ctx.send("_(d'autres commandes arrivent bientôt...)_")
















# Commandes relatives à la gestion des messages :

""" Unactive command :
@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	await message.channel.send(f"> {message.content}\n{message.author}")
	await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
	await message.channel.send(f"**Le message de {message.author} a été supprimé \n> {message.content}**")


@bot.event
async def on_message_edit(before, after):
	await before.channel.send(f"{before.author} a édité son propre message $mdr :\n**Message précédent** : {before.content}\n**Message après editing** -> {after.content}")
"""


bot.run("ODMyNTg0NDY4NDcyMTM1NzQw.YHl6tQ.uSkHJ0eraTqMwegWaMrpZ5j9wis")
