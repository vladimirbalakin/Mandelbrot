from MS import generateMS
from JS import generateJS
import numpy as np
from math import sin, cos, pi
generateMS()
a = 0  #(0..2*Pi)
r = 0.7885
for a in np.linspace(0, 2 * pi, 50):
    c = r * cos(a) + 1j * r * sin(a)
    #c = -1.285 + 0.01j
    generateJS(c)