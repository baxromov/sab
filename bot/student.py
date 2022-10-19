import telebot
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
token = "5684210743:AAF-xPETRw4fWxM5lheaFTUGTihbXJVUaN4"


bot = telebot.TeleBot(token)


@bot.message_handler(['start'])
def start(message):
    text = f"Assalomu alaykum, {message.chat.first_name} " \
           f"{message.chat.last_name} " \
           f"{message.chat.username}\n\n" \
           f"Iltimos ismingisni kiriting!!! 👀"
    bot.send_message(message.chat.id, text)
    logger.info("Xabar yuborildi")
    bot.register_next_step_handler(message, get_first_name)


def get_first_name(message):
    first_name = message.text
    text = f"Raxmat {first_name}!!!\n\n\n" \
           f"Familyangizni kiriting 👀"
    bot.send_message(message.chat.id, text)




bot.polling()

"""
1. Pooling

2. Webhook
"""





