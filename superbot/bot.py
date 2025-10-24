import telebot
import random

bot = telebot.TeleBot('7923037076:AAEm98IRSvCydzSUaLJlry9xV3J7ngeo0As')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    mem_list = ['images/mem1.webp', 'images/mem2.webp', 'images/mem3.webp']
    mem_path = random.choice(mem_list)

    with open(mem_path, 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! используй команду /mem, чтобы получить мем!")

bot.polling()