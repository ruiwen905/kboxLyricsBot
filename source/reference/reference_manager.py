from reference.genius import Genius


class ReferenceManager:

    @staticmethod
    def get_song_list(song_title):
        return Genius.get_song_list(song_title)
