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

def MoveEqua(t,AB):
    """Gibt die Beschleunigung zurück für t.
    
    Erwartet AB[0] als z Anfangsbedingung und AB[1] als v AB"""
    
    return (0.5*m**-1*rho0*sp.e**((-mMMAtm*g*AB[0])/(R*T)) * c_w*A*AB[1]**2
    - g*(R_E/(R_E + AB[0]))**2)
    
zv = sp.empty([0])

for i in sp.linspace(h,h_0,200):
    if (i == h):#Anfangsbedingung für v
        zv = sp.append(zv,sp.integrate.odeint(MoveEqua,sp.array([i,0]),0))
    else:
        zv = sp.append(zv,sp.integrate.odeint(MoveEqua,sp.array([i,]),0))
    
print zv
   
#print sp.integrate.odeint(MoveEqua,sp.array([h,0]),0) #h und v kommt zurück
    
