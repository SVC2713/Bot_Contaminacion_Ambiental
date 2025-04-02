import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def Tres_R(ctx):
    await ctx.send("Esta es una lista de que cosas puedes hacer, en base a las Tres R, con objetos que tienes en casa. Puedes usar los comandos: Reciclar, Reutilizar y Reducir")

@bot.command()
async def Reciclar(ctx):
    await ctx.send("Envases de plástico como botellas - Bolsas de plástico - Tetrabricks de leche y jugo - Latas de aluminio - Envases de papel y cartón como las cajas de cereales o zapatos - Aparatos electrónicos - Periódicos y revistas")
    await ctx.send("Si quieres saber qué es reciclar puedes usar el comando: info_reciclar")

@bot.command()
async def info_reciclar(ctx):
    await ctx.send("Es el proceso de transformar materiales usados en nuevos productos")

@bot.command()
async def Reutilizar(ctx):
    await ctx.send("Portavasos nuevos - Guarda los corchos - Periódicos viejos para limpiar ventanas - Macetas ecológicas")
    await ctx.send("Si quieres saber qué es reutilizar puedes usar el comando: info_reutilizar")

@bot.command()
async def info_reutilizar(ctx):
    await ctx.send("Es darle a un objeto o material una segunda vida, usándolo para el mismo propósito o para uno diferente, en lugar de desecharlo. ")

@bot.command()
async def Reducir(ctx):
    await ctx.send("El consumo de energía - El consumo de agua - El consumo del papel - El consumo de plástico")
    await ctx.send("Si quieres saber qué es reducir puedes usar el comando: info_reducir")

@bot.command()
async def info_reducir(ctx):
    await ctx.send("Reducir significa consumir menos, lo que ayuda a cuidar el medio ambiente. ")
