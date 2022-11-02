import telebot
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
from bot.utils.worksheet import WorkSheet

token = "5684210743:AAGeidrT3wVYLSlTgPIl0nzvDmMtEMyCa4A"

bot = telebot.TeleBot(token)



@bot.message_handler(['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello")
    w = WorkSheet('../pysheets-demo-362905-50f5575b16f9.json', 'example_dev', 'Python_G1')
    # w.mark_student('123458', date='31.10.2022')
    w.mark_student(str(message.chat.id))
    bot.send_message(message.chat.id, "Keldiz")

# bot.polling()



if __name__ == "__main__":
    # server = HTTPServer(server_address=('127.0.0.1', 2000), BaseHTTPRequestHandler)
    bot.polling()



"""
1. Polling

2. Webhook
"""
