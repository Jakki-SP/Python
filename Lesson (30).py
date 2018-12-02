
#WAP to read a String from user and print no of words in String
# and print no of char's in String

s1 = input("Enter a String : ")
res = s1.split()
print(res)
print("The Total Words = ",len(res))
print("The Total char's = ",len(s1))