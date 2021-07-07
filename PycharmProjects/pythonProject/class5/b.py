import time
start = time.time()
l = range(100_0000)
l = [x*2 for x in l]
print('list:',time.time()-start)

import numpy as np
start = time.time()
l = np.arange(100_0000)
l = l*2
print('np:', time.time()-start)
