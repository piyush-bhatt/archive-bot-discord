# Archive bot discord

A Discord bot designed to manage event threads in Forum channels. It automatically identifies threads with past dates in their titles and moves them to an Archive channel, keeping your active events list clean.

## Features

*   **📅 Automatic Archiving**: Runs a daily check to find threads with dates that have passed.
*   **🧠 Smart Date Parsing**: Detects various date formats in thread titles (e.g., "Movie Night 25/12/2023", "Team Meeting 2024-01-15").
*   **🔒 Thread Locking**: Automatically locks and closes the original thread upon archiving.
*   **🔗 Cross-Linking**: Posts a summary in the archive channel with a link back to the original thread.
*   **⚡ Manual Commands**: Trigger archiving manually or configure the bot directly from Discord.

## How it Works

### Auto-Archive
The bot scans the configured Forum channel every 24 hours. If a thread title contains a date that is older than today, it gets archived.

### Manual Archive
You can also archive a thread immediately using a command.

## Setup & Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/piyush-bhatt/archive-bot-discord.git
    cd archive-bot-discord
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables**
    Create a `.env` file in the root directory and add your bot token:
    ```env
    DISCORD_TOKEN=your_discord_bot_token_here
    ```

4.  **Run the Bot**
    ```bash
    python bot.py
    ```

## Commands

*   `!setupArchiveBot <forum_channel_id> <archive_channel_id>`
    *   **Admin only**. Links a Forum channel to an Archive text channel for the current server.
*   `!archive`
    *   Can be used inside a thread to force an immediate archive.

## Hosting
The project includes a `keep_alive.py` script, making it ready for hosting on platforms that require a web server to stay active (like Render/Replit).
