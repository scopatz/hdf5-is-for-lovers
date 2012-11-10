===================
HDF5 is for Lovers
===================

----
Bio
----
Anthony Scopatz is a computational nuclear engineer / physicist post-doctoral 
scholar at the FLASH Center at the University of Chicago.  His initial workshop 
teaching experience came from instructing bootcamps for The Hacker Within - a 
peer-led teaching organization at the University of Wisconsin.  Out of this grew 
a collaboration teaching Software Carpentry bootcamps in partnership with Greg 
Wilson.  During his tenure at Enthought, Inc, Anthony taught many week long 
courses (approx. 1 per month) on scientific computing in Python.

-----
Track
-----
This tutorial was conceived as an advanced track tutorial.  However, it could be recast 
as an introductory one, if the program committee desires.

------------
Description
------------
HDF5 is a hierarchical, binary database format that has become a *de facto* standard for 
scientific computing.  While the specification may be used in a relatively simple way 
(persistence of static arrays) it also supports several high-level features that prove 
invaluable.  These include chunking, ragged data, extensible data, parallel I/O, 
compression, complex selection, and in-core calculations.  Moreover, HDF5 bindings
exist for almost every language - including two Python libraries (PyTables and h5py).

This tutorial will discuss tools, strategies, and hacks for really squeezing every ounce
of performance out of HDF5 in new or existing projects.  It will also go over fundamental 
limitations in the specification and provide creative and subtle strategies for getting around 
them.  Overall, this tutorial will show how HDF5 plays nicely with all parts of an application 
making the code and data both faster and smaller.  With such powerful features at the 
developer's disposal, what is not to love?!

This tutorial is targeted at a more advanced audience which has a prior knowledge
of Python and NumPy.  Knowledge of C or C++ and basic HDF5 is recommended but not required.

--------------
Outline
--------------
* Meaning in layout (20 min)

    - Tips for choosing your hierarchy

* Advanced datatypes (20 min)

    - Tables
    - Nested types
    - Tricks with malloc() and byte-counting

* **Exercise on above topics** (20 min)

* Chunking (20 min)

    - How it works
    - How to properly select your chunksize

* Queries and Selections (20 min)

    - In-core vs Out-of-core calculations
    - PyTables.where()
    - Datasets vs Dataspaces

* **Exercise on above topics** (20 min)

* The Starving CPU Problem (1 hr)

    - Why you should always use compression
    - Compression algorithms available
    - Choosing the correct one
    - Exercise

* Integration with other databases (1 hr)

    - Migrating to/from SQL
    - HDF5 in other databases (JSON example)
    - Other Databases in HDF5 (JSON example)
    - Exercise

-------------------
Packages Required
-------------------
This tutorial will require Python 2.7, IPython 0.12+, NumPy 1.5+, and PyTables 2.3+. 
`ViTables`_ and MatPlotLib are also recommended.  These may all be found in Linux package
managers.  They are also available through EPD or easy_install.  ViTables may need to 
be installed independently.

.. _ViTables: http://vitables.org/
