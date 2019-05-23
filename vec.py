class vec:
    """ A class representing 2d vector
    Implements basic vector arithmetic operations
    """

    def __init__(self, x, y=None):
        if y is None:
            self.x, self.y = x  # Init from tuple
        else:
            self.x, self.y = x, y  # Init from coordinates


    def __add__(self, other):
        return vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier):
        return vec(self.x * multiplier, self.y * multiplier)

    def __floordiv__(self, divisor):
        return vec(self.x // divisor, self.y // divisor)


    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__, self.x, self.y)

    def __iter__(self):
        # Useful for converting to tuple
        yield self.x 
        yield self.y


if __name__ == '__main__':
    # Examples:
    v = vec(2, 3)
    print(v)

    t = (2, 3)
    v = vec(t)
    print(v)

    print(v + vec(5, 8))
    print(vec(100, 100) - v)
    print(v * 2)
    print(v // 2)

    print(tuple(v))
