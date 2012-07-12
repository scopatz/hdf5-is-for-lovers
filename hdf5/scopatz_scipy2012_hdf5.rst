SciPy 2012 - Tutorials
==============================

.. container:: main-title

    HDF5 is for Lovers |nerd_candy_heart|

.. container:: main-names

    July 16th, 2012, SciPy, Austin, TX

    Anthony Scopatz 

    The FLASH Center

    The University of Chicago

    scopatz@gmail.com


.. |nerd_candy_heart| image:: img/nerd_candy_heart.png 
                        :scale: 100%



What is HDF5?
==============================
HDF5 stands for (**H**)eirarchical (**D**)ata (**F**)ormat (**5**)ive.

.. break

It is supported by the lovely people at |hdf_group|

.. break

At its core HDF5 is binary file type specification.

.. break

However, what make HDF5 great is the numerous libraries written to interact 
with files of this type and their *extremely rich* feature set.

.. break

.. raw:: pdf

    Spacer 0 40

.. container:: align-center

    **Which you will learn today!**

.. |hdf_group| image:: img/hdf_logo.jpg
                :scale: 70%
                :align: middle
                :target: http://www.hdfgroup.org/


A Note on the Format
=================================
Intermixed, there will be:

* Slides
* Interactive Hacking
* Exercises

.. break

Feel free to:

* Ask questions at anytime 
* Explore at your own pace.

A Note on the Format
=================================
This tutorial was submitted to the *Advanced* track.

.. break

And this was slated to be *after* the IPython tutorial.  So...

.. break

.. container:: align-center

    **Get the Program Committee!**

.. image:: img/angry-mob.jpg
    :align: center
    :scale: 250%

.. container:: gray-and-small

    ~please don't!

Warm up exercise
===============================
In IPython:

.. raw:: pdf

    Spacer 0 20

.. code-block:: python

    import numpy as np
    import tables as tb

    f = tb.openFile('temp.h5', 'a')
    heart = np.ones(42, dtype=[('rate', int), ('beat', float)])
    f.createTable('/', 'heart', heart)
    f.close()

.. raw:: pdf

    Spacer 0 20

Or run ``python exer/warmup.py``

Warm up exercise
===============================
You should see in ViTables:

.. image:: img/warmup.png
    :align: center
    :scale: 35%


Questions
===============================
.. image:: img/qm.jpg
    :scale: 55%

.. raw:: pdf

    Spacer 0 20

.. container:: gray-and-small

    Image source: http://www.fotopedia.com/items/flickr-2200500024




