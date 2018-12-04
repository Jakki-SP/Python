# using iter and next functions on
# pre-defined Iterator Object

x = [10,20,30,40,50]
print(type(x)) # <class 'list'>
y = iter(x)
print(type(y))

print(next(y)) # 10
print(next(y)) # 20
print(next(y)) # 30
print(next(y)) # 40
print(next(y)) # 50
print(next(y)) # StopIteration Exception
