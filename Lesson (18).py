d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

# This loop will display Keys
for x in d1:
    print(x)
print("Thanks")
print("------------------")

# display values
for x in d1:
    print(d1[x])
print("Thanks")
print("------------------")

# Program to display key and value

for x in d1:
    print(x," -- ",d1[x])
print("Thanks")
print("------------------")

# Example's on Dict Functions

# Example 1
for x in d1.items():
    print(x,type(x))
print("Thanks")
print("------------------")

# Example 2
for key,value in d1.items():
    print(key,value)
print("Thanks")
print("------------------")








