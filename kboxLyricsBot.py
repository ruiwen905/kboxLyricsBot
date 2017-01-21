from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text(
        """"Hello {}, \nPlease enter the singer followed by the title of the song. \ne.g. the chainsmokers closer
        Other features includes:
        /hits -- view top 10 songs
        /artists -- view top artists
        
        /cancel - cancel the current operation """.format(update.message.from_user.first_name))

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('329555371:AAG6VH8AiLUJJCF5Vp1tGcJ6TFymho-_ArU')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()