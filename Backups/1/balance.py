import telebot
import config
from telebot import types
import sqlite3

bot = telebot.TeleBot(config.Token)
winner = []
def winner()
    id = ["{0.id}".format(call.from_user, bot.get_me())]
    bd = sqlite3.connect('balance.db')
    curs = bd.cursor()
    bot.send_message(call.message.chat.id, "Winners:\n" +"\n".join(winner) + "\nWinners receive " + str(pool))
    curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
    balance = curs.fetchall()
    balance1 = []
    balance2 = []
    for i in filter(str.isdigit, str(balance)):
        balance1.append(i)
    balance2.append(balance1[1] + int(round(pool)))
    curs.execute('UPDATE ballance SET user_balance = ? WHERE id = ?',balance2, id)
    bd.commit()
    curs.close()
    bd.close()