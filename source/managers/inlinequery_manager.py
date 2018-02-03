from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent
from reference.reference_manager import ReferenceManager


# Ref: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinequery.html
class InlineQueryManager:
    def __init__(self, bot, update):
        self.bot = bot
        self.inline_query = update.inline_query

    def manage(self):
        song_to_search = self.inline_query.query
        result_song_list = ReferenceManager.get_song_list(song_to_search)
        result_display_list = []
        i = 0
        for song in result_song_list:
            result_display_list.append(InlineQueryResultArticle(id=i, title=song.title, input_message_content=InputTextMessageContent(song.url), url=song.url, description=song.artist, thumb_url=song.thumbnail_url, thumb_height=640, thumb_width=640))
            i += 1
        self.inline_query.answer(results=result_display_list)
