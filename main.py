import os
import telebot

my_secret = os.environ['Token']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['Max_Greet'])
def Max_Greet(message):
    bot.reply_to(message, "I am Max Whats up 🥰😎 ")


@bot.message_handler(commands=["Max"])
def Max(message):
    bot.reply_to(message, "What maye I do For You Master 👑")


@bot.message_handler(commands=["Max_New"])
def new(message):
    bot.reply_to(
        message,
        "Welcome to our Group together We shall Build Awsome Python Codes and Awsome Bots am the group's Ai System Max Its Nice to Meet You"
    )


bot.polling()
