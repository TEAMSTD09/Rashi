import requests
from MukeshAPI import api
from pyrogram import filters, Client
from pyrogram.enums import ChatAction
from nexichat import nexichat as app

conversation_cache = {}

@Client.on_message(
    (filters.command(["ai", "ask", "chatgpt"]) | filters.regex(r"^\.ai |^\.ask ") | filters.text),
    group=-9
)
async def gemini_handler(client, message):
    user_id = message.from_user.id
    user_input = None

    if message.text.startswith(("/", ".")) and len(message.command) > 1:
        user_input = " ".join(message.command[1:])
    elif message.text.startswith(f"@{client.me.username}"):
        user_input = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    elif message.reply_to_message and message.reply_to_message.text:
        if message.text.startswith(("/", ".") + tuple([f"/{command}" for command in ["ai", "ask", "chatgpt"]])) or \
           message.text.startswith(f"@{client.me.username}"):
            user_input = message.reply_to_message.text
    if message.reply_to_message and len(message.command) > 1:
        user_input = " ".join(message.command[1:])
    elif message.reply_to_message and message.text.startswith(f"@{client.me.username}"):
        split_text = message.text.split(" ", 1)
        if len(split_text) > 1:
            user_input = split_text[1]
    if not user_input:
        if message.text.startswith(("/", ".", f"@{client.me.username}")):
            await message.reply_text(f"ᴇxᴀᴍᴘʟᴇ :- `/ask who are you baby` or `@{client.me.username} how are you`")
        return

    if user_id not in conversation_cache:
        conversation_cache[user_id] = []

    conversation_history = conversation_cache[user_id]
    prompt = "This is the conversation between the user and AI(your old replies) So read the old chats and understand which topic we both were talking about and the last message after that is the latest message of this conversion(meansI have a new question for you), just reply for last message(means new message):\n\n"
    for user_msg, ai_reply in conversation_history[-20:]:
        prompt += f"User: {user_msg}\nAI: {ai_reply}\n\n"
    prompt += f"User: {user_input}\nAI:"

    try:
        response = api.gemini(prompt)
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        result = response.get("results")
        if result:
            conversation_cache[user_id].append((user_input, result))
            if len(conversation_cache[user_id]) > 20:
                conversation_cache[user_id].pop(0)
            await message.reply_text(result, quote=True)
            return
    except:
        pass

    try:
        base_url = "https://chatwithai.codesearch.workers.dev/?chat="
        response = requests.get(base_url + prompt)
        if response.status_code == 200:
            json_response = response.json()
            if "data" in json_response:
                reply_text = json_response["data"].strip()
                if reply_text:
                    conversation_cache[user_id].append((user_input, reply_text))
                    if len(conversation_cache[user_id]) > 15:
                        conversation_cache[user_id].pop(0)
                    await message.reply_text(reply_text, quote=True)
                    return
        await message.reply_text("**Both Gemini and Chat with AI are currently unavailable**")
    except:
        await message.reply_text("**Chatgpt is currently dead. Try again later.**")
