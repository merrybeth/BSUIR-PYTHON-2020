import unittest
from package.vector import Vector


class TestVector(unittest.TestCase):

    def test_len(self):
        v = Vector(1, 1, 1, 2, 3)
        self.assertEqual(v.__len__(), 5)

    def test_add(self):
        v = Vector(1, 1, 1)
        v1 = Vector(1, 1, 1)
        v3 = Vector(2, 2, 2)
        self.assertEqual(v.__add__(v1), tuple(v3))

    def test_mul_const(self):
        v = Vector(1, 1, 1)
        const = 5
        v1 = Vector(5, 5, 5)
        self.assertEqual(v.__mul__(const), tuple(v1))

    def test_mul_vector(self):
        v = Vector(1, 1, 1)
        v1 = Vector(2, 3, 4)
        mul = 9
        self.assertEqual(v.__mul__(v1), 9)

    def test_sub(self):
        v = Vector(4, 5, 17, 9)
        v1 = Vector(2, 6, 13, -10)
        v3 = Vector(2, -1, 4, 19)
        self.assertEqual(v.__sub__(v1), tuple(v3))

    def test_getitem(self):
        v = Vector(1, 10, 13, 15, 2)
        key = 3
        self.assertEqual(v.__getitem__(key), 15)

    def test_eq_true(self):
        v = Vector(4, 5, 17, 9)
        v1 = Vector(4, 5, 17, 9)
        self.assertEqual(v.__eq__(v1), True)

    def test_eq_false(self):
        v = Vector(4, 5, 17, 9)
        v1 = Vector(1, 5, 1, 2)
        self.assertEqual(v.__eq__(v1), False)


if __name__ == '__main__':
    unittest.main()
