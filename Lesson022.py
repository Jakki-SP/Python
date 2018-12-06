#WAP to display 1 to 10
no = 1
while no<=10:
    print(no,end=" ")
    no+=1 # no = no+1
print("Thanks")

# WAP to read a no and print sum of
# the given No
# EX: 5475 = 5+4+7+5 = 21

no = int(input("Enter a No : "))
sum = 0
while no > 0:
    r = no % 10
    no //= 10
    sum += r
print("The sum = ",sum)
print("Thanks")



