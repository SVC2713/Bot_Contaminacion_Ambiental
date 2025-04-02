import discord
import os, random
from discord.ext import commands
from Tres_R import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def presentacion(ctx):
    await ctx.send("Hola, soy un bot que te puede enseñar de la cotaminación ambiental, darte recomendaciones, y ayudarte a clasificar objetos con las Tres R")

@bot.command()
async def ayuda(ctx):
    await ctx.send("Comandos disponibles: recomendaciones_agua, recomendaciones_aire, recomendaciones_suelo, contaminacion_video, Tres_R, imagen")


@bot.command()
async def recomendaciones_agua(ctx):
    await ctx.send("NO botes la basura al mar")
    await ctx.send("Cierra la llave del grifo, para que no desperdicies el agua")

@bot.command()
async def recomendaciones_aire(ctx):
    await ctx.send("Si quieres ir a un lado cercano, puedes ir en bicicleta. No solo estás cuidando al medio ambiente, también cuidas tu salud")

@bot.command()
async def recomendaciones_suelo(ctx):
    await ctx.send("Separa la basura en los tachos de reciclaje")
    await ctx.send("Evita plásticos de un solo uso, opta por embalajes ecológicos y reutilizables. ")

@bot.command()
async def imagen(ctx):
    img_name = random.choice(os.listdir('Imagen'))
    with open(f'Imagen/{img_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def contaminacion_video(ctx):
    await ctx.send("https://www.youtube.com/watch?v=nvUqnpicSd0&t=50s")




bot.run("TOKEN")
