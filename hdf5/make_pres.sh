#!/bin/bash
PRESNAME="scopatz_scipy2012_hdf5"

# save existing matplotlibrc
if [ -f ${HOME}/.matplotlib/matplotlibrc -a ! -f ${HOME}/.matplotlib/matplotlibrc.presbak ]; then
    mv ${HOME}/.matplotlib/matplotlibrc ${HOME}/.matplotlib/matplotlibrc.presbak
fi

# make slides with swapped matplotlibrc
cp matplotlibrc ${HOME}/.matplotlib/matplotlibrc
rst2pdf ${PRESNAME}.rst -b1 -s slides.style -o ${PRESNAME}.pdf --fit-background-mode=center
rm ${HOME}/.matplotlib/matplotlibrc

# replace matplotlibrc
if [ -f ${HOME}/.matplotlib/matplotlibrc.presbak ]; then
    mv ${HOME}/.matplotlib/matplotlibrc.presbak ${HOME}/.matplotlib/matplotlibrc
fi


