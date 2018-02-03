from bs4 import BeautifulSoup
import requests
from utilities.formatter import Formatter


class MusicMatch:

    MAIN_URL = "https://www.musixmatch.com/"
    TOP_SONGS_URL = "https://www.musixmatch.com/explore"
    SEARCH_URL = "https://www.musixmatch.com/search/"

    @staticmethod
    def get_soup_object(url):
        request_result = requests.get(url)
        request_html_content = request_result.content
        print('html', request_html_content)
        soup_obj = BeautifulSoup(request_html_content, "html.parser")
        return soup_obj

    # def generate_site_from_input(self, message):
    #     input_message = message
    #     input_message_trim = input_message.strip()
    #     processed_message = input_message_trim.replace(' ', '-')
    #
    #     final_url = self.url + processed_message + "-lyrics"
    #     return final_url
    #
    # def get_raw_lyrics(self, message):
    #     final_url = self.generate_site_from_input(message)
    #     soup = self.get_soup_object(final_url)
    #     raw_lyrics = soup.lyrics
    #     return raw_lyrics
    #
    # def display_lyrics(self, message):
    #     raw_lyrics = self.get_raw_lyrics(message)
    #     for tag in raw_lyrics.find_all('a'):
    #         tag.replaceWith(tag.text)
    #     final_lyrics = raw_lyrics.get_text().rstrip()
    #     return final_lyrics

    # @staticmethod
    # def get_list_lyrics_with_song_title(song_title):
    #     url__of_site_to_scrap = MusicMatch.SEARCH_URL + Formatter.get_percent_encoding_from_string(song_title)
    #     soup = MusicMatch.get_soup_object(url__of_site_to_scrap)
    #     # print(soup)
    #     return url__of_site_to_scrap
    #
    # @staticmethod
    # def temp_method(song_name):
    #     return MusicMatch.SEARCH_URL + Formatter.get_percent_encoding_from_string(song_name)
