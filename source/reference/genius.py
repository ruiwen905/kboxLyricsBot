import requests
from bs4 import BeautifulSoup
from utilities.keys import Keys
from utilities.formatter import Formatter
from songs.song import Song


# Ref: https://docs.genius.com/
class Genius:
    __MAIN_URL = 'https://genius.com/'
    __API_URL = 'https://api.genius.com/'

    @staticmethod
    def get_song_list(query):
        search_url = Genius.__API_URL + "search?access_token=" + Keys.GENIUS_CLIENT_ACCESS_TOKEN + "&q=" + Formatter.get_percent_encoding_from_string(query)
        json_obj = requests.get(search_url).json()
        results_arrray = json_obj['response']['hits']
        song_list = []
        for result in results_arrray:
            song = Genius.__make_song_object(result['result'])
            song_list.append(song)
        return song_list

    @staticmethod
    def __get_lyrics(lyrics_url):
        request_html_content = requests.get(lyrics_url).content
        soup_obj = BeautifulSoup(request_html_content, "html.parser")
        return soup_obj.find('div', class_='lyrics').text.strip()

    @staticmethod
    def __make_song_object(json_result):
        song_title = json_result['title']
        song_artist = json_result['primary_artist']['name']
        song_url = json_result['url']
        # song_lyrics = Genius.__get_lyrics(song_url)
        song_lyrics = song_url
        song_thumbnail = json_result['header_image_thumbnail_url']
        return Song(title=song_title, artist=song_artist, lyrics=song_lyrics, url=song_url, thumbnail_url=song_thumbnail)
