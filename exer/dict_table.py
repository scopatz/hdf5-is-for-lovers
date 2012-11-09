"""Node lookup in HDF5, like chunk lookup, is done via B-tree searching. 
Finding an entry in a B-tree is an O(log(n)) operation.  Sometimes, we
want to be faster than that.  Say O(1) --- (*cough* dict). 

Say that you have a complicated file layout: 500 arrays split randomly 
over 100 groups.  You'd rather not have to ask each group if they have a 
specific dataset, so when you create the file you also create a map of
all datasets to the group that they are part of. 

Now wouldn't it be convenient to store this map right next to the data?!

1. Store your (id, group) map as a Table on the root node.  Close the file.

2. Reopen the file read-only, recreate your dictionary from the Table, 
   and grab any array back into memory

"""

import numpy as np
import tables as tb


# create sample data 
f = tb.openFile('dict_table.h5', 'w')
groups = [f.createGroup('/', 'grp' + str(i), "Group " + str(i)) for i in range(1, 101)]

idmap = {}
for i in range(1, 501):
    id = 'id' + str(i)
    grpi = np.random.randint(0, 100)
    grpid = '/grp' + str(grpi + 1)
    f.createArray(groups[grpi], id, i*np.ones(i), "ID-" + str(i))
    idmap[id] = grpid



# 1. Store your (id, group) map as a Table on the root node.  Close the file.



# 2. Reopen the file read-only, recreate your dictionary from the Table, 
#    and grab any array back into memory
