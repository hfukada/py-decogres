import psycopg2
import inspect
from functools import wraps

from contextlib import contextmanager

from psycopg2 import pool
from psycopg2.extras import RealDictCursor


def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

class DatabasePool:
    """
    Creates and manages a pool of connections to a database.
    - connection_pool_type is an AbstractConnectionPool
    - name is an optional nickname for the database connection
    - connection_url is a postgresql://user@host/database style DSN
    - mincount is the minimum number of connections to keep open
    - maxcount is the maximum number of connections to have open
    - cursor_factory defines the factory used for inflating database rows
    """
    def __init__(self, connection_pool_type=pool.ThreadedConnectionPool, connection_url="postgresql://postgres:postgres@localhost/", \
            name=None, mincount=2, maxcount=40, cursor_factory=RealDictCursor, **kwargs):
        self.connection_url = connection_url
        self.name = name or connection_url
        self._pool = connection_pool_type(mincount, maxcount, connection_url, cursor_factory=cursor_factory, **kwargs)

    @classmethod
    @memoize
    def recall(cls, **kwargs):
        return cls(**kwargs)

    def __repr__(self):
        return "<%d: %s: %s>" %(id(self), self.__class__.__name__, self.name)

    def __del__(self):
        self._pool.closeall()

    def __attempt_connect(self, retry=True):
        try:
            return self._pool.getconn()
        except psycopg2.DatabaseError, psycopg2.OperationalError:
            if retry:
                return self.__attempt_connect(retry=False)
            else:
                raise RuntimeError('Could not get a connection to: {}'.format(self.name))

    @contextmanager
    def cursor(self, commit_on_close=False):
        con = self.__attempt_connect()

        try:
            yield con.cursor()
            if commit_on_close:
                con.commit()
        except pool.PoolError as e:
            logging.log(logging.ERROR, e.message)
        finally:
            try:
                self._pool.putconn(con)
            except psycopg2.pool.PoolError as e:
                logging.warn(e.message)
