
def sample(max=0):
    no = 0
    while True:
        if max > no:
            no+=1
            yield no
        else:
            break

for x in sample(int(input("Last No : "))):
    print(x)
