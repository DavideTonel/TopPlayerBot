import telebot
import logging
from config import TOKEN

from telebot import types

from soccer.Tournament import Tournament
from soccer.Match import MatchBuilder

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

tournament = Tournament()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def store_players(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Chi gioca?')
    bot.register_next_step_handler(msg, process_names)


def process_names(message):
    chat_id = message.chat.id
    try:
        text = message.text
        names = text.replace(' ','').split(',')
        tournament.setPlayers(names)

    except Exception as e:
        print(e)
        msg = bot.send_message(chat_id, 'Inserimento non valido, scrivi il nome di ogni giocatore separato da una virgola')
        bot.register_next_step_handler(msg, process_names)
    else:
        msg = bot.send_message(chat_id, 'CHE IL TORNEO ABBIA INIZIO')


@bot.message_handler(commands=['match'])
def store_match(message):
    chat_id = message.chat.id
    matchBuilder = MatchBuilder()

    #show all players' buttons
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in tournament.getPlayerNames():
        keyboard.add(types.KeyboardButton(name))

    msg = bot.send_message(chat_id, 'Chi è il primo giocatore?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, store_player1, matchBuilder)
    
def store_player1(message, matchBuilder : MatchBuilder):
    chat_id = message.chat.id

    try:
        matchBuilder.setPlayer1(tournament.getPlayerByName(message.text))
    except:
        msg = bot.send_message(chat_id, 'Inserimento non valido, riprova')
        bot.register_next_step_handler(msg, store_player1, matchBuilder)
    else:
        msg = bot.send_message(chat_id, 'Chi è il secondo giocatore?')
        bot.register_next_step_handler(msg, store_player2, matchBuilder)

def store_player2(message, matchBuilder : MatchBuilder):
    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardRemove(selective=False)

    try:
        matchBuilder.setPlayer2(tournament.getPlayerByName(message.text))
    except:
        msg = bot.send_message(chat_id, 'Inserimento non valido, riprova')
        bot.register_next_step_handler(msg, store_player2, matchBuilder, keyboard)
    else:
        msg = bot.send_message(chat_id, 'Quanti goal ha segnato ' + matchBuilder.p1.getName() + '?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, store_score_player1, matchBuilder)

def store_score_player1(message, matchBuilder : MatchBuilder):
    chat_id = message.chat.id
    try:
        matchBuilder.setScorePlayer1(int(message.text))
    except:
        msg = bot.send_message(chat_id, 'Inserimento non valido, riprova')
        bot.register_next_step_handler(msg, store_score_player1, matchBuilder)
    else:
        msg = bot.send_message(chat_id, 'Quanti goal ha segnato ' + matchBuilder.p2.getName() + '?')
        bot.register_next_step_handler(msg, store_score_player2, matchBuilder)

def store_score_player2(message, matchBuilder : MatchBuilder):
    chat_id = message.chat.id
    try:
        matchBuilder.setScorePlayer2(int(message.text))
    except:
        msg = bot.send_message(chat_id, 'Inserimento non valido, riprova')
        bot.register_next_step_handler(msg, store_score_player2, matchBuilder)
    else:
        status = addMatchInTorunament(matchBuilder)
        if status:
            msg = bot.send_message(chat_id, 'Match salvato')

def addMatchInTorunament(matchBuilder : MatchBuilder):
    try:
        tournament.addMatch(matchBuilder.build())
    except Exception as e:
        print(e)
        return False
    else:
        return True

@bot.message_handler(commands=['reset'])
def reset_tournament(message):
    chat_id = message.chat.id
    tournament.reset()
    msg = bot.send_message(chat_id, 'Torneo concluso')

@bot.message_handler(commands=['ranking'])
def show_rank(message):
    chat_id = message.chat.id
    ranking = tournament.getRanking()
    if len(ranking) == 0:
        msg = bot.send_message(chat_id, 'Non ci sono dei match da giudicare')
    else:
        position = 1
        ranking_str = '\n'
        for player in ranking:
            ranking_str += str(position) + '\t' + str(player.name) + '\t' + str(player.score) + '\t' + str(player.getGoalDifference())
            ranking_str += '\n'
            position += 1
        msg = bot.send_message(chat_id, ranking_str)

@bot.message_handler(commands=['awards'])
def awards(message):
    chat_id = message.chat.id
    ranking = tournament.getRanking()

    position = 1
    ranking_str = '\n'
    for player in ranking:
        ranking_str += str(position) + '\t' + str(player.name) + '\t' + str(player.score) + '\t' + str(player.getGoalDifference())
        ranking_str += '\n'
        position += 1
    msg = bot.send_message(chat_id, ranking_str)

    # no need to remember data
    reset_tournament(message)



bot.infinity_polling()
