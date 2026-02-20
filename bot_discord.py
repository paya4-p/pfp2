import discord
import os

# --- CONFIGURACIÓN ---
TOKEN = 'MTQ3NDE1NjA4MjAwNzExNzk4OA.GExla-.aJdGcc2S2lO5KZQi6xd_H0UryBiIXYKC6KQeK0'
FOTO_A = '1.jpg' 
FOTO_B = '2.jpg'
# ---------------------

class DiagnosticBot(discord.Client):
    async def on_ready(self):
        print(f'✅ Conectado como {self.user}')
        
        # 1. Ver en qué carpeta está trabajando el bot realmente
        ruta_actual = os.getcwd()
        print(f'📍 El bot está buscando en la carpeta: {ruta_actual}')
        
        # 2. Listar TODOS los archivos que hay en esa carpeta
        archivos = os.listdir('.')
        print(f'📁 Archivos encontrados en esta carpeta: {archivos}')
        
        # 3. Intentar abrir la foto A
        if os.path.exists(FOTO_A):
            print(f'✔️ ¡Archivo {FOTO_A} encontrado! Intentando subir...')
            try:
                with open(FOTO_A, 'rb') as f:
                    await self.user.edit(avatar=f.read())
                print("✨ ¡Avatar cambiado con éxito!")
            except Exception as e:
                print(f"❌ Error al subir: {e}")
        else:
            print(f'❌ El archivo "{FOTO_A}" NO existe en esta carpeta.')
            print(f'💡 Sugerencia: Revisa si en la lista de arriba el nombre aparece distinto.')

intents = discord.Intents.default()
client = DiagnosticBot(intents=intents)
client.run(TOKEN)