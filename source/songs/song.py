
class Song(object):
    def __init__(self, title, artist="Unknown", description=None, lyrics=None, year=None, url=None, thumbnail_url=None, genre=None):
        self.__title = title
        self.__artist = artist
        self.__description = description
        self.__lyrics = lyrics
        self.__year = year
        self.__url = url
        self.__thumbnail_url = thumbnail_url
        self.__genre = genre

    # --- Properties ---
    @property
    def title(self):
        return self.__title

    @property
    def artist(self):
        return self.__artist

    @property
    def description(self):
        return self.__description

    @property
    def lyrics(self):
        return self.__lyrics

    @property
    def year(self):
        return self.__year

    @property
    def url(self):
        return self.__url

    @property
    def thumbnail_url(self):
        return self.__thumbnail_url

    @property
    def genre(self):
        return self.__genre

    # --- Setter ---
    @title.setter
    def title(self, title):
        self.__title = title

    @artist.setter
    def artist(self, artist):
        self.__artist = artist

    @description.setter
    def description(self, description):
        self.__description = description

    @lyrics.setter
    def lyrics(self, lyrics):
        self.__lyrics = lyrics

    @year.setter
    def year(self, year):
        self.__year = year

    @url.setter
    def url(self, url):
        self.__url = url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        self.__thumbnail_url = thumbnail_url

    @genre.setter
    def genre(self, genre):
        self.__genre = genre
