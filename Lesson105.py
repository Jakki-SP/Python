
import copy as cp
l1 = [[10,20,30],[40,50,60]]
l2 = cp.deepcopy(l1)
l2[0][1] = 90
print(l1)
print(l2)