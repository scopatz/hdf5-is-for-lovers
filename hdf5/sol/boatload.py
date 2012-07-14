"""Create a metric boatload of random people.  That's right, create a table of 
1000 random people on boats.  

1. Define the description.  This should include:

    * First names
    * Last names
    * Lattitude and longitude, together
    * List of ships which they have sailed on, min 1 but at most 5
    * Lost at sea status

2. Use the rand_sailor function to write a table of all of these people.

3. Resuce patrols are dispatched by quarter.  Using the lattitude and 
   longitude, create groups representing the NE, NW, SE, and SW and place
   smaller tables of just these sailors.

4. Rescue patrols also need up to date information on whether a not 
   a person is lost.  Create two tables (lost & found) in each of the 
   four directions which approriately elliminate the lost-at-sea status.
"""
import random
import numpy as np
import tables as tb

with open('names.txt', 'r') as f:
    names = f.read().split()
    first_names = names[::2]
    last_names = names[1::2]

with open('ships.txt', 'r') as f:
    ship_names = [s.strip() for s in f.readlines()]

def rand_sailor():
    first = random.choice(first_names)
    last = random.choice(last_names)
    lat_long = np.random.random((2,)) * (180.0, 360.0) - (90.0, 180.0)
    num_ships = np.random.random_integers(1,5)
    ships = list(np.random.choice(ship_names, num_ships, replace=False))
    lost = bool(np.random.random_integers(0,1))
    return first, last, lat_long, ships, lost

f = tb.openFile('boatload.h5', 'a')

# 1. Define the description.  This should include:
#
#    * First names
#    * Last names
#    * Lattitude and longitude, together
#    * List of ships which they have sailed on, min 1 but at most 5
#    * Lost at sea status

max_first_len = max([len(x) for x in first_names])
max_last_len = max([len(x) for x in last_names])
max_ship_len = max([len(x) for x in ship_names])

desc = np.dtype([('first', 'S' + str(max_first_len)), 
                 ('last', 'S' + str(max_last_len)), 
                 ('location', [
                    ('lat', float),
                    ('long', float),
                    ]),
                 ('ships', 'S' + str(max_ship_len), (5,)),
                 ('lost', bool),
                ])


# 2. Use the rand_sailor function to write a table of all of these people.
raw_sailors = []
for i in range(1000):
    first, last, lat_long, ships, lost = rand_sailor()
    ships.extend([''] * (5 - len(ships)))
    raw_sailors.append((first, last, lat_long, ships, lost))
sailors = np.array(raw_sailors, dtype=desc)

f.createTable('/', 'sailors', sailors)


# 3. Resuce patrols are dispatched by quarter.  Using the lattitude and 
#    longitude, create groups representing the NE, NW, SE, and SW and place
#    smaller tables of just these sailors.
quads = {'NE': [(0.0, 90.0), (0.0, 180.0)],
         'NW': [(0.0, 90.0), (-180.0, 0.0)],
         'SE': [(-90.0, 0.0), (0.0, 180.0)],
         'SW': [(-90.0, 0.0), (-180.0, 0.0)],
        }

for quad in quads:
    f.createGroup('/', quad)
    lower_lat_mask = quads[quad][0][0] < sailors['location']['lat']
    upper_lat_mask = quads[quad][0][1] > sailors['location']['lat']
    lower_long_mask = quads[quad][1][0] < sailors['location']['long']
    upper_long_mask = quads[quad][1][1] > sailors['location']['long']
    mask = lower_lat_mask & upper_lat_mask & lower_long_mask & upper_long_mask
    f.createTable('/' + quad, 'sailors', sailors[mask])

# 4. Rescue patrols also need up to date information on whether a not 
#    a person is lost.  Create two tables (lost & found) in each of the 
#    four directions which approriately elliminate the lost-at-sea status.

    lost_mask = mask & sailors['lost']
    lost_sailors = sailors[lost_mask][['first', 'last', 'location', 'ships']]
    f.createTable('/' + quad, 'lost', lost_sailors)

    found_mask = mask & ~sailors['lost']
    found_sailors = sailors[found_mask][['first', 'last', 'location', 'ships']]
    f.createTable('/' + quad, 'found', found_sailors)

# Remember to always close the file!
f.close()
