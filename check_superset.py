# check if set is strict superset
#The first line contains the space separated elements of set A.
#The second line contains integer N, the number of other sets. 
#The next N lines contains the space separated elements of the other sets.
#Print True if set A is a strict superset of all other N sets. Otherwise, print False

A = set(map(int,raw_input().split()))
cm = True
for i in range(int(raw_input())):
  B = set(map(int,raw_input().split()))
  cm = cm and (A>B) 
print cm
