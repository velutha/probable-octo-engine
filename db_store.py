import dbm

# storage1 = dbm.open('storage1', 'c')
# storage2 = dbm.open('storage2', 'c')

storage_map = {}


def save(key, val):

    hash_key = hash(key)
    storage = get_storage(hash_key)
    hash_key = str(hash_key)
    with dbm.open(storage, 'c') as db:
        db[hash_key] = val

    return True

def get_val(key):

    hash_key = hash(key)
    storage = get_storage(hash_key)
    hash_key = str(hash_key)
    with dbm.open(storage, 'c') as db:
        try:
            value = db[hash_key]
        except KeyError:
            value = None

    return value

def get_storage(hash_key):
    return 'storage1'
