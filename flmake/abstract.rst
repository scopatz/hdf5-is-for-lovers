======================================================
Total Recall: flmake and the Quest for Reproducibility
======================================================

:Author: Anthony Scopatz <scopatz@gmail.com>
:Affiliation: The University of Chicago

`FLASH`_ is a high-performance computing (HPC) multi-physics code which is used to perform 
astrophysical and high-energy density physics simulations.  It runs on the full range of 
systems from laptops to workstations to 100,000 processor super computers - such as the 
Blue Gene/P at Argonne National Laboratory.

Historically, FLASH was born from a collection of unconnected legacy codes written 
primarily in Fortran and merged into a single project.  Over the past 13 years major 
sections have been rewritten in other languages.  For instance, I/O is now implemented 
in C.  However building, testing, and documentation are all performed in Python.

FLASH has a unique architecture which compiles *simulation specific* executables for each 
new type of run.  This is aided by an object-oriented-esque inheritance model that is 
implemented by inspecting the file system's directory hierarchy.  This allows FLASH to 
compile to faster machine code than a compile-once strategy.  However it also 
places a greater importance on the Python build system.

To run a FLASH simulation, the user must go through three basic steps: setup, build, and 
execution.  Canonically, each of these tasks are independently handled by the user.  
However, with the recent advent of `flmake`_ - a Python workflow management utility for 
FLASH - such tasks may now be performed in a repeatable way.

Previous workflow management tools have been written for FLASH.  (For example, the 
"Milad system" was implemented entirely in Makefiles.)  However, none of the prior
attempts have placed reproducibility as their primary concern.  This is in part because
fully capturing the setup metadata requires alterations to the build system.

The development of flmake started by rewriting the existing build system
to allow FLASH to be run outside of the main line subversion repository.  It separates out
project and simulation directories independent of the FLASH source directory.  These
directories are typically under their own version control.

Moreover for each of the important tasks (setup, build, run, etc), a sidecar metadata 
*description* file is either written or appended to.  This is a simple 
dictionary-of-dictionaries JSON file which stores the environment of the 
system and the state of the code when each flmake command is run.  This metadata includes 
the version information of both the FLASH main line and project repositories.  
However, it also may include *all* local modifications since the last commit.  
A patch is automatically generated using the Python standard library ``difflib`` 
module and stored directly in the description.  

Along with universally unique identifiers, logging, and Python run control files, the 
flmake utility may use the description files to fully reproduce a simulation by 
re-executing each command in its original environment and state.  While ``flmake reproduce`` 
makes a useful debugging tool, it fundamentally increases the scientific merit of 
FLASH simulations.  

The methods described above may be used whenever 
source code itself is distributed.   While this is true for FLASH (uncommon amongst compiled
codes), most Python packages also distribute their source.  Therefore the same 
reproducibility strategy is applicable and highly recommended for Python simulation codes.  
Thus flmake shows that reproducibility - which is notably absent from most computational science 
projects - is easily attainable using only version control and standard library modules.

.. _FLASH: http://flash.uchicago.edu/site/

.. _flmake: http://flash.uchicago.edu/site/flashcode/user_support/tools4b/usersguide/flmake/index.html

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
