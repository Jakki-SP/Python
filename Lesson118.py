def outer():
    print("I am Outer Function")
    def inner():
        print("I am Inner Function")
    return  inner # returning function object


inn = outer()
print(inn)
print(type(inn))
del outer
inn()
outer()

