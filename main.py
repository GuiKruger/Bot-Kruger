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

page1 = discord.Embed(
    title="🦋 | Portifólio", 
    description="Para conferir nossas artes use as reaçoes abaixo para se deslocar.", 
    colour=4250015
    )
page1.set_image(url="https://media.discordapp.net/attachments/859201102610956358/947507414972891146/unknown.png?width=810&height=360")
page1.set_footer(text="1/8")

page2 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page2.set_image(url="https://media.discordapp.net/attachments/929153410555596840/939533435725291560/5ea2adca-1b21-40a5-a3f0-7dde1c57eb15.png?width=1080&height=540")
page2.set_footer(text="2/8")


page3 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page3.set_image(url="https://media.discordapp.net/attachments/929153410555596840/934444785194893312/unknown.png?width=720&height=270")
page3.set_footer(text="3️/8")

page4 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page4.set_image(url="https://media.discordapp.net/attachments/929153410555596840/934445378219175956/unknown.png?width=1080&height=450")
page4.set_footer(text="4️/8")

page5 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page5.set_image(url="https://images-ext-1.discordapp.net/external/D76nt8pFN2RBA1YkhMLrHfXUWSPvAHwNvD3ZD5g3Mbs/%3Fwidth%3D1080%26height%3D450/https/media.discordapp.net/attachments/859201102610956358/944429142668116058/unknown.png?width=972&height=405")
page5.set_footer(text="5️/8")

page6 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page6.set_image(url="https://media.discordapp.net/attachments/859201102610956358/945503093263572992/unknown.png?width=810&height=360")
page6.set_footer(text="6️/8")

page7 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page7.set_image(url="https://media.discordapp.net/attachments/859201102610956358/944045460010704926/unknown.png?width=1080&height=450")
page7.set_footer(text="7️/8")

page8 = discord.Embed(
    title="🦋 | Portifólio",
    colour=4250015
    )
page8.set_image(url="https://media.discordapp.net/attachments/859201102610956358/944024645806485534/unknown.png?width=1080&height=450")
page8.set_footer(text="8️/8")

bot.portf_pages = [page1, page2, page3, page4, page5, page6, page7, page8]

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

#embeds
@bot.command()
async def embed1(ctx):
    embed = discord.Embed(
        title = "Portifólio - Kruger Design 🔹",
        description = f"**Portifólio**\nConfira alguns de nossos trabalhos para ter uma ideia do nosso produto final.\n \n**Como eu vejo?**\nSimples! digite `k.portif` em <#947553146509602917> após isso use as reações abaixo para se deslocar de uma embed para outra, cada embed tera uma arte diferente feita pela nossa equipe.",
        color = 4250015
    )
    embed.set_image(url="https://media.discordapp.net/attachments/859201102610956358/947507414972891146/unknown.png?width=810&height=360")
    await ctx.send(embed = embed)


#portifólio
@bot.command()
async def portif(ctx):
    print (f'"portifólio" usado por {ctx.author}')
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    current = 0
    await ctx.send(f"> <a:fogo_emoji:912122546525184082>||{ctx.author.mention}||")
    await ctx.message.delete()
    msg = await ctx.send(embed=bot.portf_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(bot.portf_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.portf_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.portf_pages[current])

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
    embed.add_field(name=f'💼 Nome do Discord',value=f'`{user.display_name}`', inline=False)
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
    print (f'server info usado pelo {ctx.author}!'),
    embed = discord.Embed(
        timestamp = ctx.message.created_at,
        colour = 16777215,
        description = f'Aqui estão algumas informações do server **{ctx.guild.name}**'
    )
    embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    embed.set_author(name='剣 Kruger Bot ☕', icon_url='https://media.discordapp.net/attachments/859201102610956358/915944247943901194/Perfil_Bot_Kruger.jpg?width=584&height=584'),
    embed.add_field(name=f'🌺 Name do Server',value=f'`{ctx.guild.name}`', inline=False)
    embed.add_field(name=f'📋 Descrição do Server',value=f'`{ctx.guild.description}`',inline=False)
    embed.add_field(name=f'🔮 Quantidade de Membros',value=f'`{ctx.guild.member_count}`',inline=False)
    embed.add_field(name=f'💻 ID do Server',value=f'`{ctx.guild.id}`',inline=False)
    embed.set_footer(text=f'Solicitado por {ctx.author}')
    
    #delet comando usado pelo user
    await ctx.message.delete()
    
    #menssagem para o user
    await ctx.send(f"<a:fogo_emoji:912122546525184082>||{ctx.author.mention}||")

    #add reações na msg
    await ctx.send(embed = embed)

#treino/sus

@bot.command()
async def visão_delas(ctx):
    print ("comando usado!")
    await ctx.send(f"> <a:fogo_emoji:912122546525184082> Não olha pra cima!")
    await ctx.author.send(f"https://media.discordapp.net/attachments/716824742946144277/901567412611207229/IMG_20211020_174132005_HDR.jpg?width=438&height=584")

#inicialização─╯
bot.run(token)