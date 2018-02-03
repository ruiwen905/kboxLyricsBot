from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler, InlineQueryHandler, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from managers.callbackquery_manager import CallbackQueryManager
from managers.inlinequery_manager import InlineQueryManager


class Telebot:
    def __init__(self, bot_token):
        self.token = bot_token
        self.callback_query_manager = None

    def __command_start(self, bot, update):
        start_message = """Hello {}, 
        \nTo start a search, type: @kboxlyricsbot<space><song-title><artist>
        \ne.g. @kboxlyricsbot the chainsmoker
        \ne.g. @kboxlyricsbot the chainsmoker closer"""
        keyboard = [[InlineKeyboardButton("How to view YouTube Playlist", callback_data=CallbackQueryManager.INSTRUCT_VIEW_YOUTUBE_PLAYLIST)],
                    [InlineKeyboardButton("Search in chat", callback_data=CallbackQueryManager.SEARCH)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(start_message.format(update.message.from_user.first_name), reply_markup=reply_markup)

    def __manage_callbacks(self, bot, update):
        callback_query_manager = CallbackQueryManager(bot, update)
        callback_query_manager.manage()

    def __manage_inline_queries(self, bot, update):
        inline_query_manager = InlineQueryManager(bot, update)
        inline_query_manager.manage()

    def run_update(self):
        updater = Updater(self.token)

        # Command Handlers
        updater.dispatcher.add_handler(CommandHandler('start', self.__command_start))

        # Message Handler
        # updater.dispatcher.add_handler(MessageHandler(Filters.text, self.display))

        # Callback Handler
        updater.dispatcher.add_handler(CallbackQueryHandler(self.__manage_callbacks))

        # Inline Query Handler
        updater.dispatcher.add_handler(InlineQueryHandler(self.__manage_inline_queries))

        updater.start_polling()
        updater.idle()
