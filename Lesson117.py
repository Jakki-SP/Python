def outer():
    print("I am Outer Function")
    def inner():
        print("I am Inner Function")
    inner()
    print("Outer close")


outer() # Calling Outer Function


