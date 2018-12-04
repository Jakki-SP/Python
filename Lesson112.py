def sample():
    no = 0
    no+=1
    yield no

    no += 1
    yield no

    no += 1
    yield no

# x = sample()
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x)) # StopIteration


for x in sample():
    print(x)