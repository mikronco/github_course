# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:57:01 2021

@author: Michele Ronco 
"""

import numpy as np 


np.random.seed(10) 

N = 100
X = np.random.rand(N,5)
y = 3*X[:,3] + 6*X[:,1] + np.random.normal(0,0.5,N) + 5

