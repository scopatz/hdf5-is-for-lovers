
# coding: utf-8

# In[ ]:

import numpy as np
import tables as tb

f = tb.open_file('temp.h5', 'w')
heart = np.ones(42, dtype=[('rate', int), ('beat', float)])
f.create_table('/', 'heart', heart)
f.close()

