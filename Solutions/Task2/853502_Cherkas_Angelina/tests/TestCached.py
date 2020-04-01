import unittest
from package import cached


class MyTestCase(unittest.TestCase):
    def test_count(self):
        self.assertEqual(cached.count(1), 2)
        self.assertEqual(cached.count(2), 3)

    def test_mul(self):
        self.assertEqual(cached.mul(2), 4)
        self.assertEqual(cached.mul(3), 9)


if __name__ == '__main__':
    unittest.main()
