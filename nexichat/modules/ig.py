import requests
from pyrogram import filters
from nexichat import nexichat as app

@app.on_message(filters.command(["ig", "instagram"]))
async def download_instagram_content(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide the Instagram URL after the command.")
        return

    url = message.text.split()[1]
    if "instagram.com" not in url:
        await message.reply_text("Invalid Instagram URL. Please check and try again.")
        return

    processing_message = await message.reply_text("Processing...")

    api_url = f"https://insta-dl.hazex.workers.dev/?url={url}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        result = response.json()

        if result["error"]:
            await processing_message.edit("Failed to download. The content might not be available.")
            return

        data = result["result"]
        content_url = data["url"]
        caption = (
            f"**Type:** {data['extension']}\n"
            f"**Quality:** {data.get('quality', 'Unknown')}\n"
            f"**Size:** {data.get('formattedSize', 'Unknown')}\n"
        )

        await processing_message.delete()
        if data["isVideo"]:
            await message.reply_video(content_url, caption=caption)
        else:
            await message.reply_photo(content_url, caption=caption)

    except requests.exceptions.RequestException:
        await processing_message.edit("An error occurred while processing the request. Please try again.")
    except Exception as e:
        await processing_message.edit(f"An unexpected error occurred: {e}")
