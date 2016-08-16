
# coding: utf-8

# In[2]:

#function that computes for the height
from math import pi
G = 6.67e-11
M = 5.97e24
R = 6371000
def h(T):
    h = ((G*M*T**2)/(4*pi**2))**(1./3) - R
    return h

