# Fancy Indexing 
import numpy as np
rand = np.random.RandomState(43)
x = rand.randint(100,size=5)
ind = rand.randint(5,size=4)
print(x)
index = [0,2,3]
print(x[ind])
# array([51, 92, 14, 71, 60, 20, 82, 86, 74, 74])
# x[3], x[5]
# # (71, 20)
# ind=[3,4,5]
# x[ind]
# # array([71, 60, 20])
# row=np.array([0,1,2])
# col=np.array([3,4,5])
# x[row,col]
# array([2,5,11])