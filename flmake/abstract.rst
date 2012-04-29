======================================================
Total Recall: flmake and the Quest for Reproducibility
======================================================

:Author: Anthony Scopatz <scopatz@gmail.com>
:Affiliation: The University of Chicago

FLASH is high-performance computing (HPC) multi-physics code which is used to perform 
astrophysical and high-energy density physics simulations.  It runs on the full range of 
systems from laptops to workstations to 100,000 processors - such as the Blue Gene/P at 
Argonne National Laboratory.

Historically, FLASH was born from a collection of unconnected legacy codes written 
primarily in Fortran.  Over the past 13 years major sections have been rewritten in other 
languages.  For instance, I/O is now implemented in C.  However building, testing, and 
documentation are all performed in Python.

FLASH has a unique architechure which compiles *simulation specific* executables for each 
new type of run.  This is aided by an object-oriented-esque inheritence model that is 
implemented by inspecting the file system's directory hierarchy.  This allows FLASH to 
compile to faster machine code than a more standard compile once strategy.  However it also 
places a much greater importance on the Python build system.

To run a FLASH simulation, the user must go through three basic steps: setup, build, and 
execution.  Canonically, each of these tasks are independently handled by the user.  
However, with the recent advent of ``flmake``

Here, include a talk summary of no longer than 500 words. Aspects such as relevance to 
Python in science, applicability, and novelty will be considered by the program committee.

...............................................................

Please indicate with an X your preference::

  [X] Only consider this presentation for a talk.

  [ ] Only consider this presentation for a poster.

  [ ] Consider this presentation for either a talk or a poster.

...............................................................

Please indicate with an X whether you are willing to prepare an accompanying paper::

  [X] Yes [ ] No

...............................................................

Optional: Indicate your preference for a specialized main track::

  [ ] High Performance Computing with Python
  [ ] Visualization

Or for one of the smaller domain-specific sessions::

  [ ] Computational bioinformatics
  [ ] Meteorology and climatology
  [ ] Astronomy and astrophysics
  [ ] Geophysics

Please note that this selection is simply a guideline for the program committee, and that 
talks may be scheduled in a different session than indicated.

...............................................................

Please email this form to 2012submissions@scipy.org
