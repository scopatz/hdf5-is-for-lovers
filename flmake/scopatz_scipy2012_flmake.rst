SciPy 2012
==============================

.. container:: main-title

    Total Recall: ``flmake`` and the Quest for Reproducibility

.. container:: main-names

    July 16th, 2012, SciPy, Austin, TX

    Anthony Scopatz 

    The FLASH Center

    The University of Chicago

    scopatz@gmail.com

Introduction
===============================
What is the one thing that we do shamefully poorly as computational scientists?

.. break

.. container:: big-and-center

    *Reproducibility!*

.. break

**Goals:**

.. break

    * Attain a totally reproducible workflow, 

.. break

    * Show that it is not hard (in Python), 

.. break

    * Inspire you!


What is FLASH?
==============================
FLASH code is a modular, parallel multiphysics simulation code for modeling
terrestrial and astrophysical plasmas.  Features include:

.. break

    * Grid: Uniform Grid, AMR

.. break

    * Equation of State: Ideal gas, Multimaterial

.. break

    * Laser ray trace package

.. break

    * Nuclear Burning


FLASH Architecture
===============================
FLASH compiles simulation-specific binaries from user defined 
code Units.

.. break

Code Units are mix of Fortran, C, C++, and Python and have  
an OO-esque inheritance model via posix directories.

.. break

To execute a FLASH simulation you must:

.. container:: small

    * setup (pure python), 

.. break

    * build (make),

.. break

    * and run (flash binary).

Questions
===============================
.. raw:: pdf 

    Spacer 0 30

.. image:: img/qm.jpg
    :scale: 55%

