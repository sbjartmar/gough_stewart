# -*- coding: utf-8 -*-

#Setjum inn söfn og f-fallið okkar úr lið 1.
import numpy as np
import scipy.optimize as sci
from lidur1 import f1, f2, f3
import time
from rootfinder import find_all_roots

#Skilgreinum fall rot sem tekur inn upphafsbil (a,b), fjölda róta í núlli, n1 og tolerance fyrir bilunum.
def rot(a, b, n1, tol=0.001):
        while a < 9.99:
                #Finnum allar rætur á bilinu -pí:pí fyrir p2. 
                x_2, x_2p, y_2p = find_all_roots(f3(b), -np.pi, np.pi)
                x_3, x_3p, y_3p = find_all_roots(f3(b-tol), -np.pi, np.pi)
                #Fjöldi róta er lengd fylkisins sem inniheldur þær.
                n2 = len(x_2)
                n3 = len(x_3)
                if n3 != n2:
                        print(a,b)
                        print(x_2p)
                        #Skilyrði fyrir fallinu til að ljúka. 
                        if b > 11: break
                        a = b + 0.001
                        b = a + 0.01
                        x_1, x_1p, y_1p = find_all_roots(f3(a), -np.pi, np.pi)
                        n1 = len(x_1)
                #Ef fjöldi róta er sá sami höldum við áfram.
                if n1 == n2:
                        b = b + 0.01
                #Ítrum niður.
                else:
                        b = b - 0.00001
#Köllum á fallið.
rot(0.0, 1.0, 0)
