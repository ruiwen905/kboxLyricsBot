from urllib.parse import quote as Url_Quote


class Formatter:
    @staticmethod
    def get_percent_encoding_from_string(string):
        encoded = Url_Quote(string, safe='')
        return encoded
