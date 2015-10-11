from postgresql import postgres
import testdb

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
def test1b():
    print 'test1b black: ' + str(black)

@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2b():
    print 'test2b psql: ' + str(psql)
    try:
        print 'test2b black: ' + str(black)
    except:
        print 'black doesnt exist'

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test3b():
    print 'test3b psql: ' + str(psql)
    print 'test3b black: ' + str(black)

print "\nbefore 1b"
test1b()
print "before 2b"
test2b()
print "before 3b"
test3b()
