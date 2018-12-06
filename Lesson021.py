
# nested Loops
# WAP to display
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3

for x in range(5):
    for y in range(1, 4):
        print(y, end=" ")
    print()
print("Thanks")
print("--------------------------")

# WAP to display
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

for x in range(3):
    for y in range(5, 0, -1):
        print(y, end=" ")
    print()
print("Thanks")

print("--------------------------")

# WAP to display
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

for x in range(1,4):
    for y in range(1, 5):
        print(x, end=" ")
    print()
print("Thanks")
print("-------------------")

# WAP to display
# 1
# 1 2
# 1 2 3

for x in range(1,4):
    for y in range(1,x+1):
        print(y,end=" ")
    print()
print("Thanks")
print("-----------------------")

# Error Program range will accept
# only Integer
#for x in range("Sathya"):
#   print(x)


for x in "sathya":
    print(x,end=" ")
