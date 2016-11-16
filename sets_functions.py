# length is length of set A and second i/p line is A set of elements
# 3rd i/p is N number of other sets
# for each other set we have 2 attributes in i/p operation on other set and length of other set

length = int(raw_input())
A = set(map(int, raw_input().split()))
N = int(raw_input())
for i in range(N):    
  (operation_name, other_set_length) = raw_input().split()
  other_set = set(map(int, raw_input().split()))
  if operation_name == 'intersection_update': 
    A.intersection_update(other_set) 
  elif operation_name == 'update': 
    A.update(other_set)
  elif operation_name == 'symmetric_difference_update':
    A.symmetric_difference_update(other_set)    
  elif operation_name == 'difference_update':
    A.difference_update(other_set)    
  else:
    assert False
print sum(A)
