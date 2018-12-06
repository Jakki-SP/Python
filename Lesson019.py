d1 = {"101":[10,20,30,40,50,60],
      "102":[11,22,33,44,55,66],
      "103":[99,88,77,66,55,44]}

for key,value in d1.items():
    print("Idno = ",key,end=" ")
    print("Toal = ",sum(value),end=" ")
    print("High Marks = ",max(value),end=" ")
    print("Low Marks = ",min(value))

