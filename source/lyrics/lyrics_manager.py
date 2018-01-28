from lyrics.musicmatch_site import MusicMatch


class LyricsManager:
    UNKNOWN_LYRICS_SOURCE = "UNKNOWN"

    def get_top_songs(self):
        return "NIL"

    def display_lyrics(self, message):
        music_match = MusicMatch()
        return music_match.display_lyrics(message)
