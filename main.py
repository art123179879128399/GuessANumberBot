import telebot
import random
import database
import PlayerData
BOT_KEY = "6752811972:AAE3gcqOz_S2-Fj0frrNjLmX9BkLGDFAj38"
bot = telebot.TeleBot(BOT_KEY)
players = database.load()

def random_number(x):
    s = random.randint(1, x + 1)
    return 

def get_player_id(id):
    if id not in players:
        players[id] = PlayerData()
    return players[id]


@bot.message_handler(commands=["start"])
def start(message):
    global players
    players[message.from_user.id].num = random_number(6)
    players[message.from_user.id].times = 0
    bot.send_message(message.chat.id, "hey lets play a game: try to guess my number")
    username = message.from_user.username
    print(username)

@bot.message_handler(func=lambda message: True)
def on_message(message):
    try:
        a = int(message.text) 
        if a == players[message.from_user.id].num:
            bot.send_message(message.chat.id, "Congratulations you won!!!!!!!!!!!!!!!!!!!!!!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            players[message.from_user.id].wins += 1
            bot.send_message(message.chat.id, f"You tried {players[message.from_user.id].times + 1} times")
            players[message.from_user.id].times = 0
            players[message.from_user.id].num = random_number(6)
            bot.send_message(message.chat.id, f"you won {players[message.from_user.id].wins} times and lost {players[message.from_user.id].loses} times")
        else:
            bot.send_message(message.chat.id, "Try again you loser")
            players[message.from_user.id].times += 1
            players[message.from_user.id].loses += 1
        database.save(players)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "sorry something went wrong with the bot (: 🥲")




bot.infinity_polling()
