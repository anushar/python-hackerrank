
# read coeff's of polygon from stdin and find value of polygon at x
import numpy

coeff = numpy.array(raw_input().split(),float)
x = int(raw_input())
print numpy.polyval(coeff,x)
