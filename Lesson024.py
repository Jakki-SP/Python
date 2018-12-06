# WAP to Validate PIN No
count = 1
while True:
    pin = int(input("Enter Pin No : "))
    if pin == 5475:
        print("Valid User")
        break
    else:
        count+=1
        print("Invalid User")
        if count > 3:
            print("Account is Blocked")
            break
        else:
            ans = int(input("To Continue Press 1 "))
            if ans == 1:
                continue
            else:
                break
print("Thanks")
