# WAP to read 2 no's and find Big No
no1 = int(input("1st No"))
no2 = int(input("2nd No"))
if no1>no2:
    print(no1," is Big")
else:
    if no2>no1:
        print(no2," is Big")
    else:
        print("Both are same")
print("Thanks")
