
import copy as cp
l1 = [10,20,30,40,50]
l2 = cp.copy(l1)
l2[2] = 90
print(l1)
print(l2)
