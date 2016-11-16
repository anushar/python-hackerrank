#Find the probability that at least one of the  indices selected will contain the letter: 'a'.  
#Input Format
#The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of  #space-separated lowercase English letters, denoting the elements of the list A. 
#The third and the last line of input contains the integer K, denoting the number of indices to be selected. 
#Output Format
#Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'. 


import sys,itertools  
raw_input() 
a=raw_input().split()
k=int(raw_input()) 
num=0 
den=0 
for e in itertools.permutations(a,k):  
  den+=1  
  num+='a' in e[:k] 

print(num*1.0/den) 
