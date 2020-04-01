class Vector(object):
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def __mul__(self, other):
        if type(other) == type(self):
            return sum(a * b for a, b in zip(self, other))
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple(a * other for a in self)
            return product

    def __add__(self, other):
        res = tuple(a + b for a, b in zip(self, other))
        return res

    def __sub__(self, other):
        res = tuple(a - b for a, b in zip(self, other))
        return res

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __str__(self):
        return str(self.values)

    def __eq__(self, other):
        if self.__len__() == len(other) and all([a == b for a, b in zip(self, other)]):
            return True
        else:
            return False


v = Vector(1, 1, 1)
v2 = Vector(2, 2, 2)
print(v.__add__(v2))
