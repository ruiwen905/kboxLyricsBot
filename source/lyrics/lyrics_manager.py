from lyrics.musicmatch_site import MusicMatch


class LyricsManager:

    def get_top_songs(self):
        return "NIL"

    def get_list_lyrics_with_song_title(self, song_title):
        return MusicMatch.get_list_lyrics_with_song_title(song_title)

    def display_lyrics(self, message):
        return "XXX"
        # return MusicMatch.display_lyrics(message)

    def temp_method(self, song_title):
        url = MusicMatch.temp_method(song_title)
        print(url)
        return url
