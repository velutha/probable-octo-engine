import base64

from db_store import save, get_val
class UrlShortener():

    # lookup_dict = {}

    def __init__(self):
        pass

    @classmethod
    def get_short_url(cls, url):

        shortcode = base64.b64encode(bytes(str(hash(url)), 'utf-8'))[-6:].decode('utf-8')
        shortcode = cls.get_unique_code(shortcode)
        is_saved = save(shortcode, url)
        # cls.lookup_dict[shortcode] = url
        return shortcode

    @classmethod
    def get_long_url(cls, key):
        url = get_val(key)
        # if key in cls.lookup_dict:
            # return cls.lookup_dict[key]
        return url

    @classmethod
    def get_unique_code(cls, code):
        if get_val(code):
            code = list(code)
            code[-1] += 1
            code = "".join(code)
            return cls.get_unique_code(code)
        return code
