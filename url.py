import base64

from db_store import DB
class UrlShortener():

    # lookup_dict = {}

    def __init__(self):
        self.db = DB()

    def get_short_url(self, url):

        shortcode = base64.b64encode(bytes(str(hash(url)), 'utf-8'))[-6:]
        shortcode = self.get_unique_code(shortcode)
        shortcode = shortcode.decode('utf-8')
        is_saved = self.db.save(shortcode, url)
        # cls.lookup_dict[shortcode] = url
        return shortcode

    def get_long_url(self, key):
        url = self.db.get_val(key)
        # if key in cls.lookup_dict:
            # return cls.lookup_dict[key]
        return url

    def get_unique_code(self, code):
        if self.db.get_val(code):
            code = list(code)
            code[-1] += 1
            code = "".join(code)
            return self.get_unique_code(code)
        return code
