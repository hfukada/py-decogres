from postgresql import DatabasePool

class postgres(object):
    def __init__(self, **kwargs):
        self.db_args = kwargs
        self.db = DatabasePool.recall(**self.db_args)

    def __call__(self, db_call):
        def wrapped_db_call(*args, **kwargs):
            global_refs = db_call.func_globals
            key = self.db.name
            global_refs[key] = self.db
            return db_call(*args, **kwargs)
        return wrapped_db_call