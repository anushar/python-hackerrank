# read in square matrix and print determinant
# Here is the option to use the _ variable, which in reality, is just another variable.
#for _ in range(n):
#    do_something()
#Note that _ is assigned the last result that returned in an interactive python session:
#>>> 1+2
#3
#>>> _
#3

import numpy
n=input()
a=numpy.array([raw_input().split() for j in range (n)],float)
print numpy.linalg.det(a) 
