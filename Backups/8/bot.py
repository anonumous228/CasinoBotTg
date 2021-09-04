import telebot
import config
import time
from telebot import types
from telegram.ext.dispatcher import run_async
import sqlite3

from threading import Timer
from datetime import timedelta, datetime




bot = telebot.TeleBot(config.Token)

lst = []
check = []
winner = []
wagger = []
username = []
id_winner = []
id_check = []
big_balance = []
bet1 = []
kek = []
answ = []

 


@bot.message_handler(commands=['for_two'])
def for_two(message):
	try:
		for i in range(len(config.chat_id)):
			if str(message.chat.id) == str(config.chat_id[i]):
				privacy = True
				if privacy == True:
					if message.chat.type == 'private':
						bot.send_message(message.chat.id, "Мы еще не сделали одиночный режим")
					else:
						global gameee
						if bet1 == []:
							global bet
							if len(message.text.split(maxsplit=1)) == 1:
								bot.send_message(message.chat.id, "Неверный формат\nПопробуйте: /for_two <ставка>")
							else:
								bet = message.text.split(maxsplit=1)[1]
								global user1
								user1 = "{0.id}".format(message.from_user, bot.get_me())
								global first_name
								first_name = "{0.first_name}".format(message.from_user, bot.get_me())
								if bet.isdigit() == True and 0 <= int(bet) and bet != "":
									bd = sqlite3.connect('balance.db')
									curs = bd.cursor()
									give_id_id1 = [message.from_user.id]
									curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
									answer = curs.fetchall()
									if answer == []:
										curs.execute('INSERT INTO balance VALUES(?, 0)', give_id_id1)
										bd.commit()
									curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
									balance = curs.fetchall()
									balance1 = balance[0]
									balance = balance1[0]
									curs.close()
									bd.close()
									if int(balance) >= int(bet):
										bet1.append(bet)
										markup2 = types.InlineKeyboardMarkup(row_width=2)
										item1 = types.InlineKeyboardButton("Начать", callback_data="start_two")
										item2 = types.InlineKeyboardButton("Отмена", callback_data="cancel")
										item5 = types.InlineKeyboardButton("Присоединиться", callback_data="join_two")
										markup2.add(item1, item2, item5)
										global gamee
										gamee = bot.send_message(message.chat.id, "Игра для двоих со ставкой: " + bet, reply_markup=markup2)
										gameee = gamee
										gamee = gamee.message_id
										global t
										t = Timer(int(config.delay), cancel1)
										t.start()
									else:
										bot.send_message(message.chat.id, "У вас недостаточно средств")
								else:
									bot.send_message(message.chat.id, "Неверный формат\nПопробуйте: /for_two <ставка>")
						else:
							bot.reply_to(gameee, "Игра уже создана")
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))


def cancel1():
	bot.edit_message_text(chat_id=gameee.chat.id, message_id=gameee.message_id, text="Игра была отменена", reply_markup=None)
	lst.clear()
	check.clear()
	winner.clear()
	wagger.clear()
	username.clear()
	id_winner.clear()
	id_check.clear()
	bet1.clear()

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, "Команды:\n/new_game <ставка>\n/for_two <ставка>\n/balance\n/give <значение>\n/deposit <номер чека>\n/widthraw <номер кошелька> <значение>")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	try:
		bd = sqlite3.connect('balance.db')
		curs = bd.cursor()
		id = ["{0.id}".format(message.from_user, bot.get_me())]
		curs.execute('SELECT id FROM balance WHERE id = ?', id)
		answer = curs.fetchall()
		if answer == []:
			curs.execute('INSERT INTO balance VALUES(?, 0)', id)
			bd.commit()
		curs.close()
		bd.close()
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))

@bot.message_handler(commands=['balance'])
def balance(message):
	try:
		bd = sqlite3.connect('balance.db')
		curs = bd.cursor()
		id = ["{0.id}".format(message.from_user, bot.get_me())]
		curs.execute('SELECT id FROM	 balance WHERE id = ?', id)
		answer = curs.fetchall()
		if answer == []:
			curs.execute('INSERT INTO balance VALUES(?, 0)', id)
			bd.commit()
		curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
		balance = curs.fetchall()
		curs.close()
		bd.close()
		balance1 = balance[0]
		if message.chat.type == 'private':
			bot.send_message(message.chat.id, "Ваш баланс: "+ str(balance1[0]))
		else:
			bot.reply_to(message, text="{0.first_name} balance: ".format(message.from_user, bot.get_me()) + str(balance1[0]))
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))

@bot.message_handler(commands=['new_game'])
def game(message):
	try:
		for i in range(len(config.chat_id)):
			if str(message.chat.id) == str(config.chat_id[i]):
				privacy = True
				if privacy == True:
					if message.chat.type == 'private':
						bot.send_message(message.chat.id, "Мы еще не сделали одиночный режим")
					else:
						global gameee
						if bet1 == []:
							global bet
							if len(message.text.split(maxsplit=1)) == 1:
								bot.send_message(message.chat.id, "Неверный формат\nПопробуйте: /new_game <ставка>")
							else:
								bet = message.text.split(maxsplit=1)[1]
								global user1
								user1 = "{0.id}".format(message.from_user, bot.get_me())
								global first_name
								first_name = "{0.first_name}".format(message.from_user, bot.get_me())
								if bet.isdigit() == True and 0 <= int(bet) and bet != "":
									bd = sqlite3.connect('balance.db')
									curs = bd.cursor()
									give_id_id1 = [message.from_user.id]
									curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
									answer = curs.fetchall()
									if answer == []:
										curs.execute('INSERT INTO balance VALUES(?, 0)', give_id_id1)
										bd.commit()
									curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
									balance = curs.fetchall()
									balance1 = balance[0]
									balance = balance1[0]
									curs.close()
									bd.close()
									if int(balance) >= int(bet):
										bet1.append(bet)
										markup2 = types.InlineKeyboardMarkup(row_width=2)
										item1 = types.InlineKeyboardButton("Угадай цифру", callback_data="number")
										item2 = types.InlineKeyboardButton("Кто больше", callback_data="bigger")
										item3 = types.InlineKeyboardButton("Попади в центр", callback_data="center")
										item4 = types.InlineKeyboardButton("Кидание дротиков", callback_data="throw_darts")
										item5 = types.InlineKeyboardButton("Отмена", callback_data="cancel")
										markup2.add(item1, item2, item3, item4, item5)
										global gamee
										gamee = bot.send_message(message.chat.id, "Выберите игру	", reply_markup=markup2)
										gameee = gamee
										gamee = gamee.message_id
										global t
										t = Timer(int(config.delay), cancel1)
										t.start()
									else:
										bot.send_message(message.chat.id, "У вас недостаточно средств")
								else:
									bot.send_message(message.chat.id, "Неверный формат\nПопробуйте: /new_game <ставка>")
						else:
							bot.reply_to(gameee, "Игра уже создана")
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))

@bot.message_handler(commands=['give'])
def give(message):
	try:
		if message.chat.type == "supergroup":
			if len(message.text.split(maxsplit=1)) == 1:
				bot.send_message(message.chat.id, "Wrong format\nPlease send: /give <value>")
			else:
				givee = message.text.split(maxsplit=1)[1]
				user_call = "{0.id}".format(message.from_user, bot.get_me())
				give_id = message.reply_to_message.from_user.id
				give_id_id = [give_id]

				if user_call == config.creator_id:
					if givee.isdigit() == True and 0 <= int(givee) and givee != "":
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
						give_bet = int(balance) + int(givee)
						give_bet_bet = [int(give_bet), give_id]
						curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_bet_bet)
						bd.commit()
						curs.close()
						bd.close()
						bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " новый баланс: "  + str(give_bet))
				else:
					if givee.isdigit() == True and 0 <= int(givee) and givee != "":
						bd = sqlite3.connect('balance.db')
						curs = bd.cursor()
						give_id_id1 = [message.from_user.id]
						curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
						answer = curs.fetchall()
						if answer == []:
							curs.execute('INSERT INTO balance VALUES(?, 0)', give_id_id1)
							bd.commit()
						curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
						balance = curs.fetchall()
						balance1 = balance[0]
						balance = balance1[0]
						curs.close()
						bd.close()
						if int(balance) >= int(message.text[6:]):
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
							give_bet = int(balance) + int(givee)
							give_bet_bet = [int(give_bet), give_id]
							curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_bet_bet)
							curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
							balance = curs.fetchall()
							balance1 = balance[0]
							balance = balance1[0]
							give_bet = int(balance) - int(givee)
							give_bet_bet1 = [int(give_bet), int(message.from_user.id)]
							curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_bet_bet1)
							bd.commit()
							curs.close()
							bd.close()
						else:
							bot.send_message(message.chat.id, "У вас недостаточно средств")
					else:
						bot.send_message(message.chat.id, 'Неверный формат\nПопробуйте: /give <значение>')
		else:
			bot.send_message(message.chat.id, 'Сделайте группу супергруппой')
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))


@bot.message_handler(commands=['cancel'])
def oplata(message):
	user_call = "{0.id}".format(message.from_user, bot.get_me())
	if user_call == "214580153":
		cancel1()


@run_async
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
				user_call = "{0.id}".format(call.from_user, bot.get_me())
				if call.data == 'number':
					if user_call == user1:
						if str(call.message.message_id) == str(gamee):
							markup3 = types.InlineKeyboardMarkup(row_width=3)
							number1 = types.InlineKeyboardButton("1", callback_data='1')
							number2 = types.InlineKeyboardButton("2", callback_data='2')
							number3 = types.InlineKeyboardButton("3", callback_data='3')
							number4 = types.InlineKeyboardButton("4", callback_data='4')
							number5 = types.InlineKeyboardButton("5", callback_data='5')
							number6 = types.InlineKeyboardButton("6", callback_data='6')
							start = types.InlineKeyboardButton("Начать", callback_data='start_number')
							cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
							markup3.add(number1, number2, number3, number4, number5, number6, start, cancel)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) +"\nУгадай цифру", reply_markup=markup3)
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра уже создана")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == 'join_two':
					if str(call.message.message_id) == str(gamee):
						if len(username) == 2:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Максимальное количество участников")
						else:
							username2 = "{0.id}".format(call.from_user, bot.get_me())
							id = ["{0.id}".format(call.from_user, bot.get_me())]
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
							if int(balance) >= int(bet):
								number = "{0.first_name}".format(call.from_user, bot.get_me())
								have = False
								for i in range(len(username)):
									if str(username[i]) == str(username2):
										have = True
										bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=number + " уже участвует")
								if have != True:
									username.append(username2)
									markup4 = types.InlineKeyboardMarkup(row_width=2)
									start = types.InlineKeyboardButton("Начать", callback_data='start_two')
									cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
									join = types.InlineKeyboardButton("Присоединиться", callback_data='join_two')
									markup4.add(start, cancel, join)
									check.append(number)
									bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра для двоих со ставкой: " + str(bet) + "\n" + "\n".join(check), reply_markup=markup4)
									id_check.append("{0.id}".format(call.from_user, bot.get_me()))
							else:
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас недостаточно средств")
					else:
						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра уже создана")

				elif call.data == 'start_two':
					if user_call == user1 or user_call == config.creator_id:
						if len(username) == 0 or len(username) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Мало участников")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
							t.cancel()
							for i in range(len(id_check)):
								username2 = id_check[i]
								id = [id_check[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								balance = curs.fetchall()
								balance1 = balance[0]
								balance = balance1[0]
								balance3 = int(balance) - int(bet)
								big_balance = [balance3, username2]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
							time.sleep(0.5)
							throw_cube = bot.send_dice(call.message.chat.id)
							dice_value = throw_cube.dice.value
							if dice_value <= 3:
								winner.append(check[0])
								id_winner.append(id_check[0])
							else:
								winner.append(check[1])
								id_winner.append(id_check[1])
							pool = int(bet) * len(id_check) / len(id_winner)
							int(round(pool))
							for i in range(len(id_winner)):
								id = [id_winner[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								id.clear()
								balance = curs.fetchall()
								balance1 = balance[0]
								balance2 = []
								balance2.append(int(balance1[0]) + pool)
								big_balance = [balance2[0], id_winner[i]]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								big_balance.clear()
							time.sleep(5)
							bot.send_message(call.message.chat.id,"Победитель: " + " ".join(winner) + " выиграл " + str(pool))
							id_check.clear()
							lst.clear()
							winner.clear()
							check.clear()
							wagger.clear()
							username.clear()
							id_check.clear()
							id_winner.clear()
							bet1.clear()

				elif call.data == 'start_number' :
					if user_call == user1 or user_call == config.creator_id:
						if len(username) == 0 or len(username) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Мало участников")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
							t.cancel()
							for i in range(len(id_check)):
								username2 = id_check[i]
								id = [id_check[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								balance = curs.fetchall()
								balance1 = balance[0]
								balance = balance1[0]
								balance3 = int(balance) - int(bet)
								big_balance = [balance3, username2]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
							time.sleep(0.5)
							throw_cube = bot.send_dice(call.message.chat.id)
							dice_value = throw_cube.dice.value
							have = True
							while have == True:
								if str(dice_value) not in wagger:
									bot.delete_message(chat_id = call.message.chat.id, message_id = throw_cube.message_id)
									throw_cube = bot.send_dice(call.message.chat.id)
									dice_value = throw_cube.dice.value
									time.sleep(3)
								else:
									have = False
							time.sleep(1)
							for i in range(len(lst)):
								if lst[i] == check[i] + ": " + str(dice_value):
									winner.append(check[i])
									id_winner.append(id_check[i])
							pool = int(bet) * len(id_check) / len(id_winner)
							int(round(pool))
							for i in range(len(id_winner)):
								id = [id_winner[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								id.clear()
								balance = curs.fetchall()
								balance1 = balance[0]
								balance2 = []
								balance2.append(int(balance1[0]) + pool)
								big_balance = [balance2[0], id_winner[i]]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								big_balance.clear()

							bot.send_message(call.message.chat.id, "Победители:\n" +"\n".join(winner) + "\nПобедители получают по " + str(pool))
							id_check.clear()
							lst.clear()
							winner.clear()
							check.clear()
							wagger.clear()
							username.clear()
							id_check.clear()
							id_winner.clear()
							bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == '1' or call.data == '2' or call.data == '3' or call.data == '4' or call.data == '5' or call.data == '6':
					id = ["{0.id}".format(call.from_user, bot.get_me())]
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
					if int(balance) >= int(bet):
						number = "{0.first_name}".format(call.from_user, bot.get_me())
						username2 = "{0.id}".format(call.from_user, bot.get_me())
						have = False
						for i in range(len(lst)):
							if str(username[i]) == str(username2):
								have = True
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text= number + " уже участвует")
						if have != True:
							username.append(username2)
							check.append(number)
							markup3 = types.InlineKeyboardMarkup(row_width=3)
							number1 = types.InlineKeyboardButton("1", callback_data='1')
							number2 = types.InlineKeyboardButton("2", callback_data='2')
							number3 = types.InlineKeyboardButton("3", callback_data='3')
							number4 = types.InlineKeyboardButton("4", callback_data='4')
							number5 = types.InlineKeyboardButton("5", callback_data='5')
							number6 = types.InlineKeyboardButton("6", callback_data='6')
							start = types.InlineKeyboardButton("Начать", callback_data='start_number')
							cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
							markup3.add(number1, number2, number3, number4, number5, number6, start, cancel)
							lst.append(number + ": " + call.data)
							id_check.append(username2)
							wagger.append(call.data)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nУгадай цифру\n" + "\n".join(lst), reply_markup=markup3)
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас недостаточно средств")

				elif call.data =="bigger":
					if user_call == user1:
						if str(call.message.message_id) == str(gamee):
							markup4 = types.InlineKeyboardMarkup(row_width=2)
							start = types.InlineKeyboardButton("Начать", callback_data='start_bigger')
							cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
							join = types.InlineKeyboardButton("Присоединиться", callback_data='join')
							markup4.add(start, cancel, join)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nКто больше", reply_markup=markup4)
							lst.clear()
							winner.clear()
							check.clear()
							username.clear()
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра уже создана")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == 'start_bigger':
					if user_call == user1 or user_call == config.creator_id:
						if len(check) == 0 or len(check) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Мало участников")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
							t.cancel()
							for i in range(len(id_check)):
								username2 = id_check[i]
								id = [id_check[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								balance = curs.fetchall()
								balance1 = balance[0]
								balance = balance1[0]
								balance3 = int(balance) - int(bet)
								big_balance = [balance3, username2]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								id.clear()
							time.sleep(0.5)
							max = 0
							for i in range(len(check)):
									bot.send_message(call.message.chat.id, check[i] + " кидает кубики")
									summ = 0
									for j in range(3):
										throw_cube = bot.send_dice(call.message.chat.id)
										dice_value = throw_cube.dice.value
										time.sleep(5)
										summ = summ + dice_value
									lst.append(check[i] + ": " + str(summ))
									if summ >= max:
										if summ == max:
											winner.append(check[i])
											id_winner.append(id_check[i])
										else:
											max = summ
											winner.clear()
											id_winner.clear()
											winner.append(check[i])
											id_winner.append(id_check[i])
									time.sleep(2)
									bot.send_message(call.message.chat.id, check[i] + " выкинул в сумме " + str(summ))
									time.sleep(2)
							pool = int(bet) * len(id_check) / len(id_winner)
							int(round(pool))
							for i in range(len(id_winner)):
								id = [id_winner[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								id.clear()
								balance = curs.fetchall()
								balance1 = balance[0]
								balance2 = []
								balance2.append(int(balance1[0]) + pool)
								big_balance = [balance2[0], id_winner[i]]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								big_balance.clear()
							time.sleep(3)
							bot.send_message(call.message.chat.id, "Результаты:\n" + "\n".join(lst))
							time.sleep(3)
							bot.send_message(call.message.chat.id, "Победители:\n" + "\n".join(winner) + "\nПобедители получили по " + str(pool))
							lst.clear()
							check.clear()
							winner.clear()
							wagger.clear()
							username.clear()
							id_winner.clear()
							id_check.clear()
							bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				if call.data == 'cancel':
					if user_call == user1 or user_call == config.creator_id:
						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра была отменена", reply_markup=None)
						lst.clear()
						check.clear()
						winner.clear()
						wagger.clear()
						username.clear()
						id_winner.clear()
						id_check.clear()
						bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == 'join':
					username2 = "{0.id}".format(call.from_user, bot.get_me())
					id = ["{0.id}".format(call.from_user, bot.get_me())]
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
					if int(balance) >= int(bet):
						number = "{0.first_name}".format(call.from_user, bot.get_me())
						have = False
						for i in range(len(username)):
							if str(username[i]) == str(username2):
								have = True
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=number + " уже участвует")
						if have != True:
								username.append(username2)
								markup4 = types.InlineKeyboardMarkup(row_width=2)
								start = types.InlineKeyboardButton("Начать", callback_data='start_bigger')
								cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
								join = types.InlineKeyboardButton("Присоединиться", callback_data='join')
								markup4.add(start, cancel, join)
								check.append(number)
								bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nКто больше\n" + "\n".join(check), reply_markup=markup4)
								id_check.append("{0.id}".format(call.from_user, bot.get_me()))
					else:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас недостаточно средств")


				elif call.data == "start_to_the_center":
					if user_call == user1 or user_call == config.creator_id:
						if len(check) == 0 or len(check) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Мало участников")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
							t.cancel()
							for i in range(len(id_check)):
								username2 = id_check[i]
								id = [id_check[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								balance = curs.fetchall()
								balance1 = balance[0]
								balance = balance1[0]
								balance3 = int(balance) - int(bet)
								big_balance = [balance3, username2]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								id.clear()
							time.sleep(0.5)
							dart = True
							time.sleep(3)
							while dart == True:
								for i in range(len(id_check)):
									bot.send_message(call.message.chat.id, check[i] + " кидает дротик")
									time.sleep(2)
									darts = bot.send_dice(call.message.chat.id, "🎯")
									darts_value = darts.dice.value
									if darts_value == 6:
										id_winner.append(id_check[i])
										winner.append(check[i])
									time.sleep(6)
								if len(id_winner) >= 1:
									dart = False
								else:
										bot.send_message(call.message.chat.id, "Никто не попал, перекидываем")
							pool = int(bet) * len(id_check) / len(id_winner)
							int(round(pool))
							for i in range(len(id_winner)):
								id = [id_winner[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								id.clear()
								balance = curs.fetchall()
								balance1 = balance[0]
								balance2 = []
								balance2.append(int(balance1[0]) + pool)
								big_balance = [balance2[0], id_winner[i]]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								big_balance.clear()
							time.sleep(2)
							bot.send_message(call.message.chat.id, "Победители:\n" + "\n".join(winner) + "\nПобедители получают " + str(pool))
							lst.clear()
							check.clear()
							winner.clear()
							wagger.clear()
							username.clear()
							id_winner.clear()
							id_check.clear()
							bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == "center":
					if user_call == user1:
						if str(call.message.message_id) == str(gamee):
							markup4 = types.InlineKeyboardMarkup(row_width=2)
							start = types.InlineKeyboardButton("Начать", callback_data='start_to_the_center')
							cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
							join = types.InlineKeyboardButton("Присоединиться", callback_data='join_center')
							markup4.add(start, cancel, join)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nПопади в центр", reply_markup=markup4)
							lst.clear()
							winner.clear()
							check.clear()
							username.clear()
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра уже создана")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data =='throw_darts':
					if user_call == user1:
						if str(call.message.message_id) == str(gamee):
							markup4 = types.InlineKeyboardMarkup(row_width=2)
							start = types.InlineKeyboardButton("Начать", callback_data='start_throw_darts')
							cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
							join = types.InlineKeyboardButton("Присоединиться", callback_data='join_throw_darts')
							markup4.add(start, cancel, join)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nКидание дротиков", reply_markup=markup4)
							lst.clear()
							winner.clear()
							check.clear()
							username.clear()
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Игра уже создана")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == 'join_throw_darts':
					username2 = "{0.id}".format(call.from_user, bot.get_me())
					id = ["{0.id}".format(call.from_user, bot.get_me())]
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
					if int(balance) >= int(bet):
						number = "{0.first_name}".format(call.from_user, bot.get_me())
						have = False
						for i in range(len(username)):
							if str(username[i]) == str(username2):
								have = True
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=number + " уже участвует")
						if have != True:
								username.append(username2)
								markup4 = types.InlineKeyboardMarkup(row_width=2)
								start = types.InlineKeyboardButton("Начать", callback_data='start_throw_darts')
								cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
								join = types.InlineKeyboardButton("Присоединиться", callback_data='join_throw_darts')
								markup4.add(start, cancel, join)
								check.append(number)
								bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nКидание дротиков\n" + "\n".join(check), reply_markup=markup4)
								id_check.append("{0.id}".format(call.from_user, bot.get_me()))
					else:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас недостаточно средств")

				elif call.data == 'start_throw_darts':
					if user_call == user1 or user_call == config.creator_id:
						if len(check) == 0 or len(check) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Мало участников")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
							t.cancel()
							for i in range(len(id_check)):
								username2 = id_check[i]
								id = [id_check[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								balance = curs.fetchall()
								balance1 = balance[0]
								balance = balance1[0]
								balance3 = int(balance) - int(bet)
								big_balance = [balance3, username2]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								id.clear()
							time.sleep(0.5)
							for i in range(len(id_check)):
								bot.send_message(call.message.chat.id, check[i] + " кидает дротик")
								j = 1
								darts = bot.send_dice(call.message.chat.id, "🎯")
								darts_value = darts.dice.value
								time.sleep(5)
								bot.send_message(call.message.chat.id, check[i] + " попал в " + str(darts_value - 1))
								kek.append(i)
								lst.append(darts_value)
								time.sleep(3)
								while j < 2:
									markup = types.InlineKeyboardMarkup(row_width=2)
									Yes = types.InlineKeyboardButton("Да", callback_data='yes')
									No = types.InlineKeyboardButton("Нет", callback_data='no')
									markup.add(Yes, No)
									ques = bot.send_message(chat_id=call.message.chat.id, text=check[i] + ", вы хотите перебросить дротик?", reply_markup=markup)
									now = datetime.now()
									k = True
									while k == True:
										if answ == ["no"] or datetime.now() - now > timedelta(seconds= 15):
											bot.edit_message_text(chat_id=ques.chat.id, message_id=ques.message_id, text=check[i] + " решает не перебрасывать дротик", reply_markup=None)
											time.sleep(2)
											j = 2
											k = False
										elif answ == ["yes"]:
											time.sleep(2)
											darts = bot.send_dice(call.message.chat.id, "🎯")
											darts_value = darts.dice.value
											lst[i] = darts_value
											time.sleep(5)
											bot.send_message(call.message.chat.id, check[i] + " попал в " + str(darts_value - 1))
											k = False
											j = j+1
									time.sleep(3)
									answ.clear()
								kek.clear()
							max = 0
							for i in range(len(lst)):
								if lst[i] >= max:
									if max == lst[i]:
										id_winner.append(id_check[i])
										winner.append(check[i])
									else:
										id_winner.clear()
										winner.clear()
										max = lst[i]
										id_winner.append(id_check[i])
										winner.append(check[i])
							pool = int(bet) * len(id_check) / len(id_winner)
							int(round(pool))
							uch = []
							for i in range(len(lst)):
								uch.append(str(check[i]) +" попал в " + str(lst[i] - 1))
							bot.send_message(call.message.chat.id,  "\n".join(uch))
							time.sleep(2)
							for i in range(len(id_winner)):
								id = [id_winner[i]]
								bd = sqlite3.connect('balance.db')
								curs = bd.cursor()
								curs.execute('SELECT user_balance FROM balance WHERE id = ?', id)
								id.clear()
								balance = curs.fetchall()
								balance1 = balance[0]
								balance2 = []
								balance2.append(int(balance1[0]) + pool)
								big_balance = [balance2[0], id_winner[i]]
								curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', big_balance)
								bd.commit()
								curs.close()
								bd.close()
								big_balance.clear()
							time.sleep(2)
							bot.send_message(call.message.chat.id, "Победители:\n" + "\n".join(winner) + "\nПобедители получают по " + str(pool))
							lst.clear()
							check.clear()
							winner.clear()
							wagger.clear()
							username.clear()
							id_winner.clear()
							id_check.clear()
							bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + " создал эту игру")

				elif call.data == "yes":
					if id_check[kek[0]] == user_call:
						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.from_user.first_name + " решает перебросить дротик", reply_markup=None)
						answ.append("yes")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=check[kek[0]] + ' думает что выбрать')

				elif call.data == "no":
					if id_check[kek[0]] == user_call:
						answ.append("no")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=check[kek[0]] + ' думает что выбрать')

				elif call.data == 'join_center':
					username2 = "{0.id}".format(call.from_user, bot.get_me())
					id = ["{0.id}".format(call.from_user, bot.get_me())]
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
					if int(balance) >= int(bet):
						number = "{0.first_name}".format(call.from_user, bot.get_me())
						have = False
						for i in range(len(username)):
							if str(username[i]) == str(username2):
								have = True
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=number + " уже участвует")
						if have != True:
								username.append(username2)
								markup4 = types.InlineKeyboardMarkup(row_width=2)
								start = types.InlineKeyboardButton("Начать", callback_data='start_to_the_center')
								cancel = types.InlineKeyboardButton("Отмена", callback_data='cancel')
								join = types.InlineKeyboardButton("Присоединиться", callback_data='join_center')
								markup4.add(start, cancel, join)
								check.append(number)
								bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Новая игра со ставкой: " + str(bet) + "\nПопади в центр\n" + "\n".join(check), reply_markup=markup4)
								id_check.append("{0.id}".format(call.from_user, bot.get_me()))
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="У вас недостаточно средств")
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(call.message.chat.id))
		cancel1()
bot.polling()