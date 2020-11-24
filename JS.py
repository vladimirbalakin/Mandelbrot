from pygame import *
import numpy as np
import sys
from math import pi, sin, cos
from time import sleep
w, h = 150, 150
figure = [[0 for i in range(w)] for i in range(h)]
init()
root = display.set_mode((w, h))
display.set_caption("MS")

def getFigure():
    for i in range(h):
        for j in range(w):
            draw.circle(root, (figure[i][j] % 255, figure[i][j] % 255, figure[i][j] % 255), (i, j), 0, 1)

def generateJS(c):
    xmin, xmax, ymin, ymax = -2.5, 1.5, -2, 2
    infBorder = 4
    maxIter = 255
    for ix, x in enumerate(np.linspace(xmin, xmax, h)):
        for iy, y in enumerate(np.linspace(ymin, ymax, w)):
            #c = x + 1j * y
            z = x + 1j * y
            for k in range(maxIter):
                z = (z*z) + c
                #print(z)
                if abs(z) > infBorder:
                    figure[ix][iy] = 3 * k
                    draw.circle(root, (figure[ix][iy] % 255, figure[ix][iy] % 255, figure[ix][iy] % 255), (ix, iy), 1, 1)
                    break
    #getFigure()
    print("End")
    #print(figure)

a = 0  #(0..2*Pi)
r = 0.7885
for ia, a in enumerate(np.linspace(0, 2 * pi, 75)):
    c = r * cos(a) + 1j * r * sin(a)
    #c = -1.285 + 0.01j
    generateJS(c)
    display.flip()
    image.save(root, str(ia) + ".png")
    #sleep(0.1)
#draw.circle(root, (255, 0, 0), (50, 50), 0, 3)
while True:
    for i in event.get():
        if i.type == QUIT:
            display.quit()
            sys.exit()
            break
    display.flip()