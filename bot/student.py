import datetime
import time

import telebot
import logging
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton
from geopy.geocoders import Nominatim

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
token = "5695762826:AAGO7piM-pxAQem3KVpfOBja2tRQKs4i8dE"

bot = telebot.TeleBot(token)

dictionary = {}


@bot.message_handler(['start'])
def start(message):
    text = f"Assalomu alekum, {message.chat.first_name}"
    bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, "Iltimos ismingizni kiriting!!!")
    logger.info("Sent")
    bot.register_next_step_handler(message, get_first_name)


def get_first_name(message):
    first_name = message.text
    dictionary['Ism'] = first_name
    bot.send_message(message.chat.id, "Iltimos familyangizni kiriting!!!")
    bot.register_next_step_handler(message, get_last_name)


def get_last_name(message):
    last_name = message.text
    dictionary['Familya'] = last_name
    bot.send_message(message.chat.id, "Iltimos tug'ilgan kuningizni kiriting")
    day = 1
    month = 1
    year = datetime.date.today().strftime("%Y")
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton("Kun +1", callback_data='kun+'), InlineKeyboardButton("Oy +1", callback_data='oy+'),
            InlineKeyboardButton("Yil +1", callback_data="yil+"))
    ikm.add(InlineKeyboardButton("Kun -1", callback_data='kun-'), InlineKeyboardButton("Oy -1", callback_data='oy-'),
            InlineKeyboardButton("Yil -1", callback_data="yil-")
            )
    a = bot.send_message(message.chat.id, text=f"Kun: {day}  Oy: {month}  Yil: {year}", reply_markup=ikm)
    bot.register_next_step_handler(message, get_birth_date)


@bot.callback_query_handler(func=lambda call: True)
def get_birth_date(call):
    birth = call.data
    dictionary["Tug'ilgan kun"] = birth
    keyboard = ReplyKeyboardMarkup()
    button_phone = KeyboardButton(text="Telefon raqam 📞", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(call.message.chat.id, "Iltimos telefon raqamingizni yuborish uchun knopkani bosing!!!",
                     reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        remove = ReplyKeyboardRemove()
        dictionary['Telefon raqam'] = message.contact.phone_number
        bot.register_next_step_handler(message, get_address)
        bot.send_message(message.chat.id, "Iltimos addressingizni yuboring",
                         reply_markup=remove)
        keyboard = ReplyKeyboardMarkup()
        button_address = KeyboardButton(text="Lokatsiya 🗺", request_location=True)
        keyboard.add(button_address)
        bot.send_message(message.chat.id, "Yuborish uchun knopkani bosing!!!!", reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def get_address(message):
    location = [message.location.latitude, message.location.longitude]
    geoLoc = Nominatim(user_agent="GetLoc")
    locname = geoLoc.reverse(f"{location[0]}, {location[1]}")
    dictionary['Address'] = locname
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton("Erkak", callback_data='male'), InlineKeyboardButton("Ayol", callback_data='female'))
    bot.send_message(message.chat.id, "Iltimos jinsingizni tanlang!!!", reply_markup=ikm)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    dictionary['Jins'] = 'Erkak' if call.data == 'male' else 'Ayol'
    remove = ReplyKeyboardRemove()
    bot.send_message(call.message.chat.id, "Iltimos kasbingizni kiriting!!!", reply_markup=remove)
    bot.register_next_step_handler(call.message, get_proffesion)


def get_proffesion(message):
    prof = message.text
    dictionary['Kasb'] = prof
    text = ""
    for key, value in dictionary.items():
        text += f"{key}: {value}\n"
    bot.send_message(message.chat.id, text)


bot.polling()
"""
1. Polling

2. Webhook
"""
