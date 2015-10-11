from postgresql import postgres

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test1b():
    return black 

@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2b():
    return psql

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/"})
@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test3b():
    return [psql, black]

@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test4b():
    with psql.cursor() as c:
        c.execute("SELECT 42 AS AMAZING")
    return c.fetchone()['AMAZING']


