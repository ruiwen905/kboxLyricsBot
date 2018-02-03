import requests
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
        # featured_list = []
        song_list = []
        for result in results_arrray:
            # genius_song_id = result['result']['id']
            song = Genius.__make_song_object(result['result'])
            song_list.append(song)
        return song_list

    @staticmethod
    def __is_genius_song_featured(song_id):
        genius_song = Genius.__get_genius_song(song_id)
        if genius_song['featured_video'] == "true":
            return True
        else:
            return False

    @staticmethod
    def __get_genius_song(song_id):
        song_search_url = Genius.__API_URL + "songs?access_token=" + Keys.GENIUS_CLIENT_ACCESS_TOKEN + "&id=" + song_id
        json_obj = requests.get(song_search_url).json()
        print(song_search_url)
        print(json_obj)
        print("json song: ", json_obj['response']['song'])
        return json_obj['response']['song']

    @staticmethod
    def __make_song_object(json_result):
        song_title = json_result['title']
        song_artist = json_result['primary_artist']['name']
        song_lyrics = json_result['path']
        song_url = json_result['url']
        song_thumbnail = json_result['header_image_thumbnail_url']
        return Song(title=song_title, artist=song_artist, lyrics=song_lyrics, url=song_url, thumbnail_url=song_thumbnail)
