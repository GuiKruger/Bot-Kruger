#import
import discord
from discord import activity
from discord import member
from discord import colour
from discord import asset
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv
import random
import asyncio


#carregar o arquivo .env
load_dotenv(find_dotenv())
prefixo = os.getenv('prefixo')
token = os.getenv('token')

bot = commands.Bot(command_prefix=prefixo, case_insensitive=True, help_command=None)

#Status do Bot
@bot.event
async def on_ready():
    activity = discord.Game(name='Jogo da Vida', type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('tamo on meu belo, com {0.user}' .format((bot)))


#╭─eventos

#Bem vindo
@bot.event
async def on_join(member):
    canal = bot.get_channel(902005614258057226)
    regras = bot.get_channel(901983087695626290)
    await canal.send(f"> <a:fogo_emoji:912122546525184082> Bem vindo a nossa vila nobre {member.author} não se esqueça de ler nossas {regras.mention}\n" "Se **divirta!**\n")



#Menção ao bot


#╭─commandos

#comando help
@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        colour = 16777215,
        timestamp = ctx.message.created_at,
        description = '𑁯**HELP**'
    )
    embed.set_author(name='剣 Kruger Bot ☕', icon_url='https://media.discordapp.net/attachments/859201102610956358/915944247943901194/Perfil_Bot_Kruger.jpg?width=584&height=584'),
    embed.set_image(url='https://media.discordapp.net/attachments/859201102610956358/915955654424936478/unknown.png')
    embed.add_field(name=f'Comandos:',value='```k.userinfo```\n' '```k.serverinfo```\n' '```k.perfil```\n',inline=False)

    #delet comando usado pelo user
    await ctx.message.delete()
    
    await ctx.send(embed = embed)
#comandos do bot

#plastico bolha
@bot.command()
async def plastico_bolha(ctx):
    print (f'"plastico bolha" usado por {ctx.author}')
    embed = discord.Embed(
        timestamp = ctx.message.created_at,
        color = 16777215,
        description = f"||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||\n" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||\n" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||\n" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||" "||ploc||",
    )

    await ctx.send(embed = embed)
    await ctx.send(f"<a:fogo_emoji:912122546525184082>||{ctx.author.mention}||")
    await ctx.message.delete()

#perfil
@bot.command()
async def perfil(ctx, user:discord.Member=None):
    print (f'""perfil" usado pelo {ctx.author}!')
    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
        if role.name != "@everyone":
            rlist.append(role.mention)
    b = ",".join(rlist)
    
    embed = discord.Embed(
        timestamp = ctx.message.created_at,
        colour = 16777215
    )
    embed.set_author(name=user.display_name, icon_url=user.avatar_url),
    embed.set_image(url='https://media.discordapp.net/attachments/859201102610956358/916340936517255208/unknown.png')
    embed.add_field(name=f'Name:',value=user.display_name,inline=False)
    embed.add_field(name=f'Cargos: ({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name=f'Cargo King:',value=user.top_role.mention, inline=False,)
    embed.set_footer(text="剣 Kruger Bot ☕", icon_url='https://media.discordapp.net/attachments/859201102610956358/915944247943901194/Perfil_Bot_Kruger.jpg?width=584&height=584')
    
    #delet comando usado pelo user
    await ctx.message.delete()
    
    msg = await ctx.send(embed = embed)
    
    #delete embed
    await asyncio.sleep(30)
    await msg.delete()


#user info
@bot.command()
async def userinfo(ctx, user:discord.Member=None):
    print (f'user info usado pelo {ctx.author}!')
    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
        if role.name != "@everyone":
            rlist.append(role.mention)
    b = ",".join(rlist)
    
    embed = discord.Embed(
        timestamp = ctx.message.created_at,
        colour = 16777215,
        description = f'Aqui estão algumas informações do user: **{user.display_name}**'
    )
    embed.set_author(name='剣 Kruger Bot ☕', icon_url='https://media.discordapp.net/attachments/859201102610956358/915944247943901194/Perfil_Bot_Kruger.jpg?width=584&height=584'),
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name=f'💼 Name do Discord',value=f'`{user.display_name}`', inline=False)
    embed.add_field(name=f'💻 ID do Discord',value=f'`{user.id}`',inline=False)
    embed.add_field(name=f'📆 Conta criada há',value=f'`{user.created_at}`',inline=False)
    embed.add_field(name=f'⏰ Ingressou em',value=f'`{user.joined_at}`',inline=False)
    embed.add_field(name=f'🤖 É um Bot?',value=f'`{user.bot}`',inline=False)
    embed.set_footer(text=f'Solicitado por {ctx.author}')
    
    #delet comando usado pelo user
    await ctx.message.delete()
    
    #menssagem para o user
    await ctx.send(f"<a:fogo_emoji:912122546525184082>||{ctx.author.mention}||")

    #add reações na msg
    await ctx.send(embed = embed)

#server info
@bot.command()
async def serverinfo(ctx):
    print (f'server info usado pelo {ctx.author}!')
    role_count = len(ctx.guild.roles)

    embed = discord.Embed(
        timestamp = ctx.message.created_at,
        colour = 16777215,
        description = f'Aqui estão algumas informações do **{ctx.guild.name}**'
    )
    embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    embed.set_author(name='剣 Kruger Bot ☕', icon_url='https://media.discordapp.net/attachments/859201102610956358/915944247943901194/Perfil_Bot_Kruger.jpg?width=584&height=584'),
    embed.add_field(name=f'💼 Name do Server',value=f'`{ctx.guild.name}`', inline=False)
    embed.add_field(name=f'⌛ Quantidade de Membros',value=f'`{ctx.guild.member_count}`',inline=False)    
    embed.add_field(name=f'💻 ID do Server',value=f'`{ctx.guild.id}`',inline=False)
    embed.set_footer(text=f'Solicitado por {ctx.author}')
    
    #delet comando usado pelo user
    await ctx.message.delete()
    
    #menssagem para o user
    await ctx.send(f"<a:fogo_emoji:912122546525184082>||{ctx.author.mention}||")

    #add reações na msg
    await ctx.send(embed = embed)

#comando ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(bot.latency + 1000)}ms")


#treino/sus

@bot.command()
async def visão_delas(ctx):
    print ("comando usado!")
    await ctx.send(f"> <a:fogo_emoji:912122546525184082> Não olha pra cima!")
    await ctx.author.send(f"https://media.discordapp.net/attachments/716824742946144277/901567412611207229/IMG_20211020_174132005_HDR.jpg?width=438&height=584")

@bot.command()
async def cx(ctx):
    mgs = ctx.send("Pegou o fogo man!")
    msg = await ctx.send(f"> 👻" "<a:fogo_emoji:912122546525184082>\n" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪" "🟪",)
    await msg.add_reaction("◀")
    await msg.add_reaction("▶")

#inicialização─╯
bot.run(token)