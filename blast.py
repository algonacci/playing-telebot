import telebot

# Step 2: Initialize the bot with your token
bot_token = ''
bot = telebot.TeleBot(bot_token)

# Step 3: Find the group chat ID (you can print updates from bot to find this)
group_chat_id = '-4029522008'

# Step 4 and 5: Initialize bot and send message
bot.send_message(group_chat_id, 'AMIN AJA DULU!')

# Polling loop to keep the bot running
# bot.polling()
print("DONE")
