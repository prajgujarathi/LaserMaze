import unittest
from maze import maze_laser

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.m1= maze_laser(5, 6, 1, 1, [['3', '4', '/'], ['3', '0', '/'], ['1', '2', '\\'], ['3', '2', '\\']])

    def test_checkloop(self):
        self.assertFalse(self.m1.check_loop(1, 2, 'S'))
        self.assertTrue(self.m1.check_loop(1, 2, 'S'))
        self.assertFalse(self.m1.check_loop(1, 3, 'S'))

    def test_laser(self):
        tile, x, y =self.m1.laser(1, 1, 'S')
        self.assertEquals(tile, 9)
        self.assertEquals(x, 0)
        self.assertEquals(y, 0)

if __name__ == '__main__':
    unittest.main()
