import telebot
import datetime

TOKEN = ''
tb = telebot.TeleBot(TOKEN)  # create a new Telegram Bot object

file_name = 'messages.txt'


@tb.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    text = message.text
    user_id = message.from_user.id
    username = message.from_user.username

    # Get the current timestamp
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message_info = f"{current_time} - Received message in group {chat_id} from {username} (User ID: {user_id}): {text}"

    # Write the message to the text file
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(message_info + '\n')

    print(message_info)


tb.polling()
