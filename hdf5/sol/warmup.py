import numpy as np
import tables as tb

f = tb.openFile('temp.h5', 'a')
heart = np.ones(42, dtype=[('rate', int), ('beat', float)])
f.createTable('/', 'heart', heart)
f.close()

