from tkinter import *
from time import *
from random import *
from math import *
from tkinter import Tk
import numpy as np

root = Tk()
root.title("No title here!")

w = 300
h = w
figure = [[0 for i in range(w)] for j in range(h)]

can = Canvas(root, width = w, height = h, bg = 'white')
can.pack()

class Vertex():
	x = 0
	y = 0
	visible = False

class polygon():
    def line(self, x, y, x1, y1, width_):
        global can
        can.create_line(x * self.mash, y * self.mash, x1 * self.mash, y1 * self.mash, width = width_)
        root.update()
        return

    def red_line(self, x, y, x1, y1, width_):
        global can
        can.create_line(x * self.mash, y * self.mash, x1 * self.mash, y1 * self.mash, width = width_, fill = "red")
        can.update()
        return

    def dot(self, x, y, width_):
        global can
        can.create_oval(x * self.mash - width_, y * self.mash - width_, x * self.mash + width_, y * self.mash + width_, fill = "red")
        can.update()
        return

    mash = 10
    global w
    global h    
    center = h // 2 // mash

    def centerRedefinition(self):
        global h
        self.center = h // 2 // self.mash

    def get_rasm(self):
        global w, h
        for i in range(h // self.mash):
            self.line(0, i, w, i, 0.1)
            self.line(i, 0, i, w, 0.1)
        root.update()
        return
    def fill_cell(self, x, y):
        global w, h
        n1 = int(x // self.mash)
        n2 = int(y // self.mash)
        global can
        global figure
        figure[n1][n2] = 1
        can.create_rectangle(n1 * self.mash, n2 * self.mash, n1 * self.mash + self.mash, n2 * self.mash + self.mash,
                            fill="#000000", outline="#000000")
    def aFillCell(self, x, y, color):
        global w, h
        n1 = int(x // self.mash)
        n2 = int(y // self.mash)
        global can
        global figure
        figure[n1][n2] = 1
        can.create_rectangle(n1 * self.mash, n2 * self.mash, n1 * self.mash + self.mash, n2 * self.mash + self.mash,
                                fill="white", outline="white")

    def fill_dot(self, x, y):
        global can
        x = x // self.mash * self.mash
        y = y // self.mash * self.mash
        nx = x // self.mash
        ny = y // self.mash
        can.create_oval(x-2, y-2, x+2, y+2, fill="red", outline="red")

    def upd(self):
        global figure
        for i in range(len(figure)):
            for j in range(len(figure[i])):
                if not(figure[i][j]):
                    self.fill_cell(self.mash * (i + 0.1), self.mash * (j + 0.1))
                else:
                    self.aFillCell(self.mash * (i + 0.1), self.mash * (j + 0.1), figure[i][j])


poly = polygon()
poly.mash = 1
poly.centerRedefinition()
#poly.get_rasm()
#poly.line(0, h // 2 // poly.mash, h, h // 2 // poly.mash, 2)
#poly.line(h // 2 // poly.mash, 0, h // 2 // poly.mash, h, 2)
a = 1+0.1j
b = 0+1j
c = a
#poly.red_line(poly.center, poly.center, poly.center + a.real, poly.center - a.imag, 0.00000001)
#poly.red_line(poly.center, poly.center, poly.center + b.real, poly.center - b.imag, 3)
#for i in range(1, 17):
    #c = a ** (2 ** i)
    #poly.dot(poly.center + c.real, poly.center - c.imag, 2)
    #poly.red_line(poly.center, poly.center, poly.center + c.real, poly.center - c.imag, 0.1)
    #sleep(0.5)
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
maxIter = 300
infBord = 10
for ip, p in enumerate(np.linspace(pmin, pmax, h)):
    for iq, q in enumerate(np.linspace(qmin, qmax, w)):
        c = p + 1j * q
        z = 0
        for k in range(maxIter):
            z = z*z + c
            if (abs(z) > infBord):
                figure[ip][iq] = k
                break
poly.upd()
can.mainloop()