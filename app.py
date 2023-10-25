from threading import Thread
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
import telebot

app = Flask(__name__)
CORS(app)  # Enable CORS on all routes
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable CORS for SocketIO

bot = telebot.TeleBot("")

is_bot_polling_started = False  # Flag to check if bot polling has started


@app.route('/')
def index():
    return render_template('index.html')


@bot.message_handler(content_types=['text', 'photo'])
def forward_message(message):
    if message.content_type == 'text':
        socketio.emit('new_message', {'type': 'text', 'data': message.text})
    elif message.content_type == 'photo':
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        socketio.emit('new_message', {'type': 'photo', 'data': 'image.jpg'})


@socketio.on('connect')
def connect():
    global is_bot_polling_started
    if not is_bot_polling_started:
        is_bot_polling_started = True
        thread = Thread(target=bot.polling, kwargs={'none_stop': True})
        thread.start()


if __name__ == '__main__':
    if not is_bot_polling_started:
        is_bot_polling_started = True
        thread = Thread(target=bot.polling, kwargs={'none_stop': True})
        thread.start()
    socketio.run(app, debug=True)
