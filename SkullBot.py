import random
from tkinter import*
import telebot
import wikipedia
import requests
from googletrans import Translator
translator = Translator()
wikipedia.set_lang("ru")
security = open("Security.txt", "r", encoding="UTF-8")
token = security.readline()
security.close()
skullbot = telebot.TeleBot(token)
@skullbot.message_handler(commands=["translate"])
def translate_message(message):
    text_to_translate = " ".join(message.text.split()[1:])
    translated_text = translator.translate(text_to_translate, dest='en')
    skullbot.send_message(message.chat.id, f"Перевод: {translated_text.text}")
@skullbot.message_handler(commands = ["Hello_everbody_ma_name_is_rob"])
def send_message(message):
    skullbot.reply_to(message, "i hate rob")
@skullbot.message_handler(commands = ["Bro_Help_Me_Get_Rob_Glove"])
def sas (message):
    skullbot.reply_to(message, "i hate rob ")
@skullbot.message_handler(commands = ["get_good_image"])
def send_glove (message):
    skullbot.send_photo(message.chat.id,photo=open("maxresdefault (1).jpg","rb"))
@skullbot.message_handler(commands = ["get_epok_music"])
def send_NUKES (message):
    skullbot.send_audio(message.chat.id,audio=open(" (Killstreak 100 music).mp3","rb"))
@skullbot.message_handler(commands=["start"])
def help (message):
    skullbot.reply_to(message, "Available commands: /Hello_everbody_ma_name_is_rob /Bro_Help_Me_Get_Rob_Glove /get_epok_music /get_good_image")
@skullbot.message_handler(commands=["am_dying"])
def buttons(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_button = telebot.types.KeyboardButton("DAT'S TRUE")
    markup_button_2 = telebot.types.KeyboardButton("jk")
    markup.add(markup_button)
    markup.add(markup_button_2)
    skullbot.send_message(message.chat.id, "Really?", reply_markup = markup)
    sticker = "CAACAgIAAxkBAAEKqCFlQkQ5lqz7lVGJ17XdzI4Qc-YS8gACSgADJsXDEL8pMMbakI2lMwQ"
    skullbot.send_sticker(message.chat.id, sticker)
# @skullbot.message_handler(func=lambda m:True)
# def SearchTheGuyWhoAsked(message):
@skullbot.message_handler(func=lambda m:True)
def DIOlog(message):
    if message.text.lower()=="hello":
        readfail(message, "Helo.txt")
    elif message.text.lower()=="goodbye":
        readfail(message, "BYEAHHAHA.txt")
    elif message.text == "jk":
        readfail(message, "JK.txt")
    elif message.text == "DAT'S TRUE":
        readfail(message, "JK.txt")
    else:
        try:
            skullbot.send_message(message.chat.id, wikipedia.page(message.text).content[:1000])
        except:
            skullbot.send_message(message.chat.id, "я не нашел")
def readfail(message, filename):
    txt_file = open(filename, "r", encoding="UTF-8")
    HELLo = txt_file.read().split("\n")
    txt_file.close()
    skullbot.reply_to(message, random.choice(HELLo))

    



























































skullbot.polling()