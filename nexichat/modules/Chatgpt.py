import requests
from MukeshAPI import api
from pyrogram import filters, Client
from pyrogram.enums import ChatAction
from nexichat import nexichat as app


@app.on_message((filters.command(["gemini", "ai", "ask", "chatgpt"]) | filters.text), group=7)
async def gemini_handler(client, message):
    user_input = None

    if message.text.startswith(f"@{client.me.username}"):
        user_input = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    elif (
        message.text.startswith(f"/gemini@{client.me.username}")
        and len(message.text.split(" ", 1)) > 1
    ):
        user_input = message.text.split(" ", 1)[1]
    elif message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    elif len(message.command) > 1:
        user_input = " ".join(message.command[1:])

    if not user_input:
        await message.reply_text("ᴇxᴀᴍᴘʟᴇ :- `/ask who is Narendra Modi` or `@chutiyapabot how are you`")
        return

    try:
        response = api.gemini(user_input)
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        result = response.get("results")
        if result:
            await message.reply_text(result, quote=True)
            return
    except:
        pass

    try:
        base_url = "https://chatwithai.codesearch.workers.dev/?chat="
        response = requests.get(base_url + user_input)
        if response.status_code == 200:
            json_response = response.json()
            if "data" in json_response:
                reply_text = json_response["data"].strip()
                if reply_text:
                    await message.reply_text(reply_text, quote=True)
                    return
        await message.reply_text("**Both Gemini and Chat with AI are currently unavailable**")
    except:
        await message.reply_text("**Chatgpt is currently dead. Try again later.**")
