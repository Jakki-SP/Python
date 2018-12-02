def add():
    sub()
    print("I am Add")

def mul():
    sub()
    print("I am Mul")

def sub():
    print("I am Sub")

def div():
    add()
    print("I am Div")

print("Hi")
div()
print("Bye")