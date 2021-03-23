# file1 = open('input.txt')
# nums = file1.read().split()
# a, b = map(int, nums)
# result = a + b
# file2 = open('output.txt', 'w')
# file2.write(str(result))


class Robot():
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.command = None

    def move(self, command):
        if self.coordinates[0] > 100 or self.coordinates[1] > 100:
            return exit()
        a = list(self.coordinates)
        for i in command:
            if i == 'N':
                a[1] += 1
            elif i == 'S':
                a[1] -= 1
            elif i == 'W':
                a[0] -= 1
            elif i == 'E':
                a[0] += 1
        self.command = command
        return tuple(a)

    def path(self):
        if self.coordinates[0] > 100 or self.coordinates[1] > 100:
            return exit()
        cords = list()
        a = list(self.coordinates)
        cords.append(tuple(a))
        for i in self.command:
            if i == 'N':
                a[1] += 1
                cords.append(tuple(a))
            elif i == 'S':
                a[1] -= 1
                cords.append(tuple(a))
            elif i == 'W':
                a[0] -= 1
                cords.append(tuple(a))
            elif i == 'E':
                a[0] += 1
                cords.append(tuple(a))
        return cords


b = Robot((0, 0))
print(b.move('NENW'))
print(b.path())