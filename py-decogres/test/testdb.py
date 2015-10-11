from postgresql import postgres

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
def test1a():
    print 'test1a: black: ' + str(black)

@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2a():
    print 'test2a psql: ' + str(psql)
    try:
        print 'test2a black: ' + str(black)
    except:
        print 'black doesnt exist'

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test3a():
    print 'test3a psql: ' + str(psql)
    print 'test3a black: ' + str(black)

print "before 1a"
test1a()
print "before 2a"
test2a()
print "before 3a"
test3a()
