from telegram import InlineQueryResult, InlineQueryResultArticle
from telegram import InputTextMessageContent
from lyrics.lyrics_manager import LyricsManager


# Ref: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinequery.html
class InlineQueryManager:

    def __init__(self, bot, update):
        self.lyrics_manager = LyricsManager()
        self.bot = bot
        self.inline_query = update.inline_query

    def manage(self):
        song_to_search = self.inline_query.query
        # result_display_list = self.lyrics_manager.get_list_lyrics_with_song_title(song_to_search)
        # result_display_list.append(InlineQueryResultArticle(id='1', title="title1", input_message_content=InputTextMessageContent('Thanks for visit me'), url='http://telegram.org', description='Subtitle 1', thumb_url='https://telegram.org/img/t_logo.png', thumb_height=640, thumb_width=640))
        result_display_list = []
        result_display_list.append(InlineQueryResultArticle(id='1', title="title1", input_message_content=InputTextMessageContent(self.lyrics_manager.temp_method(song_to_search)), url=self.lyrics_manager.temp_method(song_to_search), description='Your_Song', thumb_url='https://telegram.org/img/t_logo.png', thumb_height=640, thumb_width=640))
        self.inline_query.answer(results=result_display_list)
