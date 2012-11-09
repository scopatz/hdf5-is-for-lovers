"""Your brother is going on an expidition to build a bridge between the two
peaks of Mount Kilimanjaro.  He needs you to create a database of information 
about the team.  This needs to include:

    1. A table of critical team member information.

    2. An array of oxygen depravation fraction (to be filled in later)
       for everyone team member for each of the million steps up the mountain.

The info he has about the team is their first name, last name, age, and 
whether they are alive or not.

Suddenly, he has forgotten every other team member's name!  

    3. Please read these off for him, but only if they are alive

Careful out there!
"""

import numpy as np
import tables as tb

team = [('Flavia',   'Jacquin',   21, True),
        ('Michal',   'Ards',       7, True),
        ('Madaline', 'Herta',     25, True), 
        ('Ike',      'Jerding',    3, True),
        ('Winford',  'Bergenty',  59, True),
        ('Fernanda', 'Leuze',     51, True),
        ('Larae',    'Dalaq',     44, False),
        ('Ema',      'Czyrnik',   51, True),
        ('Britt',    'Housemate', 32, False),
        ('Eldridge', 'Lerow',     72, False),
        ]

f = tb.openFile('expidition.h5', 'w')

# 1.
teamdt = np.dtype([('first', 'S10'), ('last', 'S10'), 
                   ('age', int), ('alive', bool)])
team = np.array(team, dtype=teamdt)
f.createTable('/', 'team', team)

# 2.
shape = (len(team), 1000000)
o2dep = np.zeros(shape, float) 
f.createArray('/', 'o2dep', o2dep, "help I can't breathe!")
f.flush()


# 3.
for first, last, age, alive in f.root.team[::2]:
    if alive:
        print first + " " + last

f.close()
