import discord
import os

print("BOT STARTING...")

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("❌ TOKEN MANQUANT")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("pong")

client.run(TOKEN)
import time

try:
except Exception as e:
    print(e)
    time.sleep(10)
