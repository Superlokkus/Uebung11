#!/usr/bin/python
# encoding=utf-8

"""Übung 11 Stratosphärensprung"""
#Markus Klemm WS12/13 Phy-BA

import matplotlib.pyplot as plt
import scipy as sc
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


def MoveEqua(t):
    return 