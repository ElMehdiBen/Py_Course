class Stats:
    def __init__(self, x):
        self.data = x

    def count(self):
        return len(self.data)

    def sum(self):
        data_sum = 0
        for e in self.data:
            data_sum += e
        return data_sum

    def mean(self):
        return self.sum() / self.count()

    def min_(self):
        return min(self.data)

    def last(self):
        return self.data[-1]


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

Obj = Stats(ages)

print(Obj.count())
print(Obj.sum())
print(Obj.mean())
print(Obj.last())