from decogres.decorator import postgres

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test1b():
    return black 

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/"})
@postgres(**{'name': 'postgresql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2b():
    return [postgresql, black]

@postgres(**{'name': 'postgresql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test4b():
    with postgresql.cursor() as c:
        c.execute("SELECT 42 AS AMAZING")
    return c.fetchone()['AMAZING']


