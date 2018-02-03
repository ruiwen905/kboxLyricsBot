from reference.reference_manager import ReferenceManager


# Ref: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#CallbackQuery.data
class CallbackQueryManager:
    # Constants
    INSTRUCT_VIEW_YOUTUBE_PLAYLIST = "How-To-View-YouTube-Playlist"
    SEARCH = "Search"

    def __init__(self, bot, update):
        self.reference_manager = ReferenceManager()
        self.bot = bot
        self.callback_query = update.callback_query

    def __get_instuct_to_view_youtube_playlist(self):
        reply = """To get your youtube playlist,
        \n1. Add @youtube
        \n2. Sign in to your youtube account by entering /auth 
        \n3. Enter /setting 
        \n4. Toggle to 'Suggest liked video' button
        \n5. Click 'Save & go to chat' button """
        self.callback_query.message.reply_text(reply)
        self.callback_query.answer()

    def __search(self):
        self.callback_query.message.reply_text("Currently nothing, just a button")
        self.callback_query.answer()

    def manage(self):
        if self.callback_query.data == self.SEARCH:
            self.__search()
        elif self.callback_query.data == self.INSTRUCT_VIEW_YOUTUBE_PLAYLIST:
            self.__get_instuct_to_view_youtube_playlist()
