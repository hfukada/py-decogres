import unittest
from decogres.decorator import postgres

from testdb2 import *

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
def test1a():
    return black

@postgres(**{'name': 'black', 'connection_url': "postgresql://postgres:postgres@localhost/black"})
@postgres(**{'name': 'postgresql', 'connection_url': "postgresql://postgres:postgres@localhost/"})
def test2a():
    print 'postgresql ' + str(postgresql) + ' black ' + str(black)
    return [postgresql, black]

class DecoratorTests(unittest.TestCase):

    def test_database_connectivity(self):
        self.assertTrue(test4b() == 42)

    def test_single_database_continuity(self):
        """ Tests that databases recalled from two spots in code recall the same db instance"""
        self.assertTrue(test1a() == test1b())

    def test_multi_database_continuity(self):
        """ Tests that multiple databases recalled from two spots in code recall the same db instance"""
        self.assertTrue(test2a() == test2b())

if __name__ == '__main__':
    unittest.main()
