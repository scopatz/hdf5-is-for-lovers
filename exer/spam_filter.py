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



# 2. Repeat step 1 but with zlib compression at level 1.




# 3. Repeat step 1 but with blosc compression at level 5.

    

# 4. You realize that spam is often vacuous.  What if the unwanted elements
#    weren't already tagged.  Repeat step 1, leaving the data uncompressed
#    but without filling in spam everywhere.


# 5. Repeat step 4 but with blosc compression at level 5.



# 6. How long does it take to read this data in?

