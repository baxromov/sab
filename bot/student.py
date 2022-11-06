# import datetime
# import telebot
# import logging
# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
#     KeyboardButton
# from geopy.geocoders import Nominatim
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
# token = "5641871319:AAEy18gfMc0jO7FLS1Z6l0YEc7vPLkq0-Tw"
#
# bot = telebot.TeleBot(token)
#
# dictionary = {}
#
#
# @bot.message_handler(['start'])
# def start(message):
#     text = f"Assalomu alekum, {message.chat.first_name}"
#     bot.send_message(message.chat.id, text)
#     bot.send_message(message.chat.id, "Iltimos ismingizni kiriting!!!")
#     logger.info("Sent")
#     bot.register_next_step_handler(message, get_first_name)
#
#
# def get_first_name(message):
#     first_name = message.text
#     dictionary['Ism'] = first_name
#     bot.send_message(message.chat.id, "Iltimos familyangizni kiriting!!!")
#     bot.register_next_step_handler(message, get_last_name)
#
#
# def get_last_name(message):
#     last_name = message.text
#     dictionary['Familya'] = last_name
#     bot.send_message(message.chat.id, "Iltimos tug'ilgan kuningizni kiriting")
#     day = datetime.date.today().strftime("%d")
#     month = datetime.date.today().strftime("%m")
#     year = datetime.date.today().strftime("%Y")
#     ikm = InlineKeyboardMarkup()
#     ikm.add(InlineKeyboardButton("Kun +1", callback_data='kun+'), InlineKeyboardButton("Oy +1", callback_data='oy+'),
#             InlineKeyboardButton("Yil +1", callback_data="yil+"))
#     ikm.add(InlineKeyboardButton("Kun -1", callback_data='kun-'), InlineKeyboardButton("Oy -1", callback_data='oy-'),
#             InlineKeyboardButton("Yil -1", callback_data="yil-")
#             )
#     bot.send_message(message.chat.id, text=f"Kun: {day}  Oy: {month}  Yil: {year}", reply_markup=ikm)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def get_birth_date(call):
#     birth = call.data
#     dictionary["Tug'ilgan kun"] = birth
#     keyboard = ReplyKeyboardMarkup()
#     button_phone = KeyboardButton(text="Telefon raqam 📞", request_contact=True)
#     keyboard.add(button_phone)
#     bot.send_message(call.message.chat.id, "Iltimos telefon raqamingizni yuborish uchun knopkani bosing!!!",
#                      reply_markup=keyboard)
#
#
# @bot.message_handler(content_types=['contact'])
# def contact(message):
#     if message.contact is not None:
#         remove = ReplyKeyboardRemove()
#         dictionary['Telefon raqam'] = message.contact.phone_number
#         bot.register_next_step_handler(message, get_address)
#         bot.send_message(message.chat.id, "Iltimos addressingizni yuboring",
#                          reply_markup=remove)
#         keyboard = ReplyKeyboardMarkup()
#         button_address = KeyboardButton(text="Lokatsiya 🗺", request_location=True)
#         keyboard.add(button_address)
#         bot.send_message(message.chat.id, "Yuborish uchun knopkani bosing!!!!", reply_markup=keyboard)
#
#
# @bot.message_handler(content_types=['location'])
# def get_address(message):
#     location = [message.location.latitude, message.location.longitude]
#     geoLoc = Nominatim(user_agent="GetLoc")
#     locname = geoLoc.reverse(f"{location[0]}, {location[1]}")
#     dictionary['Address'] = locname
#     ikm = InlineKeyboardMarkup()
#     ikm.add(InlineKeyboardButton("Erkak", callback_data='male'), InlineKeyboardButton("Ayol", callback_data='female'))
#     bot.send_message(message.chat.id, "Iltimos jinsingizni tanlang!!!", reply_markup=ikm)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     dictionary['Jins'] = 'Erkak' if call.data == 'male' else 'Ayol'
#     remove = ReplyKeyboardRemove()
#     text = ""
#     for key, value in dictionary.items():
#         text += f"{key}: {value}\n"
#     bot.send_message(call.message.chat.id, text, reply_markup=remove)
#
#
# bot.polling()
# """
# 1. Polling
#
# 2. Webhook
# """

import telebot
from bot.utils.worksheet import WorkSheet
from generate import generator_qr

token = "5641871319:AAEy18gfMc0jO7FLS1Z6l0YEc7vPLkq0-Tw"
bot = telebot.TeleBot(token)

secret = generator_qr()


@bot.message_handler(['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello welcome to SAB")


@bot.message_handler(['get_qr'])
def qr(message):
    bot.send_photo(message.chat.id, photo=open(secret[1], 'rb'))


@bot.message_handler(['access'])
def accessing(message):
    bot.send_message(message.chat.id,
                     "Please send secret word \nCarefully write down every letter and space of the secret word.")
    bot.register_next_step_handler(message, checker)


def checker(message):
    if message.text == secret[0]:
        w = WorkSheet('./students-366915-3be3d74e97e3.json', 'data', 'page 1')
        w.mark_student(str(message.chat.id), date="31.10.2022")
        bot.send_message(message.chat.id, "You are marked as arrived")


if __name__ == "__main__":
    # server = HTTPServer(server_address=('127.0.0.1', 2000), BaseHTTPRequestHandler)
    bot.polling()

"""
1. Polling

2. Webhook
"""
