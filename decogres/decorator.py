from postgresql import DatabasePool
from pprint import pprint

cache = {}

class postgres(object):
    def __init__(self, *args, **kwargs):
        key = hash(str(args) + str(kwargs))
        if key not in cache:
            cache[key] = DatabasePool(*args, **kwargs)
        self.db_name = kwargs['name']
        self.db = cache[key]

    def __call__(self, db_call):
        def wrapped_db_call(*args, **kwargs):
            global_refs = db_call.func_globals
            key = self.db.name
            global_refs[key] = self.db
            return db_call(*args, **kwargs)
        return wrapped_db_call

#@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
#def test1a():
#    return black
#
#@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
#@postgres(**{'name': 'ppp', 'connection_url': "postgresql://postgres:postgres@localhost/"})
#def test2a():
#    return [ppp, black]
#print test1a()
#print test2a()
