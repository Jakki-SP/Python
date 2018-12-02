
no = int(input("Enter a no : "))
rev = 0
while(no>0):
    r = no%10
    no = no//10
    rev = (rev*10)+r
print(rev)