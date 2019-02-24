# -*- coding: utf-8 -*-

#Setjum inn söfn og f-fallið okkar úr lið 1.
import numpy as np
import matplotlib.pyplot as plt
from lidur1 import f

#Bilið okkar sem er -pi:pi með gildum teknum á 10**-5 millibili.
x = np.arange(-np.pi, np.pi, 10**-5)

#Búum til graf af fallinu okkar, og notum grid til að sýna nálægð
#við núllpunktinn í theta = +-pi/4.
plt.title('f sem fall af ' + r'$\theta$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
plt.plot(x, f(x, skila_xy=False))
plt.show()

