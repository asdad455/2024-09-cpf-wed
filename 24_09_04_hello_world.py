# -*- coding: utf-8 -*-
"""24-09-04-hello-world

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zkFSqKTXtr0LC-_e_wNldJxQk25g8Yyg
"""

print("Hello World")

print("Hello Python")

import pylab as py

x_deg = py.arange(-180, 180+1,)
x_rad = py.deg2rad(x_deg)
y = py.sin(x_rad)

py.plot(x_deg, y)

py.xlabel('x (deg)')
py.ylabel('sin(x)')
py.grid(True)

