import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

# ---------------- ENV VARIABLES ----------------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.run(TOKEN)
