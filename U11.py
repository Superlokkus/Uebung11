#!/usr/bin/python
# encoding=utf-8

"""Übung 11 Stratosphärensprung"""
#Markus Klemm WS12/13 Phy-BA

from __future__ import division
import matplotlib.pyplot as plt
import scipy as sp
import scipy.integrate
from matplotlib import pyplot as plt


#Konstanten
rho0 = 1.204 #kg/m^3
mMMAtm = 0.029 #kg/mol
g = 9.81 #m/s^2
R = 8.314 #J*mol*K^-1
T = 450 #K
c_w = 0.25
m = 130 #kg
R_E = 6356e3 #m
A = 0.45 #m^2
h = 39045 #m
h_0 = 1585 #m

def MoveEqua(y,AB):
    """Gibt die Ableitungen der GL zurück.
        
    Erwartet AB[0] als z Anfangsbedingung und AB[1] als v AB"""
    
    return sp.array([y[1],0.5*m**-1*rho0*sp.e**((-mMMAtm*g*y[0])/(R*T)) * c_w*A*y[1]**2
    - g*(R_E/(R_E + y[0]))**2])
    

h_und_v = sp.integrate.odeint(MoveEqua,sp.array([h,0]),sp.linspace(0,200))

print h_und_v
