# substitution with a pattern
# Given input of number of lines n
# each line of n is string which has to be replaced 
# replace && with and, || with or
import re 
n=int(raw_input()) 
for i in range(n):      
  s=raw_input()      
  s1= re.sub(r"( && )",' and ',s)      
  while s1!=s:          
    s=s1          
    s1= re.sub(r"( && )",' and ',s)      
    s2=re.sub(r"( \|\| )",' or ',s1)      
   while s2!=s1:          
    s1=s2          
    s2=re.sub(r"( \|\| )",' or ',s1)      
   print(s2) 
