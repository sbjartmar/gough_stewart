# -*- coding: utf-8 -*-

#Setjum inn söfn og f-fallið okkar úr lið 1.
import numpy as np
import scipy.optimize as sci
import matplotlib.markers as marker
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from shapely.geometry.polygon import LinearRing, Polygon
from lidur1 import f1, f, f4
from lidur3 import graf

#Bilið okkar sem er -pi:pi með gildum teknum á 10**-5 millibili.
x = np.arange(-np.pi, np.pi, 10**-5)

#Búum til graf af fallinu okkar, og notum grid til að sýna nálægð
# við núllpunktinn í theta = +-pi/4.
plt.title('f sem fall af ' + r'$\theta$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
#Finnum rætur með fsolve aðferðinni í Scipy pakkanum, setjum lausnir í 
# fylkið A.
A = np.zeros((4,1), dtype=float)

for i in np.arange(-3,3):
    x = sci.fsolve(f4, i, args=(False))
    A[i+1] = x

graf(3, 3*np.sqrt(2), 3, np.pi/4, 5, 5, 3, 5, 0, 6, A[0])
plt.title('f sem fall af ' + r'$\theta$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
graf(3, 3*np.sqrt(2), 3, np.pi/4, 5, 5, 3, 5, 0, 6, A[1])
plt.title('f sem fall af ' + r'$\theta$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
graf(3, 3*np.sqrt(2), 3, np.pi/4, 5, 5, 3, 5, 0, 6, A[2])
plt.title('f sem fall af ' + r'$\theta$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
graf(3, 3*np.sqrt(2), 3, np.pi/4, 5, 5, 3, 5, 0, 6, A[3])



