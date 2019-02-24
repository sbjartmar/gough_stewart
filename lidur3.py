# -*- coding: utf-8 -*-

#Setjum inn söfn og f-fallið okkar úr lið 1.
import numpy as np
import math
import matplotlib.markers as marker
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from shapely.geometry.polygon import LinearRing, Polygon
from lidur1 import f, f1, f4

def graf(L1, L2, L3, gamma, p1, p2, p3, x1, x2, y2, theta):
    #Reiknum út hnitin fyrir punktana okkar.
    #fyrir lið 4:
    if y2 == 6:
        (x, y) = f4(theta, skila_xy=True)
    else: (x, y) = f(theta, skila_xy=True)
    (x4, y4) = (x + L2*np.cos(theta + gamma), y + L2*np.sin(theta + gamma))
    (x3, y3) = (x + L3*np.cos(theta), y + L3*np.sin(theta))
    ring = LinearRing([[x4, y4], [x3, y3], [x,y], [x4, y4]])
    t, p = ring.xy
 
    #Hérna erum við með bilin fyrir hverja línu (strut).
    range1  = np.arange(min(0,x), max(0,x), 10**-5)
    range2 = np.arange(min(x2,x4), max(x2,x4), 10**-5)
    range3 = np.arange(min(x3,x1), max(x1,x3), 10**-5)

    #Myndin sem við viljum birta.
    fig = plt.figure(1, figsize=(6,6), dpi=90)

    #Hérna bætum við hlutum á myndina okkar, tri er þríhyrningur og 
    # restin línurnar (struts).
    tri = fig.add_subplot(111)
    line1 = fig.add_subplot(111)
    line2 = fig.add_subplot(111)
    line3 = fig.add_subplot(111)

    #Plotta línurnar og þríhyrninginn
    line1.plot(range1, (y/x)*range1, linewidth=1.0, c='b')
    line2.plot(range2, ((y2-y4)/(x2-x4))*range2+y2, linewidth=1.0, c='b')
    line3.plot(range3, ((y3)/(x3-x1))*range3-((y3)/(x3-x1))*x1, linewidth=1.0, c='b')
    tri.plot(t,p, linewidth=3.0, c='b', marker='o')

    #Setja limit á ásana okkar.
    xmax = math.ceil(max(x, x1, x2, x3, x4))
    xmin = math.floor(min(x, x1, x2, x3, x4))
    ymax = math.ceil(max(y, y2, y3, y4))

    xrange = [xmin, xmax]
    yrange = [0, ymax+1]
    tri.set_xlim(*xrange)
    tri.set_xticks(np.arange(xmin,xmax+1, step=1))
    tri.set_ylim(*yrange)
    tri.set_yticks(np.arange(*yrange))
    tri.set_aspect(1)

    plt.title(r'$\theta =$' + str(theta))


    #Punktar á grafið.
    punkt1 = fig.add_subplot(111)
    punkt2 = fig.add_subplot(111)
    punkt3 = fig.add_subplot(111)
    punkt4 = fig.add_subplot(111)
    punkt5 = fig.add_subplot(111)
    punkt6 = fig.add_subplot(111)

    punkt1.plot(0, 0, marker='o', c='b')
    punkt2.plot(x2, y2, marker='o', c='b')
    punkt3.plot(x3, y3, marker='o', c='b')
    punkt4.plot(x4, y4, marker='o', c='b')
    punkt5.plot(x, y, marker='o', c='b')
    punkt5.plot(x1, 0, marker='o', c='b')

    #Sýna loks grafið.
    plt.show()
    return 0

def main():
    #Hérna er þægilegra að nota öll gildin sem breytur.
    L1 = 2
    L2 = np.sqrt(2)
    L3 = np.sqrt(2)
    gamma = (np.pi/2)
    p1 = np.sqrt(5)
    p2 = np.sqrt(5)
    p3 = np.sqrt(5)
    x1 = 4
    x2 = 0
    y2 = 4
    theta = -np.pi/4
    theta2 = np.pi/4
    graf(L1, L2, L3, gamma, p1, p2, p3, x1, x2, y2, theta)
    graf(L1, L2, L3, gamma, p1, p2, p3, x1, x2, y2, theta2)


if __name__== "__main__":
    main()