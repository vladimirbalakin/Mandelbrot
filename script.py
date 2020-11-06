from tkinter import *
from time import *
from random import *
from math import *
from tkinter import Tk

root = Tk()
root.title("Input")

w = 600
h = w
figure = [[0 for i in range(w)] for j in range(h)]
dots = [[0 for i in range(w)] for j in range(h)]

can = Canvas(root, width=w, height=h, bg='white')
can.pack()


class point():
	x = 0
	y = 0

class Vertex():
	x = 0
	y = 0
	visible = False

class polygon():
	def line(self, x, y, x1, y1):
		global can
		can.create_line(x, y, x1, y1)
		root.update()
		return

	mash = 50
	global w
	global h

	def get_rasm(self):
		global w, h
		for i in range(h // self.mash):
			self.line(0, i * self.mash, w, i * self.mash)
			self.line(i * self.mash, 0, i * self.mash, w)
		root.update()
		return

	def fill_cell(self, x, y):
		global w, h
		n1 = x // self.mash
		n2 = y // self.mash
		global can
		global figure
		figure[n1][n2] = 1
		can.create_rectangle(n1 * self.mash, n2 * self.mash, n1 * self.mash + self.mash, n2 * self.mash + self.mash,
		                     fill="#000000", outline="#1f1f1f")
	def aFillCell(self, x, y):
		global w, h
		n1 = x // self.mash
		n2 = y // self.mash
		global can
		global figure
		figure[n1][n2] = 1
		can.create_rectangle(n1 * self.mash, n2 * self.mash, n1 * self.mash + self.mash, n2 * self.mash + self.mash,
		                     fill="#1f1f1f", outline="#000000")

	def fill_dot(self, x, y):
		global can
		global dots
		x = x // self.mash * self.mash
		y = y // self.mash * self.mash
		nx = x // self.mash
		ny = y // self.mash
		dots[nx][ny] = 1
		can.create_oval(x-2, y-2, x+2, y+2, fill="red", outline="red")

	def upd(self):
		global figure
		for i in range(len(figure)):
			for j in range(len(figure[i])):
				if figure[i][j]:
					self.fill_cell(self.mash * i + 1, self.mash * j + 1)
				else:
					self.aFillCell(self.mash * i + 1, self.mash * j + 1)

def upd_mouse(event):
	x = event.x
	y = event.y
	global mouse
	mouse.x = x
	mouse.y = y
	return


def getError(event):
	global root
	root.destroy()
	root_ = Tk()
	root_.title("Error!")
	l1 = Label(text='Error!', font='Arial 32')
	l1.pack()
	root_.mainloop()


def putFill():
	global mouse
	global poly
	#poly.fill_cell(mouse.x, mouse.y)
	poly.fill_cell(mouse.x, mouse.y)

def startFilling(event):
	global filling
	filling = True

def endFilling(event):
	global filling
	filling = False

def putFillOn():
	global main
	main = True


def putFillOff(event):
	global filling
	filling = False
	global main
	main = False

poly = polygon()
poly.mash = 30
poly.get_rasm()
mouse = point()
main = True
filling = False

putFillOn()

root.bind('<Motion>', upd_mouse)
root.bind('<ButtonPress-1>', startFilling)
root.bind('<ButtonRelease-1>', endFilling)
root.bind('<e>', putFillOff)

while main:
	if filling:
		putFill()
	can.update()
while True:
	sleep(0.5)
	for i in figure:
		for j in i:
			if j:
				j = (j + randint(0, 4)) % 2
	poly.upd()
	can.update()