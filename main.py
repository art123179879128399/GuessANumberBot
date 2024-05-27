import telebot
import random
import database
import PlayerData

BOT_KEY = "6752811972:AAE3gcqOz_S2-Fj0frrNjLmX9BkLGDFAj38"
bot = telebot.TeleBot(BOT_KEY)

kb_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = telebot.types.KeyboardButton("/start")
kb_start.add(start_button, row_width = 2)

kb_num = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

players = database.load()


def random_number(x):
    s = random.randint(0, x)
    return s

def get_player(id):
    if id not in players:
        players[id] = PlayerData.PlayerData()
        players[id].id = id 
    return players[id]

@bot.message_handler(commands=["start"])
def start(message):

    global players
    bot.send_message(message.chat.id, "chose the maximum number")
    get_player(message.from_user.id).times = 0
    get_player(message.from_user.id).start = True
    get_player(message.from_user.id).max_num = 0



    username = message.from_user.username
    print(username)

@bot.message_handler(func=lambda message: True)
def on_message(message):
    try:
        cur_player = get_player(message.from_user.id)
        if cur_player.start == False:
            bot.send_message(message.chat.id, "type /start pls")
            return
        if cur_player.max_num == 0:
            cur_player.max_num = int(message.text)
            cur_player.num = random_number(cur_player.max_num)
            kb_num = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in range(0, cur_player.max_num + 1):
                curr_button = telebot.types.KeyboardButton(str(i))
                kb_num.add(curr_button)
            
            bot.send_message(message.chat.id, "I have chosen the number, try to guess it", reply_markup=kb_num)
            return

        a = int(message.text) 
        if a ==cur_player.num:
            bot.send_message(message.chat.id, "Congratulations you won!!!!!!!!!!!!!!!!!!!!!!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉", reply_markup=kb_start)

            cur_player.wins += 1
            bot.send_message(message.chat.id, f"You tried {cur_player.times + 1} times")
            cur_player.times = 0
            cur_player.num = random_number(cur_player.max_num)
            bot.send_message(message.chat.id, f"you won {cur_player.wins} times and lost {cur_player.loses} times")
        else:
            bot.send_message(message.chat.id, "Try again you loser")
            cur_player.times += 1
            cur_player.loses += 1
        database.save(players)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "sorry something went wrong with the bot (: 🥲")

bot.infinity_polling()