# -*- coding: utf-8 -*-

#Setjum inn söfn.
import numpy as np

#f-fallið okkar, prufum fallið fyrir theta = pi/4.
def f1(L1, L2, L3, gamma, p1, p2, p3, x1, x2, y2, theta, skila_xy):
    #Reiknum skv. formúlum í bók.
    A2 = L3*np.cos(theta) - x1
    B2 = L3*np.sin(theta)
    A3 = L2*np.cos(theta+gamma) - x2
    B3 = L2*np.sin(theta+gamma) - y2

    N1 = B3*(p2**2 - p1**2 - A2**2 - B2**2) - B2*(p3**2 - p1**2 - A3**2 - B3**2)
    
    D = 2*(A2*B3 - B2*A3)

    N2 = -A3*(p2**2 - p1**2 - A2**2 - B2**2) + A2*(p3**2 - p1**2 - A3**2 - B3**2)
    x = N1/D
    y = N2/D 
    fall = N1**2 + N2**2 - (p1*D)**2

    #Viljum búa til tilvik þar sem við viljum skurðpunktana x og y.
    if skila_xy == True:
        return x, y
    else:
        return fall

#f sem aðeins fall af theta.
def f(theta, skila_xy=False):
    return f1(2, np.sqrt(2), np.sqrt(2), np.pi/2, np.sqrt(5), np.sqrt(5), np.sqrt(5),
    4, 0, 4, theta, skila_xy)

#f fyrir lið 4.
def f4(theta, skila_xy):
    return f1(3, 3*np.sqrt(2), 3, np.pi/4, 5, 5, 3, 5, 0, 6, theta, skila_xy)

#f fyrir lið 5.
def f5(theta, skila_xy):
    return f1(3, 3*np.sqrt(2), 3, np.pi/4, 5, 7, 3, 5, 0, 6, theta, skila_xy)

#f sem er einnig fall af p2.
def f2(theta, p2, skila_xy):
    return f1(3, 3*np.sqrt(2), 3, np.pi/4, 5, p2, 3, 5, 0, 6, theta, skila_xy)

#f sem er aðeins fall af p2.
def f3(p2, skila_xy=False):
    def theta(theta):
        return f1(3, 3*np.sqrt(2), 3, np.pi/4, 5, p2, 3, 5, 0, 6, theta, skila_xy)
    return theta

def main():
    #Sjáum niðurstöður fyrir theta = pi/4.
    print f(np.pi/4)
 
if __name__== "__main__":
    main()