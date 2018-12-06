
# WAP to validate username and password
uname = input("Enter Username :")
upass = input("Enter Password :")
if uname == "sathya":
    if upass == "tech":
        print("Valid User")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
