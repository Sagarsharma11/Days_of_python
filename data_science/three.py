#array computation

import numpy as np

arr1 = np.arange(1,5).reshape(2,2)
arr2 = np.arange(1,5).reshape(2,2)

print(f'sum {np.add(arr1,arr2)}')
print(f'sub {np.subtract(arr1,arr2)}')
print(f'mul {np.multiply(arr1,arr2)}')
print(f'div {np.divide(arr1,arr2)}')
print(f'pow {np.power(arr1,3)}')