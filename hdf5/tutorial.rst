===================
HDF5 is for Lovers
===================

----
Bio
----
Anthony Scopatz is a computational nuclear engineer / physicist post-doctoral 
scholar at the FLASH Center at the University of Chicago.  His initial workshop 
teaching experiance came from instructing bootcamps for The Hacker Within - a 
peer-led teaching organization at the Univerity of Wisconsin.  Out of this grew 
a collaboration teaching Software Carpentry bootcamps in partnership with Greg 
Wilson.  During his tenure at Enthought, Inc, Anthony taught many week long 
courses (approx. 1 per month) on scientific computing in Python.

-----
Track
-----
This tutorial was concived as an advanced track tutorial.  However, it could be recast 
as an introductory one, if the program comittee desires.

------------
Description
------------
HDF5 is a hierarchical, binary database format that has become a *de facto* standard for 
scientific computing.  While the specification may be used in a relatively simple way 
(persistence of static arrays) it also supports several high-level features that prove 
invaluable.  These include chunking, ragged data, extensible data, parallel I/O, 
compresssion, complex selection, and in-core calculations.  Moreover, HDF5 bindings
exist for almost every language - including two Python libraries (PyTables and h5py).

This tutorial will discuss tools, strategies, and hacks for really squeezing every ounce
of performance out of HDF5 in new or existing projects.  It will also go over fundemental 
limitations in the specification and provide creative and subtle strategies for getting around 
them.  Overall, this tutorial will show how HDF5 plays nicely with all parts of an application 
making the code and data both faster and smaller.

This tutorial is targeted at a more advanced audience which has a prior knowledge
of Python and NumPy.  Knowledge of C or C++ and basic HDF5 is recomended but not required.



A more detailed outline of the tutorial content, including the duration of each part, 
and exercise sessions for the review process.
A list of Python packages that attendees will need to have installed prior to the class to follow along. Please mention if any packages are not cross platform. Installation instructions or links to installation documentation should be provided for packages that are not available through easy_install, pip, EPD, etc., or that require third party libraries.

If available, the tutorial notes, slides, exercise files, ipython notebooks, that you already have, even if they are preliminary.
Important dates:
Monday, April 30: Tutorial proposals due
Monday, May 7: Accepted tutorials announced
Monday, June 18: Early registration ends
Monday-Tuesday, July 16 - 17: SciPy 2012 Tutorials, Austin TX
Wednesday-Thursday, July 18 - 19: SciPy 2012 Conference, Austin TX
Friday-Saturday, July 20 - 21: SciPy 2012 Sprints, Austin TX & remote
