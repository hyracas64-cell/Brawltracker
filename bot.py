import discord
import os

# intents obligatoires
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("pong 🏓")

# récup du token depuis Render (Environment)
TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("❌ TOKEN MANQUANT")
else:
    client.run(TOKEN)
