import telebot
import config
import time
from telebot import types
from telegram.ext.dispatcher import run_async
import sqlite3






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
		if answer == []:
			bot.send_message(message.chat.id, "Hi")
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
			markup1 = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Deposit", callback_data='deposit')
			item2 = types.InlineKeyboardButton("Withdraw", callback_data='withdraw')
			markup1.add(item1, item2)
			bot.send_message(message.chat.id, "Your balance: "+ str(balance1[0]), reply_markup=markup1)
		else:
			bot.send_message(message.chat.id, "<b>{0.first_name}</b> balance: ".format(message.from_user, bot.get_me()) + str(balance1[0]), parse_mode='html')
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))

@bot.message_handler(commands=['new_game'])
def game(message):
	try:
				if str(message.chat.id) == str(config.chat_id):
					if message.chat.type == 'private':
						bot.send_message(message.chat.id, "Find friends until we finish solo mode")
					else:
						global gameee
						if bet1 == []:
							GET_LEN = 10
							global bet
							bet = message.text[GET_LEN:]
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
									gameee = message
									markup2 = types.InlineKeyboardMarkup(row_width=2)
									item1 = types.InlineKeyboardButton("Guess the number", callback_data="number")
									item2 = types.InlineKeyboardButton("Who is bigger", callback_data="bigger")
									item3 = types.InlineKeyboardButton("Cancel", callback_data="cancel")
									markup2.add(item1, item2, item3)
									bot.send_message(message.chat.id, "Choose a game", reply_markup=markup2)
									global gamee
									gamee = message.message_id
								else:
									bot.send_message(message.chat.id, 'You have no money')
							else:
								bot.send_message(message.chat.id, "Wrong format\nPlease send: /new_game <value>")
						else:
							bot.reply_to(gameee, "Game already start")
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))

@bot.message_handler(commands=['give'])
def give(message):
	try:
		if message.chat.type == "supergroup":
			user_call = "{0.id}".format(message.from_user, bot.get_me())
			give_id = message.reply_to_message.from_user.id
			give_id_id = [give_id]
			if user_call == config.creator_id:
				if message.text[6:].isdigit() == True and 0 <= int(message.text[6:]) and message.text[6:] != "":
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
					give_bet = int(balance) + int(message.text[6:])
					give_bet_bet = [int(give_bet), give_id]
					curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_bet_bet)
					bd.commit()
					curs.close()
					bd.close()
					bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + " new balance: "  + str(give_bet))
			else:
				if message.text[6:].isdigit() == True and 0 <= int(message.text[6:]) and message.text[6:] != "":
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
						give_bet = int(balance) + int(message.text[6:])
						give_bet_bet = [int(give_bet), give_id]
						curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_bet_bet)
						curs.execute('SELECT user_balance FROM balance WHERE id = ?', give_id_id1)
						balance = curs.fetchall()
						balance1 = balance[0]
						balance = balance1[0]
						give_bet = int(balance) - int(message.text[6:])
						give_bet_bet1 = [int(give_bet), int(message.from_user.id)]
						curs.execute('UPDATE balance SET user_balance = ? WHERE id = ?', give_bet_bet1)
						bd.commit()
						curs.close()
						bd.close()
					else:
						bot.send_message(message.chat.id, 'You have no money')
				else:
					bot.send_message(message.chat.id, 'Wrong format\nPlease send: /give <value>')
		else:
			bot.send_message(message.chat.id, 'Please make chat a supergroup')
	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(message.chat.id))


@run_async
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
				user_call = "{0.id}".format(call.from_user, bot.get_me())
				if call.data == 'number':
					if user_call == user1:
						if call.message.message_id != gamee:
							markup3 = types.InlineKeyboardMarkup(row_width=3)
							number1 = types.InlineKeyboardButton("1", callback_data='1')
							number2 = types.InlineKeyboardButton("2", callback_data='2')
							number3 = types.InlineKeyboardButton("3", callback_data='3')
							number4 = types.InlineKeyboardButton("4", callback_data='4')
							number5 = types.InlineKeyboardButton("5", callback_data='5')
							number6 = types.InlineKeyboardButton("6", callback_data='6')
							start = types.InlineKeyboardButton("Start", callback_data='start_number')
							cancel = types.InlineKeyboardButton("Cancel", callback_data='cancel')
							markup3.add(number1, number2, number3, number4, number5, number6, start, cancel)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="New game with bet: " + str(bet) +"\nChoose your number", reply_markup=markup3)
						else:
							bot.edit_message_text(call.message.chat.id, call.message.message_id, "Game already start")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + ' is start this game')

				if call.data == 'start_number' :
					if user_call == user1 or user_call == config.creator_id or bot.get_chat_member(call.message.chat.id, call.message.from_user.id).status == "creator" or bot.get_chat_member(call.message.chat.id, call.message.from_user.id).status  == "administrator":
						if len(username) == 0 or len(username) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Few participants")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=None)
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
									time.sleep(1)
								else:
									have = False
							time.sleep(1)
							for i in range(len(lst)):
								if lst[i] == check[i] + ": " + str(dice_value):
									winner.append(check[i])
									id_winner.append(id_check[i])
							time.sleep(5)
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
							bot.send_message(call.message.chat.id, "Winners:\n " +"\n".join(winner) + "\n Winners receive " + str(pool))
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
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + ' is start this game')

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
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text= number + ' is already participating')
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
							start = types.InlineKeyboardButton("Start", callback_data='start_number')
							cancel = types.InlineKeyboardButton("Cancel", callback_data='cancel')
							markup3.add(number1, number2, number3, number4, number5, number6, start, cancel)
							lst.append(number + ": " + call.data)
							id_check.append(username2)
							wagger.append(call.data)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="New game with bet: " + str(bet) + "\nChoose your number\n" + "\n".join(lst), reply_markup=markup3)
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='You have no money')

				elif call.data =="bigger":
					if user_call == user1:
						if call.message.message_id != gamee:
							markup4 = types.InlineKeyboardMarkup(row_width=2)
							start = types.InlineKeyboardButton("Start", callback_data='start_bigger')
							cancel = types.InlineKeyboardButton("Cancel", callback_data='cancel')
							join = types.InlineKeyboardButton("Join", callback_data='join')
							markup4.add(start, cancel, join)
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="New game with bet: " + str(bet) + "\nWho will have more", reply_markup=markup4)
							lst.clear()
							winner.clear()
							check.clear()
							username.clear()
						else:
							bot.edit_message_text(call.message.chat.id, call.message.message_id, "Game already start")
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + ' is start this game')

				elif call.data == 'start_bigger':
					if user_call == user1 or user_call == config.creator_id or bot.get_chat_member(call.message.chat.id, call.message.from_user.id).status == "creator" or bot.get_chat_member(call.message.chat.id, call.message.from_user.id).status  == "administrator":
						if len(check) == 0 or len(check) == 1:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Few participants")
						else:
							bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="New game with bet: " + str(bet) + "\nWho will have more\n" + "\n".join(check), reply_markup=None)
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
									bot.send_message(call.message.chat.id, check[i] + " rolls dice")
									summ = 0
									for j in range(3):
										throw_cube = bot.send_dice(call.message.chat.id)
										dice_value = throw_cube.dice.value
										time.sleep(5)
										summ = summ + dice_value
									lst.append(check[i] + ": " + str(summ))
									if summ > max:
										max = summ
										winner.clear()
										id_winner.clear()
										winner.append(check[i])
										id_winner.append(id_check[i])
									time.sleep(1)
									bot.send_message(call.message.chat.id, check[i] + " threw a total of " + str(summ))
									time.sleep(1)
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
							bot.send_message(call.message.chat.id, "Results:\n" + "\n".join(lst))
							time.sleep(2)
							bot.send_message(call.message.chat.id, "\nWinners:\n" + "\n".join(winner) + "\nWinners receive " + str(pool))
							lst.clear()
							check.clear()
							winner.clear()
							wagger.clear()
							username.clear()
							id_winner.clear()
							id_check.clear()
							bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + ' is start this game')

				if call.data == 'cancel':
					if user_call == user1 or user_call == config.creator_id or bot.get_chat_member(call.message.chat.id, call.message.from_user.id).status == "creator" or bot.get_chat_member(call.message.chat.id, call.message.from_user.id).status  == "administrator":
						bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Game has been canceled", reply_markup=None)
						lst.clear()
						check.clear()
						winner.clear()
						wagger.clear()
						username.clear()
						id_winner.clear()
						id_check.clear()
						bet1.clear()
					else:
						bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=first_name + ' is start this game')

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
								bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=number + ' is already participating')
						if have != True:
								username.append(username2)
								markup4 = types.InlineKeyboardMarkup(row_width=2)
								start = types.InlineKeyboardButton("Start", callback_data='start_bigger')
								cancel = types.InlineKeyboardButton("Cancel", callback_data='cancel')
								join = types.InlineKeyboardButton("Join", callback_data='join')
								markup4.add(start, cancel, join)
								check.append(number)
								bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="New game with bet: " + str(bet) + "\nWho will have more\n" + "\n".join(check), reply_markup=markup4)
								id_check.append("{0.id}".format(call.from_user, bot.get_me()))
					else:
							bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='You have no money')

	except Exception as e:
		bot.send_message(config.creator_id, "Error:\n" + str(e) + "\n" + "chat_id: " + str(call.message.chat.id))




bot.polling()