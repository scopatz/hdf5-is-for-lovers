"""Email today is just the worst.  It seems that 3/4 of time, the message is just 
total junk while only 25% of emails are actually worthwhile.

Somehow It is now your job to eliminate all of that spam for everyone at work, 
leaving behind only the eggy goodness. You suspect compression might be able to
aid you in your quest.

1. Create an HDF5 file which contains a single emails array, uncompressed.  
   Close this file and use the getsize() function to report the size on disk.
   Time how long this took and print that out as well.

2. Repeat step 1 but with zlib compression at level 1.

3. Repeat step 1 but with blosc compression at level 5.

4. You realize that spam is often vacuous.  What if the unwanted elements
   weren't already tagged.  Repeat step 1, leaving the data uncompressed
   but without filling in spam everywhere.

5. Repeat step 4 but with blosc compression at level 5.

6. How long does it take to read these arrays in?

"""
from time import time
from os.path import getsize

import numpy as np
import tables as tb

def email_array(num=10000000, rate=0.75, fill=True):
    if fill:
        emails = np.empty(10000000, 'S4')
        emails.fill('spam')
    else:
        emails = np.array([np.random.bytes(4) for x in range(num)], dtype='S4')
    eggind = np.random.randint(0, num, int(num * (1.0 - rate)))
    emails[eggind] = 'eggs'
    return emails


# 1. Create an HDF5 file which contains a single emails array, uncompressed.  
#    Close this file and use the getsize() function to report the size on disk.
#    Time how long this took and print that out as well.

NUM = 10000000
RATE = 0.75
emails = email_array(NUM, RATE)

t = time()
with tb.openFile('uncompressed.h5', 'w') as f:
    earray = f.createEArray('/', 'emails', tb.StringAtom(4), (0,), expectedrows=NUM)
    earray.append(emails)
tdelta = time() - t

msg = "The uncompressed array is {0} bytes and took {1} ms to write."
print msg.format(getsize('uncompressed.h5'), tdelta * 1000)



# 2. Repeat step 1 but with zlib compression at level 1.

filters = tb.Filters(complib='zlib', complevel=1)

t = time()
with tb.openFile('zlib1.h5', 'w') as f:
    earray = f.createEArray('/', 'emails', tb.StringAtom(4), (0,), 
                            filters=filters, expectedrows=NUM)
    earray.append(emails)
tdelta = time() - t

msg = "The zlib1 array is {0} bytes and took {1} ms to write."
print msg.format(getsize('zlib1.h5'), tdelta * 1000)
    



# 3. Repeat step 1 but with blosc compression at level 5.

filters = tb.Filters(complib='blosc', complevel=5)

t = time()
with tb.openFile('blosc5.h5', 'w') as f:
    earray = f.createEArray('/', 'emails', tb.StringAtom(4), (0,), 
                            filters=filters, expectedrows=NUM)
    earray.append(emails)
tdelta = time() - t

msg = "The blosc5 array is {0} bytes and took {1} ms to write."
print msg.format(getsize('blosc5.h5'), tdelta * 1000)
    

# 4. You realize that spam is often vacuous.  What if the unwanted elements
#    weren't already tagged.  Repeat step 1, leaving the data uncompressed
#    but without filling in spam everywhere.

emails = email_array(NUM, RATE, False)

t = time()
with tb.openFile('unfilled.h5', 'w') as f:
    earray = f.createEArray('/', 'emails', tb.StringAtom(4), (0,), expectedrows=NUM)
    earray.append(emails)
tdelta = time() - t

msg = "The unfilled array is {0} bytes and took {1} ms to write."
print msg.format(getsize('unfilled.h5'), tdelta * 1000)



# 5. Repeat step 4 but with blosc compression at level 5.

filters = tb.Filters(complib='blosc', complevel=5)

t = time()
with tb.openFile('blosc5_unfilled.h5', 'w') as f:
    earray = f.createEArray('/', 'emails', tb.StringAtom(4), (0,), 
                            filters=filters, expectedrows=NUM)
    earray.append(emails)
tdelta = time() - t

msg = "The blosc5_unfilled array is {0} bytes and took {1} ms to write."
print msg.format(getsize('blosc5_unfilled.h5'), tdelta * 1000)



# 6. How long does it take to read this data in?

print

files = ['uncompressed.h5', 'zlib1.h5', 'blosc5.h5', 'unfilled.h5', 'blosc5_unfilled.h5']
for file in files:
    t = time()
    with tb.openFile(file, 'r') as f:
        emails = f.root.emails[:]
    tdelta = time() - t

    msg = "The {0} file took {1} ms to read."
    print msg.format(file, tdelta * 1000)
