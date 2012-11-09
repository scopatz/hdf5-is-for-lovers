"""Your brother is going on an expidition to build a bridge between the two
peaks of Mount Kilimanjaro.  He needs you to create a database of information 
about the team.  This needs to include:

    1. A table of critical team member information.

    2. An array of oxygen depravation fraction (to be filled in later)
       for everyone team member for each of the million steps up the mountain.

The info he has about the team is their first name, last name, age, and 
whether they are alive or not.

Suddenly, he has forgotten the first half of team's names.  

    3. Please read these off for him.

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
