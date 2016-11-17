# given input of maimum number N,print 1 to N decima,binary and hex values and width of column is equal to binary width of that number
N = int(raw_input())
width = len('{:b}'.format(N))
for i in range(1, N+1):    
  print str.rjust(str(i), width),\        
  str.rjust('{:o}'.format(i), width),\        
  str.rjust('{:X}'.format(i), width),\        
  str.rjust('{:b}'.format(i), width)
