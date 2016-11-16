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
N = int(raw_input())
A = numpy.array([input().split() for _ in range(N)], float)
print(numpy.linalg.det(A))
