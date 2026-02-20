import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# ========================================================
# 1. SERVIDOR WEB PARA MANTENERLO DESPIERTO 24/7
# ========================================================
app = Flask('')

@app.route('/')
def home():
    return "¡Bot en línea! El servidor de respaldo está funcionando."

def run():
    # Render usa puertos dinámicos, el 8080 es ideal para el plan Free
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    """Inicia un servidor web en segundo plano para evitar que Render suspenda el bot."""
    t = Thread(target=run)
    t.start()

# ========================================================
# 2. CONFIGURACIÓN DEL BOT Y COMANDOS DE FOTOS
# ========================================================
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'-----------------------------------')
    print(f'Conectado exitosamente como: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'-----------------------------------')

# COMANDO PARA LA FOTO 1
@bot.command()
async def foto1(ctx):
    try:
        # Asegúrate de haber subido '1.jpg' a la carpeta principal de GitHub
        await ctx.send("Aquí tienes la imagen 1:", file=discord.File('1.jpg'))
    except Exception as e:
        await ctx.send(f"No pude enviar la foto 1. Error: {e}")

# COMANDO PARA LA FOTO 2
@bot.command()
async def foto2(ctx):
    try:
        # Asegúrate de haber subido '2.jpg' a la carpeta principal de GitHub
        await ctx.send("Aquí tienes la imagen 2:", file=discord.File('2.jpg'))
    except Exception as e:
        await ctx.send(f"No pude enviar la foto 2. Error: {e}")

# COMANDO DE PRUEBA RÁPIDA
@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! El bot está funcionando perfectamente en Render.')

# ========================================================
# 3. ARRANQUE DEL SISTEMA
# ========================================================
if __name__ == "__main__":
    # Activamos el "seguro de vida" del bot
    keep_alive()
    
    # IMPORTANTE: Configura 'DISCORD_TOKEN' en la pestaña Environment de Render
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("ERROR CRÍTICO: No se detectó la variable de entorno DISCORD_TOKEN.")
