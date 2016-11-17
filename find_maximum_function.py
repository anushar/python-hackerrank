#Find the maximized value  Smax obtained.%  denotes the modulo operator. 
#Input Format  
#The first line contains  space separated integers  and . 
#The next  lines each contains an integer  followed by  space separated integers denoting the elements in the list. 
#Output Format  Output a single integer denoting the value . 

import itertools
(K, N) = map(int, raw_input().split()) 
L = list() 
for i in range(K):     
  l = map(int, raw_input().split())    
  n = l[0]     
  L.append(l[1:])     
  assert len(L[i]) == n 
  
 S_max = 0 
 L_max = None 
 
for l in itertools.product(*L):     
  s = sum([x**2 for x in l]) % N     
  if s > S_max:         
    S_max = s         
    L_max = l         
print S_max 
