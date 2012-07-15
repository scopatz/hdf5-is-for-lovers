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

crono_alive = f.root.log.readWhere('crono', field='timestamp')
print "Crono was alive at:\n", crono_alive, '\n'

# 2. Figure out if you ever left Crono alone, and if so, when?
#    Write these time out to a separate table with fully reading
#    the log into memory.
crono_alone = f.createTable('/', 'crono_alone', f.root.log.description)
alone_cond = "crono & ~" + " & ~".join(friends)
f.root.log.whereAppend(crono_alone, alone_cond)

if 0 < len(crono_alone):
    print "Oh no! Crono was left alone...\n"
else:
    print "Great! Crono always had backup!"

# 3. Send three friends into the fray to help Crono out in 
#    his time of need.
for row in f.root.log.where(alone_cond):
    row['lucca'] = True
    row['frog'] = True
    row['magus'] = True
    row.update()
f.root.log.flush()

# 4. Who are Crono's best friends?  Who are his worst?  Judge 
#    based on the amount of time they spend with him.
time_together = {}
for friend in friends:
    inds = f.root.log.getWhereList("crono & " + friend)
    time_together[friend] = len(inds)

besties = sorted(time_together.items(), reverse=True, key=lambda x: x[1])
print "Best friend: ", besties[0][0]
print "Worst friend: ", besties[-1][0]

f.close()
