
# coding: utf-8

# **Your brother is going on an expidition to build a bridge between the two
# peaks of Mount Kilimanjaro.  He needs you to create a database of information 
# about the team.  This needs to include:**
# 
# I. A table of critical team member information.
# 
# II. An array of oxygen depravation fraction (to be filled in later)
#     for everyone team member for each of the million steps up the mountain.
# 
# The info he has about the team is their first name, last name, age, and 
# whether they are alive or not.
# 
# Suddenly, he has forgotten every other team member's name!  
# 
# III. Please read these off for him, but only if they are alive
# 
# Careful out there!

# In[1]:

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

f = tb.open_file('expidition.h5', 'w')


# In[2]:

# 1.
teamdt = np.dtype([('first', 'S10'), ('last', 'S10'), 
                   ('age', int), ('alive', bool)])
team = np.array(team, dtype=teamdt)
f.create_table('/', 'team', team)


# In[3]:

# 2.
shape = (len(team), 1000000)
o2dep = np.zeros(shape, float) 
f.create_array('/', 'o2dep', o2dep, "help I can't breathe!")
f.flush()


# In[4]:

# 3.
for first, last, age, alive in f.root.team[::2]:
    if alive:
        print(first, last)

f.close()

