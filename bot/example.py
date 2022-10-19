import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

token = "5684210743:AAF-xPETRw4fWxM5lheaFTUGTihbXJVUaN4"

bot = telebot.TeleBot(token)


@bot.message_handler(['start'])
def hello(message):
    text = "Hello %s %s with %s username" % (message.chat.first_name, message.chat.last_name, message.chat.username)

    # rkm = ReplyKeyboardMarkup(True)
    # rkm.row('Salom')

    # rkm.add("Mahmud", "Abdulloh", "Muhammadamin", "Mahmud", "Abdulloh", "Muhammadamin", "Mahmud", "Abdulloh", "Muhammadamin")

    # ikm = InlineKeyboardMarkup()
    # ikm.add(InlineKeyboardButton("Salom", callback_data="unnique1"), InlineKeyboardButton("Salom", callback_data="unnique2"))
    #
    #
    #
    # bot.send_message(message.chat.id, text, reply_markup=ikm)
#
#
# @bot.message_handler(['remove_button'])
# def remove_button(message):
#     rkr = ReplyKeyboardRemove()
#     bot.send_message(message.chat.id, "Removed", reply_markup=rkr)


bot.polling()
