import unittest


class TestSort(unittest.TestCase):
    def test_sort(self):
        i = 0
        j = 0
        file = r'D:\Univercity\2 cours\4 sem\Python\Laba 2\tasks\sorted_numbers.txt'
        with open(file) as files:
            for line in files:
                next = int(line)
                if i > 0:
                    self.assertTrue(next >= j)
                i += 1
                j = next


if __name__ == '__main__':
    unittest.main()
