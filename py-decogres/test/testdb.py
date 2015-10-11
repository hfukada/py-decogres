import unittest
import testdb as moretests

from postgresql import postgres

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
def test1a():
    return black

@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2a():
    return psql

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
@postgres(**{'name': 'psql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test3a():
    return [psql, black]

class DecoratorTests(unittest.TestCase):
    def test_database_continuity():
        self.assertTrue(test1a() == moretests.test2a())
        self.assertTrue(test1b() == moretests.test2b())
        self.assertTrue(test1c() == moretests.test3c())

    def test_database_connectivity():
        self.assertTrue(test4b() == 42)
