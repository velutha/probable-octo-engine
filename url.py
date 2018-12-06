import base64
class UrlShortener():

    lookup_dict = {}

    def __init__(self):
        pass

    @classmethod
    def get_short_url(cls, url):

        shortcode = base64.b64encode(bytes(str(hash(url)), 'utf-8'))[-6:].decode('utf-8')
        shortcode = cls.get_unique_code(shortcode)
        cls.lookup_dict[shortcode] = url
        return shortcode

    @classmethod
    def get_long_url(cls, key):
        if key in cls.lookup_dict:
            return cls.lookup_dict[key]
        return None

    @classmethod
    def get_unique_code(cls, code):
        if code in cls.lookup_dict.keys():
            code = list(code)
            code[-1] += 1
            code = "".join(code)
            return cls.get_unique_code(code)
        return code
