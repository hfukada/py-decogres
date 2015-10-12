from decogres.decorator import postgres

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
def test1b():
    return black 

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
@postgres(**{'name': 'ppp', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2b():
    return [ppp, black]

@postgres(**{'name': 'ppp', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test4b():
    with ppp.cursor() as c:
        c.execute("SELECT 42 AS AMAZING")
    return c.fetchone()['amazing']



