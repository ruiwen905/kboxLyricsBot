from lyrics.lyrics_manager import LyricsManager


# Ref: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#CallbackQuery.data
class CallbackQueryManager:
    # Constants
    INSTRUCT_VIEW_YOUTUBE_PLAYLIST = "How-To-View-YouTube-Playlist"
    TOP_SONGS = "Top-songs"

    def __init__(self, bot, update):
        self.lyrics_manager = LyricsManager()
        self.bot = bot
        self.callback_query = update.callback_query

    def get_instuct_to_view_youtube_playlist(self):
        reply = """
        To get your youtube playlist, 
        1. Add @youtube
        2. Sign in to your youtube account by entering /auth 
        3. Enter /setting 
        4. Toggle to 'Suggest liked video' button
        5. Click 'Save & go to chat' button """
        self.callback_query.message.reply_text(reply)

    def get_top_songs(self):
        self.callback_query.message.reply_text(self.lyrics_manager.get_top_songs())

    def manage(self):
        if self.callback_query.data == self.TOP_SONGS:
            self.get_top_songs()
        elif self.callback_query.data == self.INSTRUCT_VIEW_YOUTUBE_PLAYLIST:
            self.get_instuct_to_view_youtube_playlist()
