import decorator

@decorator.postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test1b():
    return black 

@decorator.postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2b():
    return psql

@decorator.postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/"})
@decorator.postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test3b():
    return [psql, black]

@decorator.postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test4b():
    with psql.cursor() as c:
        c.execute("SELECT 42 AS AMAZING")
    return c.fetchone()['AMAZING']


