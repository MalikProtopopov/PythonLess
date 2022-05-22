import telebot
from telebot import types

bot = telebot.TeleBot("5200340010:AAHNlxyry804yThjfcJK-hXAvB2vpKlC_KU")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет<b> {message.from_user.first_name} <u>{message.from_user.last_name}</u></b> "
    bot.send_message(message.chat.id,mess, parse_mode="html")

#@bot.message_handler()
#def get_user_text(message):
#    if message.text == "Hello":
#       bot.send_message(message.chat.id,"Привет ", parse_mode="html")
#    elif message.text == "id":
#        bot.send_message(message.chat.id,  f"Твой айди:, {message.from_user.id}", parse_mode="html")
#    elif message.text == "photo":
#        photo = open("1.png", "rb")
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id,  "я тебя не понимаю:" , parse_mode="html")

@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Хай, фото шик")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Послушать лучший трек в ютубе", url="https://www.youtube.com/watch?v=B4mcHe7Anls"))
    bot.send_message(message.chat.id,"Перейдите на сайт", reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1§)
    website = types.KeyboardButton("Веб сайт",)
    start = types.KeyboardButton("Старт")
    markup.add(website, start)
    bot.send_message(message.chat.id,"Перейдите на сайт", reply_markup=markup)

bot.polling(none_stop=True)
#python newBot.py
