# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:43:36 2022

@author: saham
"""

import math
a=[20,25,32,35,26]
mean, variance, deviation = 0,0,0
for i in a:
	mean=mean+i
mean/=5
for i in a:
	variance = variance + (mean-i)**2
variance = variance/5
deviation = math.sqrt(variance)
print(mean)
print(variance)
print(deviation)