#!/usr/bin/python
## python template
'''
    This script has the basic to
    use gnuplot with python.
    Notice that it produce a plot in the
    monitor and also write a file (pdf)
    to the disk
'''


import numpy
import Gnuplot

def rainfall_intensity_t10(t):
    return 32.23 * (t**(-0.713))

def rainfall_intensity_t50(t):
    return 55.06 * (t**(-0.713))

def rainfall_intensity_t80(t):
    return 75.06 * (t**(-0.713))

g = Gnuplot.Gnuplot()

g.title("rainfall intensity")
g.xlabel("t (min)")
g.ylabel("i (mm/min)")

g('set grid')
g('set key top left box')
#g('set xtic 10')
#g('set ytic 1')
g('set style line 1 ps 0.5 lc rgb "#ff0000"')
g('set style line 2 ps 0.5 lc rgb "#ff4f00"')
g('set style line 3 ps 0.4 lc rgb "#0000ff"')
g('set style line 4 ps 0.4 lc rgb "#0099ff"')
g('set style line 5 ps 0.4 lc rgb "#00ff00"')
g('set style line 6 ps 0.4 lc rgb "#00ff99"')

#g('set label "Pure Share Memory" at graph 0.5, 1.035 center font "Arial,11"')
g('set logscale y')

x = numpy.arange (start=2, stop=24, step=0.5, dtype='float_')

y1 = rainfall_intensity_t10(x) # yields another numpy.arange object
y2 = rainfall_intensity_t50(x) # ...
y3 = rainfall_intensity_t80(x) # ...

d1 = Gnuplot.Data (x, y1, title="intensity i (T=10)", with_="lines ls 4")
d2 = Gnuplot.Data (x, y2, title="intensity i (T=50)", with_="lines ls 5")
d3 = Gnuplot.Data (x, y3, title="intensity i (T=80)", with_="lines ls 6")
 
g("set terminal qt")
g.plot(d1,d2,d3) # write pdf data directly to stdout ...
raw_input("\nPress return to exit")


g.hardcopy (filename='rainfall-intensity.pdf', terminal='pdf') # write last plot to another terminal
#g.hardcopy (filename='rainfall-intensity.png', terminal='png') # write last plot to another terminal
#g.hardcopy (filename='rainfall-intensity.svg', terminal='svg') # ...
del g

