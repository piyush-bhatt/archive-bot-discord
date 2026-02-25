import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from config import load_config, save_config
from archiver import archive_thread_to_text
from utils import extract_date
from keep_alive import keep_alive

# ---------------- ENV VARIABLES ----------------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ---------------- WEB SERVER TO KEEP BOT ALIVE ----------------
keep_alive()

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- DAILY AUTO-ARCHIVE ----------------
#TODO: change to 24 after successful testing
@tasks.loop(minutes=5)
async def daily_archive():
    print("Running daily archive...")
    config = load_config()
    today = datetime.now().date()

    for guild_id_str, channels in config.items():
        guild = bot.get_guild(int(guild_id_str))
        if not guild:
            continue

        forum_channel = guild.get_channel(int(channels["forum"]))
        archive_channel = guild.get_channel(int(channels["archive"]))
        if not forum_channel or not archive_channel:
            continue

        for thread in forum_channel.threads:
            event_date = extract_date(thread.name)
            if event_date and event_date < today:
                await archive_thread_to_text(thread, archive_channel)
            elif not event_date:
                print(f"Skipping (no valid date): {thread.name}")

# ---------------- MANUAL ARCHIVE COMMAND ----------------
@bot.command(name="archive")
async def archive_command(ctx):
    config = load_config().get(str(ctx.guild.id))
    if not config:
        await ctx.send("Bot not set up for this server. Use `!setupArchiveBot <forum_channel_id> <archive_channel_id>` first.")
        return

    archive_channel = ctx.guild.get_channel(int(config["archive"]))

    if isinstance(ctx.channel, discord.Thread):
        await archive_thread_to_text(ctx.channel, archive_channel)
    else:
        await ctx.send("Use this command inside an event thread.")

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

# ---------------- ON READY ----------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not daily_archive.is_running():
        daily_archive.start()

# ---------------- RUN BOT ----------------
bot.run(TOKEN)
