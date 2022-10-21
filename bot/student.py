import telebot
import logging
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
token = "5684210743:AAF-xPETRw4fWxM5lheaFTUGTihbXJVUaN4"

bot = telebot.TeleBot(token)

data = dict()


@bot.message_handler(['start'])
def start(message):
    text = f"Assalomu alaykum, {message.chat.first_name} " \
           f"{message.chat.last_name} " \
           f"{message.chat.username}\n\n" \
           f"Iltimos ismingisni kiriting!!! 👀"
    bot.send_message(message.chat.id, text)
    logger.info("Xabar yuborildi")
    bot.register_next_step_handler(message, get_first_name)
    # get_profession(message)


def get_first_name(message):
    first_name = message.text
    data['Ismi'] = first_name
    text = f"Raxmat {first_name}!!!\n\n\n" \
           f"Familyangizni kiriting 👀"

    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_last_name)


def get_last_name(message):
    last_name = message.text
    data['Familiya'] = last_name
    text = f"Raxmat {last_name}!!!\n\n\n" \
           f"Tug'ilgan kunizni kiriting 👀 (24.05.2003)"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_birth_data)


def get_birth_data(message):
    birth_date = message.text
    data["Tug'ilgan kun"] = birth_date
    text = f"Raxmat {birth_date}!!!\n\n\n" \
           f"Manzilingizni kiriting 👀"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_address)


def get_address(message):
    address = message.text
    data["Manzil"] = address
    text = f"Raxmat {address}!!!\n\n\n" \
           f"Kasbingizni kiriting 👀"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_profession)


def get_profession(message):
    address = message.text
    data["Kasbi"] = address
    text = f"Raxmat {address}!!!\n\n\n" \
           f"Jinsigizni kiriting"
    ikm = InlineKeyboardMarkup()
    ikm.add(
        InlineKeyboardButton("Erkak", callback_data="male"),
        InlineKeyboardButton("Ayol", callback_data='female'))

    bot.send_message(message.chat.id, text, reply_markup=ikm)


@bot.callback_query_handler(func=lambda call: True)
def data_xyz(call):
    data["Jinsi"] = "Erkak" if call.data == "male" else "Ayol"
    bot.send_message(call.message.chat.id, "Correct")
    get_gender(call.message)


def get_gender(message):
    s = ''
    for k, v in data.items():
        s += k + " " + v + "\n"
    text = f"Raxmat\n\n" \
           f"{s}"
    bot.send_message(message.chat.id, text)


bot.polling()

"""
1. Polling

2. Webhook
"""
