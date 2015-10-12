# Decogres (python **Deco**rator for Post**gres**SQL)
## Description
This is a small module for maintaining connection pools for an application that connect to a single or connect to multiple databases.

## Motivation and Reasoning
Decorators are a crowd favorite for hiding silly things like global state. The idea is to be able to easily recall a database pool that you have already initialized, and continue to use the same pool as your code chugs along using a simple interface. The decorator makes it easy to see that a function touches a database and also implies a larger scope.

## Use Cases

Simple stuff like this.

```
@postgres(**{'name': 'ppp', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def get_42_from_the_database():
    with ppp.cursor() as c:
        c.execute("SELECT 42 AS AMAZING")
    return c.fetchone()['amazing']
```

```
@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
@postgres(**{'name': 'ppp', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def give_me_some_databases():
    return [ppp, black]

```

"WOW THAT'S AMAZING" You might say. You're not incorrect.

### Actual Documentation
the @postgres decorator can take the following keyword arguments
- connection_pool_type: a class of AbstractConnectionPool (defaults to ThreadedConnectionPool)
- connection_url: your postgres url (defaults to "postgresql://postgres:postgres@localhost/")
- name: the name of the connection (defualts to connection_url if not set. please set it)
- mincount: minimum number of connection pool connections (defaults to 2)
- maxcount: maximum number of connection pool connections (defaults to 40)
- cursor_factory: cursor factory to use when creating a cursor with cursor(). (defualts to RealDictCursor)

any other keywords can by found in the actualy [psycopg2.pool](http://initd.org/psycopg/docs/pool.html) page.

if I missed anything make a Pull request or something.
