# JOINING ARRAYS (CONCATENATE( ),STACK( ),VSTACK( ),HSTACK( ),DSTACK( ))
import numpy as np
arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)
# print(np.concatenate((arr1,arr2),axis=1))

# print(np.stack((arr1,arr2)))
# print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
print(np.dstack((arr1,arr2)))