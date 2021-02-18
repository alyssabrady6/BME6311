# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:42:45 2021

@author: Alyssa Brady
"""

from matplotlib import pyplot
from numpy.random import seed 
from numpy import mean
from numpy import random
import numpy as np
from scipy.stats import norm
from scipy.stats import kstest
from scipy.stats import kstest
from scipy.stats import stats

mu, sigma = 0,0.01
x = np.random.normal(mu, sigma, 100)
print(mean(x))
pyplot.hist(x)
pyplot.show()
norm=[np.mean(np.random.normal(mu, sigma, 100)) for _i in range(1000)]
print(norm)

#histogram plot
pyplot.hist(norm)
plt.xlabel("Frequency")
plt.ylabel("Probability Density")
plt.title ("Histogram plot for 100 samples from Random Normal Distribution")
pyplot.show()

#Z-score KS test 
stats.kstest(stats.zscore(norm), "norm")


#poisson
seed (2)
t=np.random.poisson(lam=3,size=(100))
print(mean(t))
pyplot.hist(t)
plt.xlabel("Frequency")
plt.ylabel("Probability Density")
plt.title ("Histogram plot for Random Poisson Distribution of 100 samples (lambda=3)")
pyplot.show()

s = [np.mean(np.random.poisson(3,100)) for _i in range(1000)]
pyplot.hist(s)
plt.xlabel("Frequency")
plt.ylabel("Probability Density")
plt.title ("Histogram plot for means of 100 samples from Random Poisson Distribution (lambda=3)")
pyplot.show()

# test normality with KS test
stats.kstest(stats.zscore(s), stats.zscore(norm))



