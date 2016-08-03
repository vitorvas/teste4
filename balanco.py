#!/usr/bin/python3

# This program calculates mass balance of of a flow.
# Input:
# Q [W], rho [g/m^3], U [m/s], a [m^2], Cp [J/g*K], Ti [K]
#
# Output: Tf [K] = Final temperature
#
# Formule: Q'=m'Cp dT, where Q' is in Watts (J/s) and
# m' is density * velocity * area which fives g/s.
#
# Vitor Vasconcelos
# 03/08/2016

Q = float(input('Q [W]= '))
rho = float(input('rho [g/m^3]= '))
U = float(input('U [m/s]= '))
a = float(input('a [m^2]= '))
Cp = float(input('Cp [J/g.K]= '))
Ti = float(input('Ti [K or Celsius]= '))

Tf = (Q/(rho*U*a*Cp))+Ti

print('Final temperature is ' + str(Tf))
