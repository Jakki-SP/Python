class MyIterator:
    def __init__(self,max=0):
        self.max = max
    def __iter__(self):
        self.no = 0
        return self
    def __next__(self):
        if self.max > self.no:
            self.no+=1
            return self.no
        else:
            raise StopIteration


# m1 = MyIterator()
# y = iter(m1)
# print(next(y))


# m2 = MyIterator(3)
# y = iter(m2)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

for x in MyIterator(5):
    try:
        print(x)
    except StopIteration:
        break



