import dbm
import sys

class DB():

    def save(self, key, val):

        hash_key = hash(key)
        storage = self.get_storage(hash_key)
        hash_key = str(hash_key)
        with dbm.open(storage, 'c') as db:
            db[hash_key] = val

        return True

    def get_val(self, key):

        hash_key = hash(key)
        storage = self.get_storage(hash_key)
        hash_key = str(hash_key)
        with dbm.open(storage, 'c') as db:
            try:
                value = db[hash_key]
            except KeyError:
                value = None

        return value

    def get_storage(self, hash_key):
        storages = ['storage1', 'storage2']

        if hash_key in range(-sys.maxsize, 1):
            return storages[0]
        elif hash_key in range(0, sys.maxsize + 1):
            return storages[1]
