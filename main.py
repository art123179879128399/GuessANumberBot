import telebot
import random
import database
import PlayerData
BOT_KEY = "6752811972:AAE3gcqOz_S2-Fj0frrNjLmX9BkLGDFAj38"
bot = telebot.TeleBot(BOT_KEY)
players = database.load()

def random_number(x):
    s = random.randint(1, x + 1)
    return s

def get_player(id):
    if id not in players:
        players[id] = PlayerData.PlayerData()
        players[id].id = id 
    return players[id]


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "chose the maximum number")


    global players
    # get_player(message.from_user.id).num = random_number(6)
    get_player(message.from_user.id).times = 0
    # bot.send_message(message.chat.id, "hey lets play a game: try to guess my number")
    get_player(message.from_user.id).start = True
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
            cur_player.max_num == int(message.text)
            cur_player.num = random_number(cur_player.max_num)
            bot.send_message(message.chat.id, "I have cose the number try to guess it")
            return

        a = int(message.text) 
        if a ==cur_player.num:
            bot.send_message(message.chat.id, "Congratulations you won!!!!!!!!!!!!!!!!!!!!!!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
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
