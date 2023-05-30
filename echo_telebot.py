import telebot
from config import bot_token


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Готов тебя дразнить! Напиши, что-нибудь.')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, message.text + '🤡')


bot.polling(none_stop=True, interval=0)
