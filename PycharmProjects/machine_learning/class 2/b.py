import numpy as np
import decimal
start = decimal.Decimal('1')
stop = decimal.Decimal('10')
step = decimal.Decimal('0.2')
for x in np.arange(start=start,stop = stop , step = step):
    print(x,type(x))

