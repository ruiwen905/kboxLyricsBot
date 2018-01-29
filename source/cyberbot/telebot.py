from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, InlineQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from managers.callbackquery_manager import CallbackQueryManager
from managers.inlinequery_manager import InlineQueryManager


class Telebot:
    def __init__(self, bot_token):
        self.token = bot_token
        self.callback_query_manager = None

    def command_start(self, bot, update):
        start_message = """Hello {}
        Please enter the singer followed by the title of the song. 
        e.g. the chainsmokers closer"""
        keyboard = [[InlineKeyboardButton("Top Songs", callback_data=CallbackQueryManager.TOP_SONGS)],
                    [InlineKeyboardButton("How to view YouTube Playlist", callback_data=CallbackQueryManager.INSTRUCT_VIEW_YOUTUBE_PLAYLIST)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(start_message.format(update.message.from_user.first_name), reply_markup=reply_markup)

    def display(self, bot, update):
        update.message.reply_text("Type @kboxlyricsbot <song_name>")

    def manage_callbacks(self, bot, update):
        callback_query_manager = CallbackQueryManager(bot, update)
        callback_query_manager.manage()

    def manage_inline_queries(self, bot, update):
        inline_query_manager = InlineQueryManager(bot, update)
        inline_query_manager.manage()

    def run_update(self):
        updater = Updater(self.token)

        # Command Handlers
        updater.dispatcher.add_handler(CommandHandler('start', self.command_start))

        # Message Handler
        updater.dispatcher.add_handler(MessageHandler(Filters.text, self.display))

        # Callback Handler
        updater.dispatcher.add_handler(CallbackQueryHandler(self.manage_callbacks))

        # Inline Query Handler
        updater.dispatcher.add_handler(InlineQueryHandler(self.manage_inline_queries))

        updater.start_polling()
        updater.idle()
