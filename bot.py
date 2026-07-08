import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

# -------- CONFIG --------
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# -------- JSON --------
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# -------- READY --------
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Connecté : {bot.user}")

# -------- COMMANDES --------

@bot.tree.command(name="save", description="Ajouter un joueur")
async def save(interaction: discord.Interaction, tag: str, name: str, trophies: int):
    data = load_data()

    data[tag] = {
        "name": name,
        "trophies": trophies
    }

    save_data(data)

    await interaction.response.send_message(f"✅ {name} ajouté !")

@bot.tree.command(name="player", description="Voir un joueur")
async def player(interaction: discord.Interaction, tag: str):
    data = load_data()

    if tag in data:
        p = data[tag]

        embed = discord.Embed(title="📊 Stats Joueur", color=0x00ff00)
        embed.add_field(name="👤 Nom", value=p['name'], inline=False)
        embed.add_field(name="🏆 Trophées", value=p['trophies'], inline=False)

        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("❌ Joueur introuvable")

@bot.tree.command(name="list", description="Liste des joueurs")
async def list_players(interaction: discord.Interaction):
    data = load_data()

    if not data:
        await interaction.response.send_message("❌ Aucun joueur")
        return

    msg = ""
    for tag, p in data.items():
        msg += f"{p['name']} ({tag}) - {p['trophies']}🏆\n"

    await interaction.response.send_message(msg)

# -------- RUN --------
bot.run(TOKEN)