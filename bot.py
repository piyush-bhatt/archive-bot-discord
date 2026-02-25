import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from config import load_config, save_config

# ---------------- ENV VARIABLES ----------------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- BOT SETUP COMMAND FOR SERVER ----------------
@bot.command(name="setupArchiveBot")
@commands.has_permissions(administrator=True)
async def setup(ctx, forum_channel_id: int, archive_channel_id: int):
    """
    Admin command: !setupArchiveBot <forum_channel_id> <archive_channel_id>
    """
    config = load_config()
    config[str(ctx.guild.id)] = {
        "forum": forum_channel_id,
        "archive": archive_channel_id
    }
    save_config(config)
    await ctx.send(f"ArchiveBot setup complete!\nForum channel ID: {forum_channel_id}\nArchive channel ID: {archive_channel_id}")

# ---------------- RUN BOT ----------------
bot.run(TOKEN)
