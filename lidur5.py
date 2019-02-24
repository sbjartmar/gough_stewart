# -*- coding: utf-8 -*-

#Setjum inn söfn og f-fallið okkar úr lið 1.
import numpy as np
import scipy.optimize as sci
import matplotlib.markers as marker
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from shapely.geometry.polygon import LinearRing, Polygon
from lidur1 import f1, f, f2, f3, f4, f5
from lidur3 import graf

#Búum til graf af fallinu okkar, og notum grid til að sýna nálægð
# við núllpunktinn í theta = +-pi/4.
x = np.arange(-np.pi, np.pi, 10**-5)
plt.title('f sem fall af ' + r'$\theta, p2 = 7$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$f(\theta)$')
plt.grid(True)
plt.plot(x, f2(x, 7, False))
plt.show()

#Finnum rætur með fsolve aðferðinni í Scipy pakkanum, setjum lausnir í 
# fylkið A.

A = np.zeros((6,1), dtype=float)

#Finnum rætur. Sjáum á grafi hvar þær eru u.þ.b.
x1 = sci.fsolve(f5, 2.5, args=(False), epsfcn = 0.1)
A[0] = x1
x2 = sci.fsolve(f5, -0.35, args=(False), epsfcn = 0.1)
A[1] = x2
x3 = sci.fsolve(f5, -0.65, args=(False), epsfcn = 0.1)
A[2] = x3
x4 = sci.fsolve(f5, 0.0, args=(False), epsfcn = 0.1)
A[3] = x4
x5 = sci.fsolve(f5, 0.45, args=(False), epsfcn = 0.1)
A[4] = x5
x6 = sci.fsolve(f5, 0.9, args=(False), epsfcn = 0.1)
A[5] = x6

for i in range (0, len(A)):
    plt.title('f sem fall af ' + r'$\theta$')
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$f(\theta)$')
    plt.grid(True)
    graf(3, 3*np.sqrt(2), 3, np.pi/4, 5, 7, 3, 5, 0, 6, A[i])



