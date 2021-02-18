# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:38:06 2021

@author: Alyssa Brady
"""

from numpy.random import seed
from numpy.random import randint
from numpy import mean
from matplotlib import pyplot
import matplotlib.pyplot as plt
from scipy.stats import kstest
from scipy.stats import stats
seed (1)

#generate sample die roll (100 times) data for 12-sided die
rolls=randint(1, 13,100)
print(rolls)
print(mean(rolls))

#demonstration of central limit theorem
# seed the random number generator
seed(1)

# calculate the mean of 100 dice rolls 1000 times
means = [mean(randint(1, 13, 100)) for _ in range(1000)]
# plot the distribution of sample means
pyplot.hist(means)
plt.xlabel("Frequency")
plt.ylabel("Probability Density")
plt.title ("Histogram plot for 100 rolls 12-sided die")
pyplot.show()

#Z-score KS test
stats.kstest(stats.zscore(means), "norm")


#Shapiro-Wilk normailty test
from scipy.stats import shapiro
stat, p = shapiro(means)
print('Statistics={}, p={}'.format(stat, p))
alpha = 0.05
if p > alpha:
    print('Sample looks Normal so we do not reject H0')
else:
    print('Sample does not look Normal so we reject H0')
    
