import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['deposit'])
def deposit(message):
	try:
		if message.chat.type == 'private':
			if len(message.text.split(maxsplit=1)) == 2:
				if message.text.split(maxsplit=1)[1].isdigit() and wallet.transaction(message.text.split(maxsplit=1)[1], 'IN').sum.amount >= 1:
					code = [message.text.split(maxsplit=1)[1]]
					bd = sqlite3.connect('balance.db')
					curs = bd.cursor()
					curs.execute('SELECT code FROM deposits WHERE code = ?', code)
					answer1 = curs.fetchall()
					bd.commit()
					curs.close()
					bd.close()
					if answer1 == []:
						bd = sqlite3.connect('balance.db')
						curs = bd.cursor()
						curs.execute('INSERT INTO deposits VALUES(?)', code)
						money = wallet.transaction(message.text.split(maxsplit=1)[1], 'IN').sum.amount
						bd.commit()
						curs.close()
						bd.close()
						user_call = "{0.id}".format(message.from_user, bot.get_me())
						give_id_id = [user_call]
						bd = sqlite3.connect('balance.db')
						curs = bd.cursor()
						curs.execute('SELECT id FROM balance WHERE id = ?', give_id_id)
						answer = curs.fetchall()
						if answer == []:
							curs.execute('INSERT INTO balance VALUES(?, 0)', give_id_id)
							bd.commit()
						curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id)
						balance = curs.fetchall()
						balance1 = balance[0]
						balance = balance1[0]
						give_money = int(balance) + int(money)
						give_money_money = [int(give_money), user_call]
						curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_money_money)
						bd.commit()
						curs.close()
						bd.close()
						bot.send_message(message.chat.id, 'Balance perfect at ' + str(money))
						bot.send_message(config.creator_id, message.from_user.first_name + " replenished the balance on " + str(money))
					else:
						bot.send_message(message.chat.id, "Transaction code has already been used")

			else:
				bot.send_message(message.chat.id, "Wrong format\nReplenish qiwi wallet +" + str(config.wallet) +  " and send the transaction code\nPlease send: /deposit <transaction code>")
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))
		bot.send_message(message.chat.id, "Wrong format\nReplenish qiwi wallet +" + str(config.wallet) + " and send the transaction code\nPlease send: /deposit <transaction code>")

@bot.message_handler(commands=['widthraw'])
def deposit(message):
	try:
		if message.chat.type == 'private':
			if len(message.text.split(maxsplit=2)) == 3:
				if message.text.split(maxsplit=2)[1].isdigit() and message.text.split(maxsplit=2)[2].isdigit():
                    if message.text.split(maxsplit=2)[2] >= config.minwid:
                        phone = message.text.split(maxsplit=2)[1]
                        money = message.text.split(maxsplit=2)[2]
                        comm = int(money) * float(config.com)
                        money_com = int(money) - float(comm)
                        id = ["{0.id}".format(message.from_user, bot.get_me())]
                        bd = sqlite3.connect('balance.db')
                        curs = bd.cursor()
                        curs.execute('SELECT id FROM balance WHERE id = ?', id)
                        answer = curs.fetchall()
                        if answer == []:
                            curs.execute('INSERT INTO balance VALUES(?, 0)', id)
                            bd.commit()
                        curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
                        balance = curs.fetchall()
                        curs.close()
                        bd.close()
                        balance1 = balance[0]
                        balance = balance1[0]
                        if int(balance) >= int(money):
                            wallet.qiwi_transfer(phone, money_com, comment=message.from_user.username)
                            user_call = "{0.id}".format(message.from_user, bot.get_me())
                            give_id_id = [user_call]
                            bd = sqlite3.connect('balance.db')
                            curs = bd.cursor()
                            curs.execute('SELECT id FROM balance WHERE id = ?', give_id_id)
                            answer = curs.fetchall()
                            if answer == []:
                                curs.execute('INSERT INTO balance VALUES(?, 0)', give_id_id)
                                bd.commit()
                            curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id)
                            balance = curs.fetchall()
                            balance1 = balance[0]
                            balance = balance1[0]
                            give_money = int(balance) - int(money)
                            give_money_money = [int(give_money), user_call]
                            curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_money_money)
                            bd.commit()
                            curs.close()
                            bd.close()
                            bot.send_message(message.chat.id, "Complete")
                            bot.send_message(config.creator_id, message.from_user.first_name + " brought " + money +"\n" + "Profit:" + str(comm))
                        else:
                            bot.send_message(message.chat.id, "You have no money")
                    else:
                        bot.send_message(message.chat.id, "Minimum " + str(config.minwid))
				else:
					bot.send_message(message.chat.id, 'Wrong format\nPlease send: /withdraw <phone number> <value>')
			else:
				bot.send_message(message.chat.id, 'Wrong format\nPlease send: /withdraw <phone number> <value>')
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))
		bot.send_message(message.chat.id, 'Wrong format\nPlease send: /withdraw <phone number> <value>')

