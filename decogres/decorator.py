from postgresql import DatabasePool
from pprint import pprint

class postgres(object):
    def __init__(self, *args, **kwargs):
        self.db_args = kwargs
        self.db = DatabasePool.recall(*args, **self.db_args)

    def __call__(self, db_call):
        def wrapped_db_call(*args, **kwargs):
            global_refs = db_call.func_globals
            key = self.db.name
            global_refs[key] = self.db
            return db_call(*args, **kwargs)
        return wrapped_db_call

#@postgres(**{'name': 'ppp', 'connection_url': "postgresql://postgres:postgres@localhost/"})
#@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
#def test2a():
#    print 'ppp ' + str(ppp) + ' black ' + str(black)
#    return [ppp, black]
#
#test2a()
