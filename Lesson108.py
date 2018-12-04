
x = [10,20,30,40,50]
y = iter(x)
while True:
    try:
        #print(next(y))
        print(y.__next__())
    except StopIteration:
        break
print("Thanks")
