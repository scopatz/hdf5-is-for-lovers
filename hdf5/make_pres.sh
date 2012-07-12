#!/bin/bash
PRESNAME="scopatz_scipy2012_hdf5"

# save existing matplotlibrc
if [ -f ${HOME}/.matplotlib/matplotlibrc -a ! -f ${HOME}/.matplotlib/matplotlibrc.presbak ]; then
    mv ${HOME}/.matplotlib/matplotlibrc ${HOME}/.matplotlib/matplotlibrc.presbak
fi

# make slides with swapped matplotlibrc
cp matplotlibrc ${HOME}/.matplotlib/matplotlibrc
python pagenum_filter.py ${PRESNAME}.rst ${PRESNAME}.tmp.rst
rst2pdf ${PRESNAME}.tmp.rst -b1 -s slides.style -o ${PRESNAME}.pdf --fit-background-mode=center
rm ${PRESNAME}.tmp.rst
rm ${HOME}/.matplotlib/matplotlibrc 

# replace blue links with another color
sed -i 's/0 0 .501961 [Rr][Gg]/.8671875 .188235 .188235 rg/' ${PRESNAME}.pdf


# replace matplotlibrc
if [ -f ${HOME}/.matplotlib/matplotlibrc.presbak ]; then
    mv ${HOME}/.matplotlib/matplotlibrc.presbak ${HOME}/.matplotlib/matplotlibrc
fi
