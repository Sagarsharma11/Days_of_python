import numpy as np
from scipy import stats
import statistics

li = [1,2,3,4]
print(f'mean {np.mean(li)}')
print(f'median {np.median(li)}')
print(f'mode {statistics.mode(li)}')
print(f'sum {np.sum(li)}')
print(f'standard daviation {stats.tstd(li)}')
print(f'Variance {statistics.variance(li)}')