#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:26:50 2021

@author: dennisblaufuss
"""
import numpy as np
import matplotlib.pyplot as plt

def JL(m, eps):
    n = (8 * np.log(m))/(eps**2)
    return n

eps = 0.1
m = np.arange(10,1010,10)

JL_bound = JL(m, eps)

plt.figure()
plt.plot(m, JL_bound)
plt.xlabel("number of data points")
plt.show()
