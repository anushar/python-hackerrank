
#If set  is subset of set , print True.
#If set  is not a subset of set , 
#input mode
#The first line will contain the number of test cases, T.
#The first line of each test case contains the number of elements in set A. 
#The second line of each test case contains the space separated elements of set A .
#The third line of each test case contains the number of #elements in set B. 
#The fourth line of each test case contains the space separated elements of set B.

for i in range(int(input())): #More than 4 lines will result in 0 score. Do not leave a blank line also.     
a = int(input()); A = set(input().split())
b = int(input()); B = set(input().split())
print(A <= B)
