#!/bin/bash
PRESNAME="scopatz_scipy2012_flmake"

# save existing matplotlibrc
if [ -f ${HOME}/.matplotlib/matplotlibrc -a ! -f ${HOME}/.matplotlib/matplotlibrc.presbak ]; then
    mv ${HOME}/.matplotlib/matplotlibrc ${HOME}/.matplotlib/matplotlibrc.presbak
fi

# make slides with swapped matplotlibrc and filters
cp tools/matplotlibrc ${HOME}/.matplotlib/matplotlibrc
cp ${PRESNAME}.rst ${PRESNAME}.tmp.rst
python tools/pagenum_filter.py ${PRESNAME}.tmp.rst -o ${PRESNAME}.tmp.rst
python tools/slidebreak_filter.py ${PRESNAME}.tmp.rst -o ${PRESNAME}.tmp.rst
rst2pdf ${PRESNAME}.tmp.rst -b1 -s tools/slides.style,tango -o ${PRESNAME}.pdf --fit-background-mode=center
rm ${PRESNAME}.tmp.rst
rm ${HOME}/.matplotlib/matplotlibrc 

# replace blue links with another color
sed -i 's/0 0 .501961 [Rr][Gg]/.8671875 .188235 .188235 rg/' ${PRESNAME}.pdf


# replace matplotlibrc
if [ -f ${HOME}/.matplotlib/matplotlibrc.presbak ]; then
    mv ${HOME}/.matplotlib/matplotlibrc.presbak ${HOME}/.matplotlib/matplotlibrc
fi
