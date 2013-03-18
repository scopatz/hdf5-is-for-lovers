import numpy as np
import tables as tb

with tb.openFile('temp.h5', 'a') as f:
    heart = np.ones(42, dtype=[('rate', int), ('beat', float)])
    f.createTable('/', 'heart', heart)

