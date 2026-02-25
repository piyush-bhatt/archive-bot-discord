async def archive_thread_to_text(thread, archive_channel):
    try:
        # Rename, lock, and archive original thread
        if not thread.name.startswith("[ARCHIVED]"):
            new_name = f"[ARCHIVED] {thread.name}"
            await thread.edit(name=new_name, locked=True, archived=True)
            print(f"Locked, archived, and renamed thread: {new_name}")

        # Post header in archive channel with link to original
        thread_link = f"https://discord.com/channels/{thread.guild.id}/{thread.id}"
        header = f"**{thread.name}**\nArchived from {thread.parent.name}\n[View Original Thread]({thread_link})"
        await archive_channel.send(header)

        print(f"Archived thread: {thread.name}")

    except Exception as e:
        print(f"Failed to archive thread {thread.name}: {e}")
