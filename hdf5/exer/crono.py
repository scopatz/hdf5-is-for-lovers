"""Your friend Crono has been murdered by the mighty demon Lavos!
Luckily, you have a time machine, the good ship Epoch.  You and 
your friends hatch a scheme to save him by replacing him with a 
doll that looks just like him.  

Unfortunately Crono had the time machine too and you are not exactly 
sure when he died.  Thankfully the Epoch's logs keep a record of 
who visited which time periods.

To save Crono, and foil the plans of Lavos, you must:

    1. Seach through the ship's log and print all of the
       times Crono was alive.

    2. Figure out if you ever left Crono alone, and if so, when?
       Write these time out to a separate table with fully reading
       the log into memory.

    3. Send three friends into the fray to help Crono out in 
       his time of need.

    4. Who are Crono's best friends?  Who are his worst?  Judge 
       based on the amount of time they spend with him.

"""
import numpy as np
import tables as tb

import _epoch_log
_epoch_log.make_log()

friends = ['marle', 'lucca', 'frog', 'robo', 'ayla', 'magus']

f = tb.openFile('epoch_log.h5', 'a')

# 1. Seach through the ship's log and print all of the
#    times Crono was alive.



# 2. Figure out if you ever left Crono alone, and if so, when?
#    Write these time out to a separate table with fully reading
#    the log into memory.


# 3. Send three friends into the fray to help Crono out in 
#    his time of need.


# 4. Who are Crono's best friends?  Who are his worst?  Judge 
#    based on the amount of time they spend with him.

# remember to close the file
f.close()
