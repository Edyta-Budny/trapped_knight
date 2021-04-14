def add_tuples(tupleA, tupleB):
    return tupleA[0] + tupleB[0], tupleA[1] + tupleB[1]


class Matrix:
    ELEMENT = ['.']

    def __init__(self, size):
        self.size = size
        self.centre = int(size / 2) - 1 if size % 2 == 0 else int(size / 2)
        self.array = size ** 2 * self.ELEMENT

    def print(self):
        print('    ', end='')

        for num in range(-self.centre, self.centre + 1):
            print('{:>4}'.format(num), end='')
        print()

        for y in range(self.centre, -self.centre - 1, -1):
            print('{:>4}'.format(y), end='')
            for x in range(-self.centre, self.centre + 1):
                print('{:>4}'.format(self.get((x, y))), end='')
            print()

    def __index(self, spot: tuple):
        return (spot[1] + self.centre) * self.size + spot[0] + self.centre

    def set(self, spot, v):
        self.array[self.__index(spot)] = v

    def get(self, spot):
        return self.array[self.__index(spot)]

    def fill(self):
        y = 1
        x = 0
        counter = 1
        direction = 0
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        location = (0, 0)

        while counter < self.size ** 2:
            for _ in range(y):
                self.set(location, counter)
                location = add_tuples(location, DIRECTIONS[direction % 4])
                counter += 1
            direction += 1
            if x % 2:
                y += 1
            x += 1
