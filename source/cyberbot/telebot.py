from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from cyberbot.callbackquery_manager import CallbackQueryManager


class Telebot:
    def __init__(self, bot_token):
        self.token = bot_token
        self.callback_query_manager = None
        self.command_manager = None

    def command_start(self, bot, update):
        start_message = """Hello {}
        Please enter the singer followed by the title of the song. 
        e.g. the chainsmokers closer"""
        keyboard = [[InlineKeyboardButton("Top Songs", callback_data=CallbackQueryManager.TOP_SONGS)],
                    [InlineKeyboardButton("How to view YouTube Playlist", callback_data=CallbackQueryManager.INSTRUCT_VIEW_YOUTUBE_PLAYLIST)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(start_message.format(update.message.from_user.first_name), reply_markup=reply_markup)

    def display(self, bot, update):
        update.message.reply_text("Sorry, we are undergoing maintenance. Please come back later.")

    def manage_callbacks(self, bot, update):
        self.callback_query_manager = CallbackQueryManager(bot, update)
        self.callback_query_manager.manage()

    def run_update(self):
        updater = Updater(self.token)

        # Command Handlers
        updater.dispatcher.add_handler(CommandHandler('start', self.command_start))

        # Message Handler
        updater.dispatcher.add_handler(MessageHandler(Filters.text, self.display))

        # Callback Handler
        updater.dispatcher.add_handler(CallbackQueryHandler(self.manage_callbacks))

        updater.start_polling()
        updater.idle()
