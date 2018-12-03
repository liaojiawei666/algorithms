import scipy
from scipy.stats import chisquare
import numpy
observ0=numpy.array([25,38,40,20,37,44])
test0=scipy.stats.chisquare(observ0)
print(test0)
